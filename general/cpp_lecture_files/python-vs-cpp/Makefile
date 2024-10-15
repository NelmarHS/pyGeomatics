# Makefile (uses make on linux and the g++ compiler from the terminal)

clean:
	rm -f fib-debug.exe
	rm -f fib-release.exe
	rm -f fib

debug:
	g++ -g -o fib-debug.exe fib.cpp

release:
	g++ -Wall -O3 -o fib-release.exe fib.cpp
