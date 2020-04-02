#include <inttypes.h>
#include <string>
#include <judy_map.h>


typedef judy_map_kdcell<int64_t, int64_t> hash_t;

#define SETUP hash_t hash;

#define RESERVE_INT(size)
#define LOAD_FACTOR_INT_HASH() 0.0f
#define INSERT_INT_INTO_HASH(key, value) hash.insert(hash_t::value_type(key, value))
#define DELETE_INT_FROM_HASH(key) hash.erase(key)
#define FIND_INT_EXISTING_FROM_HASH(key) if(hash.find(key) == hash.end()) { printf("error"); exit(1); }
#define FIND_INT_MISSING_FROM_HASH(key) if(hash.find(key) != hash.end()) { printf("error"); exit(2); }
#define FIND_INT_EXISTING_FROM_HASH_COUNT(key, count) if(hash.find(key) != hash.end()) { count++; }
#define CHECK_INT_ITERATOR_VALUE(iterator, value) if(iterator.second != value) { printf("error"); exit(3); }
#define ITERATE_HASH_CONST for (const auto& it : hash)


#define RESERVE_STR(size) { printf("not implemented"); exit(1); }
#define LOAD_FACTOR_STR_HASH() 0.0f
#define INSERT_STR_INTO_HASH(key, value) { printf("not implemented"); exit(1); }
#define DELETE_STR_FROM_HASH(key) { printf("not implemented"); exit(1); }
#define FIND_STR_EXISTING_FROM_HASH(key) { printf("not implemented"); exit(1); }
#define FIND_STR_MISSING_FROM_HASH(key) { printf("not implemented"); exit(1); }
#define FIND_STR_EXISTING_FROM_HASH_COUNT(key, count) { printf("not implemented"); exit(1); }

#include "template.c"
