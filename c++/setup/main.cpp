#include <iostream>

int main() {
    std::cout << "=========================================" << std::endl;
    std::cout << "  Hello, World from C++ on Windows!" << std::endl;
    std::cout << "=========================================" << std::endl;

    // Detect C++ standard version at compile time
    std::cout << "Active C++ Standard: ";
    #if defined(_MSVC_LANG)
        #if _MSVC_LANG >= 202302L
            std::cout << "C++23 (MSVC)" << std::endl;
        #elif _MSVC_LANG >= 202002L
            std::cout << "C++20 (MSVC)" << std::endl;
        #elif _MSVC_LANG >= 201703L
            std::cout << "C++17 (MSVC)" << std::endl;
        #elif _MSVC_LANG >= 201402L
            std::cout << "C++14 (MSVC)" << std::endl;
        #else
            std::cout << "C++11 or older (MSVC)" << std::endl;
        #endif
    #elif defined(__cplusplus)
        #if __cplusplus >= 202302L
            std::cout << "C++23" << std::endl;
        #elif __cplusplus >= 202002L
            std::cout << "C++20" << std::endl;
        #elif __cplusplus >= 201703L
            std::cout << "C++17" << std::endl;
        #elif __cplusplus >= 201402L
            std::cout << "C++14" << std::endl;
        #elif __cplusplus >= 201103L
            std::cout << "C++11" << std::endl;
        #else
            std::cout << "Pre-C++11 (__cplusplus: " << __cplusplus << ")" << std::endl;
        #endif
    #endif

    return 0;
}

