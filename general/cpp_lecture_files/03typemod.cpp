#include<iostream>

int main() {
    // variable 'my_short' can hold value between 0 and 65,535
    // it will occupy 2 bytes of main memory
    unsigned short int my_short = 65534;

    // variable 'really_large' can hold large, but only positive numbers
    unsigned long long int really_large; // max = 18446744073709551615

    std::cout << "Input a number > ";
    std::cin >> really_large;
    std::cout << "You gave: " << really_large;
}
