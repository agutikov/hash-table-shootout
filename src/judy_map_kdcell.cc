#include <inttypes.h>
#include <string>
#include <judy_map.h>


typedef judy_map_kdcell<int64_t, int64_t> hash_t;

#include "hash_map_int_base.h"

#undef RESERVE_INT
#define RESERVE_INT(size)

#undef LOAD_FACTOR_INT_HASH
#define LOAD_FACTOR_INT_HASH() 0.0f

#undef INSERT_INT_INTO_HASH
#define INSERT_INT_INTO_HASH(key, value) hash[key] = value


#include "template.c"
