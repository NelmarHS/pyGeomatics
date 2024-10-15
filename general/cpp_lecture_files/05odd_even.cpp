#include<iostream>

int main() {
    int a;

    std::cout << "Give a number >";
    std::cin >> a;
    std::cout << "You entered " << a << " which is ";
    if (a % 2 == 0)
    {
        std::cout << "even";
    }
    else
    {
        std::cout << "odd";
    }
    std::cout << std::endl;
    return 0;
}
