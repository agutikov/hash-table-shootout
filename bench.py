import sys
import os
import subprocess
import signal
import asyncio
import multiprocessing

stopped = False

def handler(signum, frame):
    global stopped
    stopped = True

signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)


programs = [
    'std_unordered_map',
    'boost_unordered_map',
    #'google_sparse_hash_map',
    'google_dense_hash_map',
    #'google_dense_hash_map_mlf_0_9',
    'qt_qhash',
    'spp_sparse_hash_map',
    #'emilib_hash_map',
    'ska_flat_hash_map',
    'ska_flat_hash_map_power_of_two',
    'tsl_sparse_map',
    'tsl_hopscotch_map',
    'tsl_hopscotch_map_mlf_0_5',
    'tsl_hopscotch_map_store_hash',
    'tsl_robin_map',
    #'tsl_robin_map_mlf_0_9',
    'tsl_robin_map_store_hash',
    'tsl_robin_pg_map',
    'tsl_ordered_map',
    #'tsl_array_map',
    #'tsl_array_map_mlf_1_0'
    'judy_map_l',
    'judy_map_m',
    'judy_map_kdcell',
]

minkeys  =  2*100*1000
maxkeys  = 100*100*1000
interval =  2*100*1000
points = range(minkeys, maxkeys + 1, interval)
best_out_of = 5

outfile = open('output', 'w')

if len(sys.argv) > 1:
    benchtypes = sys.argv[1:]
else:
    benchtypes = ('insert_random_shuffle_range',
                  'read_random_shuffle_range', 
                  'insert_random_full',
                  'insert_random_full_reserve', 
                  'read_random_full',
                  'read_miss_random_full', 
                  'read_random_full_after_delete', 
                  'iteration_random_full',
                  'delete_random_full', 

                  'insert_small_string',
                  'insert_small_string_reserve', 
                  'read_small_string',
                  'read_miss_small_string', 
                  'read_small_string_after_delete', 
                  'delete_small_string',
                    
                  'insert_string',
                  'insert_string_reserve', 
                  'read_string',
                  'read_miss_string', 
                  'read_string_after_delete', 
                  'delete_string', )


async def run(program, nkeys, benchtype):
    cmd = f'./build/{program} {nkeys} {benchtype}'
    try:
        proc = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)

        stdout, stderr = await proc.communicate()

        words = stdout.strip().split()
        runtime_seconds = float(words[0])
        memory_usage_bytes = int(words[1])
        load_factor = float(words[2])
    except:
        print(f"Error with {cmd}\n{stderr}")
        return None
    return (runtime_seconds, memory_usage_bytes, load_factor)


parallellism = multiprocessing.cpu_count()


async def handle_tasks(results, tasks):
    global stopped
    while len(tasks) >= parallellism or (stopped and len(tasks) > 0):
        done, _ = await asyncio.wait(set(tasks.keys()), return_when=asyncio.FIRST_COMPLETED)

        for task in done:
            result = await task
            key = tasks[task]
            del tasks[task]
            #print(key, 'Done', results[key])

            if result is None:
                continue

            prev_result = results[key]

            fastest_result = prev_result[1]
            if result[0] < fastest_result[0]:
                    fastest_result = result

            results[key] = (prev_result[0] - 1, fastest_result)

            if prev_result[0] > 0:
                if not stopped:
                    # repeat
                    t = asyncio.create_task(run(*key))
                    tasks[t] = key
            else:
                # print fastest_result
                runtime_seconds, memory_usage_bytes, load_factor = fastest_result
                if runtime_seconds != 1000000:
                    program, nkeys, benchtype = key
                    line = ','.join(map(str, [benchtype,
                                            nkeys,
                                            program,
                                            "%0.2f" % load_factor, 
                                            memory_usage_bytes,
                                            "%0.6f" % runtime_seconds]))
                    print(line, file=outfile)
                    print(line)


async def main():
    global stopped
    results = {} # (nkeys, benchtype, program) -> (repeat_countdown, (runtime_seconds, memory_usage_bytes, load_factor))
    tasks = {} # task -> (nkeys, benchtype, program)

    for nkeys in points:
        for benchtype in benchtypes:
            for program in programs:
                if program.startswith('tsl_array_map') and 'string' not in benchtype:
                    continue
                if 'kdcell' in program and 'string' in benchtype:
                    continue

                if stopped and len(tasks) == 0:
                    print('Stopped. Exit.')
                    return

                key = (program, nkeys, benchtype)
                results[key] = (best_out_of - 1, (1000000, 0, 0))

                task = asyncio.create_task(run(*key))
                tasks[task] = key

                await handle_tasks(results, tasks)

    stopped = True
    await handle_tasks(results, tasks)


asyncio.run(main())
