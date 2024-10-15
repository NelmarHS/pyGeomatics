#include<iostream>

int main() {
    int a, b, c, d;

    // pre increment -- first increment, and assign result to b
    a = 2;
    b = ++a;
    std::cout << "a: " << a << std::endl; // a = 3
    std::cout << "b: " << b << std::endl; // b = 3

    // post increment -- first assign to d, then increment
    c = 2;
    d = c++;
    std::cout << "c: " << c << std::endl; // c = 3
    std::cout << "d: " << d << std::endl; // d = 2

}
