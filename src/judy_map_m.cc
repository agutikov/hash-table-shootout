#include <inttypes.h>
#include <string>
#include <judy_map.h>

template<typename T>
struct id {
    size_t operator() (const T& v) const { return v; }
};

typedef judy_map_m<int64_t, int64_t, id<int64_t>> hash_t;
typedef judy_map_m<std::string, int64_t, std::hash<std::string>> str_hash_t;

#include "hash_map_int_base.h"
#include "hash_map_str_base.h"

#undef RESERVE_INT
#define RESERVE_INT(size)

#undef LOAD_FACTOR_INT_HASH
#define LOAD_FACTOR_INT_HASH() 0.0f


#undef RESERVE_STR
#define RESERVE_STR(size)

#undef LOAD_FACTOR_STR_HASH
#define LOAD_FACTOR_STR_HASH() 0.0f

#include "template.c"
