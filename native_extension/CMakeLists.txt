cmake_minimum_required(VERSION 3.14)
project(native_extension)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Find Python
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

# Add pybind11 as a subdirectory
add_subdirectory(pybind11)

pybind11_add_module(native_extension MODULE native_extension.cpp)
