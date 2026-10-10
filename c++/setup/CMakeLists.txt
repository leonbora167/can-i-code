cmake_minimum_required(VERSION 3.20)

# Project metadata
project(CppWorkspace VERSION 1.0.0 LANGUAGES CXX)

# ==============================================================================
# C++ Language Standard Configuration
# Python analog: Setting your python version (e.g., Python 3.10 vs 3.12).
# Options: 11, 14, 17, 20, 23 (or 26 in cutting-edge compilers)
# ==============================================================================
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Export compile commands for VS Code / clangd intellisense support
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Define executable target
add_executable(CppApp main.cpp)

# Enable standard-conforming behavior and reasonable warnings
if(MSVC)
    target_compile_options(CppApp PRIVATE /Zc:__cplusplus /W4)
else()
    target_compile_options(CppApp PRIVATE -Wall -Wextra)
endif()

# For MinGW/GCC on Windows, statically link runtime to make standalone .exe
if(MINGW)
    target_link_options(CppApp PRIVATE -static -static-libgcc -static-libstdc++)
endif()

# ==============================================================================
# vcpkg Dependency Example:
# Once you add a package (e.g. fmt) to vcpkg.json, uncomment lines below:
# ==============================================================================
# find_package(fmt CONFIG REQUIRED)
# target_link_libraries(CppApp PRIVATE fmt::fmt)

