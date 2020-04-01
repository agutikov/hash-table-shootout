
import operator
import functools
import math

product = lambda values: functools.reduce(operator.mul, values, 1)

# collision probability

f = lambda N, k: 1 - product([x/N for x in range(N - k + 1, N)])

# https://preshing.com/20110504/hash-collision-probabilities/

f1 = lambda N, k: 1 - math.exp(-k*(k-1)/(2*N))

def comb(n, k):
    s = 1
    for x in range(1, k+1):
        s *= n - x + 1
        s /= x
    return s


print(f(365, 22)-f1(365, 22), f(365, 23)-f1(365, 23), f(365, 24)-f1(365, 24))

hash_size = 27

for p in range(1, 6):
    N = 2**hash_size
    k = 10**p
    print(f'N=2^{hash_size}, k={k}', f(N, k), f1(N, k)

# TODO: expected (with probability) number of collisions ???
# https://crypto.stackexchange.com/questions/27370/formula-for-the-number-of-expected-collisions


