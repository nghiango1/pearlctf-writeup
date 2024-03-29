# `ProjectTemplate/`

Copy this as the default template for `c` project with `make` tool

## Notes

### How to used

Build

```sh
make
```

Run

```sh
./dist/hello
```

### Project structure

This `c` project structure contain
- `src/` directory: Seperated module source file
    - `hello.c` contain main function
    - `world.c` contain a seperated functions that will be call by `hello.c`
- `include/` directory: Linked header file, which require by `c` lang so that `hello.c` can found the called function in `world.c`
    - `world.h` contain the explaination for `world.c`
- `Makefile` file: Contain the configuration for `make` tool, which being used to build the project
- `compile_commands.json` file: `clangd` LSP configuration file, which is auto generated by `bear` command. This help cland to properly parse the source code.
    ```sh
    bear -- make
    ```
- `build/`, `dist/` directory: Only available when build the code with `make` or `make all` from the project root directory. Containing object files (`build` directory) and built executed file (`dist` directory).

### More on `make` tool

`Makefile` configuration come with these default commands:
- `make` (or `make all`): create `dist` directory and build the code
    ```make
    all: $(DIST_DIR) $(TARGET)
    ```
    > This combine `make dist` and `make hello` command
- `make hello`: build the code
    ```make
    $(TARGET): $(OBJ_FILES)
        $(CC) $(DEBUG_FLAGS) -o $(DIST_DIR)/$(TARGET) $(OBJ_FILES)
    ```
    > This combine `make build/*.o` and call the `gcc` build
- `make build/<src_file_name>.o`: build the object file of sepecify source code file, also create `build` directory
    ```make
    $(BUILD_DIR)/%.o: $(SRC_DIR)/%.c | $(BUILD_DIR)
        $(CC) $(DEBUG_FLAGS) -I$(INCLUDE_DIR) -c $< -o $@
    ```
    > This have a wild cast to handle all `make build/<src>.o`, associate them with desired file in `src` directory, create `build` directory via `make build` command. Then call the `gcc` to build the object file
- `make build`: create `build` directory
    ```make
    $(BUILD_DIR):
        mkdir -p $(BUILD_DIR)
    ```
- `make dist`: create `dist` directory
    ```make
    $(DIST_DIR):
        mkdir -p $(DIST_DIR) 
    ```
    > Both just try to create `build` and `dist` directory if they didn't exist using `mkdir -p` command
- `make clean`: delete all build file and directory that being create by `make`
    ```make
    clean:
        rm -rf $(BUILD_DIR) $(DIST_DIR)
    ```
    > `rm -rf` all `build`, `dist` directory


