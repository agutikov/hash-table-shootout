#include <inttypes.h>
#include <string>
#include <tsl/array_map.h>

#include <experimental/string_view>
template<class CharT>
struct str_hash {
    std::size_t operator()(const CharT* key, std::size_t key_size) const {
        return std::hash<std::experimental::string_view>()(std::experimental::string_view(key, key_size));
    }
};

typedef tsl::array_map<char, int64_t, str_hash<char>> str_hash_t;

#include "hash_map_str_base.h"

#undef INSERT_STR_INTO_HASH
#define INSERT_STR_INTO_HASH(key, value) str_hash.insert(key, value)

#include "template.c"
