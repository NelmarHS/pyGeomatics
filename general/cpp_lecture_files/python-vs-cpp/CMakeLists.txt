# running the following creates a debug and release build
# each in their own folder

# cd debug
# cmake -DCMAKE_BUILD_TYPE=Debug ..
# cmake --build .
# cd ../release
# cmake -DCMAKE_BUILD_TYPE=Release ..
# cmake --build .

cmake_minimum_required(VERSION 3.22)

project(fib)

set(CMAKE_CXX_STANDARD 17)

add_executable(fib fib.cpp)
