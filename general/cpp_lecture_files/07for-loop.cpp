#include<iostream>

int main()
{
    int sum = 0;
    for (unsigned int i=0; i<10; i++)
    {
        for (unsigned int j=0; j<10; j++)
            sum += i + j;   // loop body is 1 line
                            // it is allowed to leave out {}
    }
    std::cout << "sum = " << sum << std::endl;

    return 0;
}
