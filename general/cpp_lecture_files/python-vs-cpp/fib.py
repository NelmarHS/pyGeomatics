import time


# the fibonacci function
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    start = time.time()
    for _ in range(50):
        fib(30)
    print(f"Total time spent (py): {(time.time() - start) * 1000:.3f} ms")


main()
