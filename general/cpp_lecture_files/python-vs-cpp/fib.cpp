#include <chrono>
#include <iostream>

// the fibonacci function
unsigned long int fib(unsigned long int n) 
{
    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return 0;
    } else {
        return fib(n - 1) + fib(n - 2);
    }
}

// the starting point of the program
int main() 
{
    auto t_start = std::chrono::high_resolution_clock::now();
    for (unsigned long int i = 0; i < 50; ++i) 
    {
        fib(30); // call fib function
    }
    auto t_end = std::chrono::high_resolution_clock::now();

    double elapsed_time_ms = std::chrono::duration<double, std::milli>(t_end-t_start).count();
    std::cout << "Total time spent (c++): " << elapsed_time_ms << "ms" << std::endl;

    return 0;
}

