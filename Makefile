
CXX=clang++
#CXX_FLAGS=-O3 -march=native -std=c++17 -DNDEBUG
CXX_FLAGS= -Werror -O2 -std=c++17 -DNDEBUG -ljemalloc

APPS = std_unordered_map boost_unordered_map
APPS+= google_sparse_hash_map google_dense_hash_map google_dense_hash_map_mlf_0_9
#APPS+= qt_qhash
APPS+= spp_sparse_hash_map
APPS+= emilib_hash_map
APPS+= ska_flat_hash_map ska_flat_hash_map_power_of_two
APPS+= tsl_hopscotch_map tsl_hopscotch_map_mlf_0_5 tsl_hopscotch_map_store_hash
APPS+= tsl_robin_map tsl_robin_map_mlf_0_9 tsl_robin_map_store_hash tsl_robin_pg_map
APPS+= tsl_sparse_map
APPS+= tsl_ordered_map
APPS+= tsl_array_map tsl_array_map_mlf_1_0
APPS+= judy_map_kdcell judy_map_l judy_map_m

PKG_CONFIG_PATH=/usr/lib/x86_64-linux-gnu/pkgconfig/

CXX_FLAGS+= -lm
CXX_FLAGS+= $(shell pkg-config --cflags --libs Qt5Core) -fPIC
CXX_FLAGS+= -Isparsepp
CXX_FLAGS+= -Iemilib
CXX_FLAGS+= -Iflat_hash_map
CXX_FLAGS+= -Ihopscotch-map
CXX_FLAGS+= -Irobin-map/include
CXX_FLAGS+= -Isparse-map/include
CXX_FLAGS+= -Iordered-map/include
CXX_FLAGS+= -Iarray-hash/include
CXX_FLAGS+= -Ijudyhash/libjudyhash -lJudy

BUILD_DIR=./build

EXECUTABLES = $(APPS:%=$(BUILD_DIR)/%)

all: | $(BUILD_DIR) $(EXECUTABLES)

$(EXECUTABLES): $(BUILD_DIR)/%: src/%.cc src/template.c
	$(CXX) $(CXX_FLAGS) -o $@ $<

$(BUILD_DIR):
	mkdir -p $@

clean:
	rm -f $(BUILD_DIR)/*

