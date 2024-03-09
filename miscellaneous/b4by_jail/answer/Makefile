# Compiler and flags
CC := gcc
CFLAGS := -Wall -Wextra
DEBUG_FLAGS := -fdiagnostics-plain-output -g

# Directories
SRC_DIR := src
INCLUDE_DIR := /usr/include/python3.10
BUILD_DIR := build
DIST_DIR := dist

# Source files
SRC_FILES := $(wildcard $(SRC_DIR)/*.c)
OBJ_FILES := $(patsubst $(SRC_DIR)/%.c,$(BUILD_DIR)/%.o,$(SRC_FILES))

# Executable name
TARGET := hello

# Rules
.PHONY: all clean

all: $(DIST_DIR) $(TARGET)

$(TARGET): $(OBJ_FILES)
	$(CC) $(DEBUG_FLAGS) -o $(DIST_DIR)/$(TARGET) $(OBJ_FILES)

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.c | $(BUILD_DIR)
	$(CC) $(DEBUG_FLAGS) -I$(INCLUDE_DIR) -c $< -o $@

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(DIST_DIR):
	mkdir -p $(DIST_DIR) 

clean:
	rm -rf $(BUILD_DIR) $(TARGET) $(DIST_DIR)

