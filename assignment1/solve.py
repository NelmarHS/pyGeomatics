# GEO1000 - Assignment 1
# Authors: Daan Noordam & Joost de Witte
# Studentnumbers: 5148766 & 5656176
from math import sqrt


# function to determine the roots of input values a, b and c
def abc(a, b, c):
    d_value = discriminant(a, b, c)

    # determine roots when a solution exists, otherwise; pass
    try:
        root_x1 = (- b + sqrt(d_value)) / (2 * a)
        root_x2 = (- b - sqrt(d_value)) / (2 * a)
    except ValueError:
        pass

    # determine category of the solution and print results
    if d_value < 0:
        print(f"The roots of {a} x^2 + {b} x + {c} are: \n x = Not real")
    elif d_value == 0:
        print(f"The roots of {a} x^2 + {b} x + {c} are: \n x = {root_x1}")
    elif d_value > 0:
        print(f"The roots of {a} x^2 + {b} x + {c} are: \n x = {root_x1}, {root_x2}")


# function to determine the discriminant value
def discriminant(a, b, c):
    d_value = b ** 2 - 4 * a * c
    return d_value


abc(2.0, 0.0, 0.0)
abc(1.0, 3.0, 2.0)
abc(3.0, 4.5, 9.0)
