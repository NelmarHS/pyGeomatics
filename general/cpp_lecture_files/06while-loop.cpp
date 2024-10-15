#include<iostream>

int main()
{
    int n = 0;
    while (n < 5) {
        n++; // run body as long as condition evaluates to true
        std::cout << "inside first while " << n << std::endl;
    }
    std::cout << n << std::endl;

    n = 0;
    do {
        n++; // run body (at least) once (depending on condition)
        std::cout << "inside second while " << n << std::endl;
    } while (n < 0);
    std::cout << n << std::endl;

    return 0;
}
