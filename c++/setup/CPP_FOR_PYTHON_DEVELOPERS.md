# Modern C++ Development Guide for Python Developers

Welcome to C++! Coming from Python, you are used to a rich ecosystem (`pip`, `virtualenv`, `pyenv`, `pyproject.toml`). C++ has undergone a massive modernization over the last decade. This guide maps your existing Python knowledge directly to modern C++ concepts.

---

## 1. Quick Rosetta Stone (Python vs. C++)

| Concept | Python | Modern C++ (This Workspace) |
| :--- | :--- | :--- |
| **Language Spec / Version** | Python 3.8, 3.10, 3.12 (`pyenv`) | C++14, C++17, C++20, C++23 (`CMAKE_CXX_STANDARD`) |
| **Execution Engine** | CPython interpreter / PyPy | Compilers: MSVC (`cl`), GCC (`g++`), Clang (`clang++`) |
| **Package Manifest** | `requirements.txt` / `pyproject.toml` | `vcpkg.json` (Manifest mode) |
| **Package Installer** | `pip install <package>` | `.\vcpkg\vcpkg.exe add port <package>` |
| **Virtual Environment** | `.venv` | Local `vcpkg` + per-build `build/` directory |
| **Build / Project Manager**| `setuptools` / `poetry` / `flit` | `CMakeLists.txt` (CMake) |
| **Execution** | `python main.py` | `cmake --build build && .\build\CppApp.exe` |

---

## 2. Understanding "C++ Versions" vs "Python Versions"

In Python, the **runtime interpreter** and the **language version** are tied together (e.g., Python 3.12 interpreter runs Python 3.12 code).

In C++, there are **two separate layers**:

### A. The C++ Standard (The Language Specification)
ISO releases new C++ standards every 3 years:
- **C++11 / C++14**: Introduced auto, smart pointers, lambdas (the start of "Modern C++").
- **C++17**: Structured binding (tuple unpacking like Python `a, b = tup`), `std::optional`, `std::filesystem`.
- **C++20**: Major milestone: Concepts (type constraints), Ranges (Python-like iterators / generators), Coroutines, Modules.
- **C++23**: `std::print` (Python-like `print()`!), `std::expected`, multidimensional subscripts.

You change the language version inside [`CMakeLists.txt`](CMakeLists.txt):
```cmake
set(CMAKE_CXX_STANDARD 20)      # Switch to 17, 20, or 23
set(CMAKE_CXX_STANDARD_REQUIRED ON)
```
Or override it from the command line without editing code:
```powershell
cmake -B build -S . -DCMAKE_CXX_STANDARD=23
```

### B. The Compiler (The Compilation Engine)
Because C++ compiles to machine code, different vendors provide compilers implementing the standards:
1. **MSVC (Microsoft Visual C++)**: Default compiler on Windows (installed via Visual Studio / VS Build Tools).
2. **GCC (GNU Compiler Collection)**: Common on Linux, available on Windows via MinGW-w64 / WinLibs.
3. **Clang / LLVM**: Known for clear error messages and modern tooling.

You can have multiple compilers installed on the same Windows machine and tell CMake which one to use:
```powershell
# Using GCC (MinGW)
cmake -B build-gcc -G "MinGW Makefiles" -DCMAKE_CXX_COMPILER=g++

# Using Clang
cmake -B build-clang -G "Ninja" -DCMAKE_CXX_COMPILER=clang++

# Using Visual Studio (MSVC)
cmake -B build-msvc -G "Visual Studio 17 2022"
```

---

## 3. Package Management with vcpkg (The `pip` Equivalent)

We have installed Microsoft's **vcpkg** into the local workspace folder `./vcpkg`.

### How Manifest Mode Works (`vcpkg.json`)
Just like `requirements.txt` or `pyproject.toml`, [`vcpkg.json`](vcpkg.json) lists the packages your project needs.

#### 1. Adding a library (e.g. `fmt` for Python-like string formatting):
```powershell
.\vcpkg\vcpkg.exe add port fmt
```
Or open [`vcpkg.json`](vcpkg.json) and add it to `"dependencies"`:
```json
{
  "$schema": "https://raw.githubusercontent.com/microsoft/vcpkg-tool/main/docs/vcpkg.schema.json",
  "name": "cpp-workspace",
  "version-string": "1.0.0",
  "dependencies": [
    "fmt",
    "nlohmann-json",
    "cpr"
  ]
}
```
*(Common Python-like equivalents: `fmt` $\approx$ Python f-strings, `nlohmann-json` $\approx$ `import json`, `cpr` $\approx$ `import requests`)*

#### 2. Linking the library in [`CMakeLists.txt`](CMakeLists.txt):
Add two lines to `CMakeLists.txt`:
```cmake
find_package(fmt CONFIG REQUIRED)
target_link_libraries(CppApp PRIVATE fmt::fmt)
```

#### 3. Automatic installation:
When you configure CMake, vcpkg automatically downloads, compiles, and links the libraries:
```powershell
cmake -B build -S . -DCMAKE_TOOLCHAIN_FILE="vcpkg/scripts/buildsystems/vcpkg.cmake"
```
No manual downloads, no DLL path hell.

---

## 4. How to Build and Run the Project

### The Standard 3-Step Process:

#### Step 1: Configure (CMake prepares build files & resolves dependencies)
```powershell
cmake -B build -S . -DCMAKE_TOOLCHAIN_FILE="vcpkg/scripts/buildsystems/vcpkg.cmake"
```

#### Step 2: Build (Compiles `.cpp` files into `.exe`)
```powershell
cmake --build build --config Debug
```
*(Tip: For optimized release builds, pass `--config Release`)*

#### Step 3: Run the executable
```powershell
.\build\Debug\CppApp.exe
```
*(Or `.\build\CppApp.exe` depending on generator)*

---

## 5. Using CMake Presets (Shorthand Commands)

We configured [`CMakePresets.json`](CMakePresets.json), so you don't need to type the long `-DCMAKE_TOOLCHAIN_FILE` flag every time!

```powershell
# Configure using preset
cmake --preset default

# Build using preset
cmake --build --preset default

# Run
.\build\CppApp.exe
```

---

## 6. Recommended VS Code Setup

If you use **Visual Studio Code**:
1. Install extensions:
   - **C/C++** (`ms-vscode.cpptools`)
   - **CMake Tools** (`ms-vscode.cmake-tools`)
2. CMake Tools will automatically detect [`CMakePresets.json`](CMakePresets.json) and [`CMakeLists.txt`](CMakeLists.txt).
3. You can click **Build** and **Debug/Run** (F5 / Shift+F5) directly from the VS Code status bar at the bottom.

