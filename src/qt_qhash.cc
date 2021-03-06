#include <inttypes.h>
#include <functional>
#include <string>

uint qHash(const std::string &key) {
    return std::hash<std::string>()(key);
}

#include <QtCore/QHash>
typedef QHash<int64_t, int64_t> hash_t;
typedef QHash<std::string, int64_t> str_hash_t;


#define SETUP_INT hash_t hash;
#define RESERVE_INT(size) hash.reserve(size)
#define LOAD_FACTOR_INT_HASH() 0.0f
#define INSERT_INT_INTO_HASH(key, value) hash.insert(key, value)
#define DELETE_INT_FROM_HASH(key) hash.remove(key)
#define FIND_INT_EXISTING_FROM_HASH(key) if(hash.find(key) == hash.end()) { printf("error"); exit(1); }
#define FIND_INT_MISSING_FROM_HASH(key) if(hash.find(key) != hash.end()) { printf("error"); exit(2); }
#define FIND_INT_EXISTING_FROM_HASH_COUNT(key, count) \
    if(hash.find(key) != hash.end()) { count++; }
#define CHECK_INT_ITERATOR_VALUE(iterator, value) if(iterator.value() != value) { printf("error"); exit(3); }
#define ITERATE_HASH_CONST for(auto it = hash.begin(); it != hash.end(); ++it)


#define SETUP_STR str_hash_t str_hash;
#define RESERVE_STR(size) str_hash.reserve(size) 
#define LOAD_FACTOR_STR_HASH() 0.0f
#define INSERT_STR_INTO_HASH(key, value) str_hash.insert(key, value)
#define DELETE_STR_FROM_HASH(key) str_hash.remove(key);
#define FIND_STR_EXISTING_FROM_HASH(key) if(str_hash.find(key) == str_hash.end()) { printf("error"); exit(4); }
#define FIND_STR_MISSING_FROM_HASH(key) if(str_hash.find(key) != str_hash.end()) { printf("error"); exit(5); }
#define FIND_STR_EXISTING_FROM_HASH_COUNT(key, count) \
    if(str_hash.find(key) != str_hash.end()) { count++; }


#include "template.c"
