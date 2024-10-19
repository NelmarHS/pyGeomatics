"""This script automatically runs the nbody.py, nbody.exe (debug) and nbody.exe (release). In order for this script
to work, the nbody.cpp must first be manually ran in debug and release mode (at any iteration number)"""
import subprocess # as per footnote in chapter 14.8, using subprocess module
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt



# path locations of the files and the iteration settings
cpp_debug = "cmake-build-debug/nbody.exe"
cpp_release = "cmake-build-release/nbody.exe"
python = "nbody.py"
file_name_benchmark = "benchmark_results.csv"
iteration_steps = 3 # fill in the amount of iteration steps must be done
iteration_base = 500 # fill in the base iteration number (consequent iteration steps are multiplied by 10)
N = []
for i in range(iteration_steps):
    N.append(iteration_base * (10 ** i))



def run_command(command, workdir):
    """saves the start_time, then runs the subprocess, then saves the end_time, returns the difference i.e. exec_time
    """
    start_time = time.perf_counter()
    # The work directory is added to ensure that the cpp_output.csv is put in the main directory (where runtime.py is
    # located) and not in folder back (parent folder). This is necessary because of the solution in nbody.cpp that ensures
    # placement of the output folder in the main folder (nbody.cpp line 249)
    subprocess.run(command, cwd=workdir)
    end_time = time.perf_counter()
    return end_time - start_time


def benchmark_cpp_debug(file, workdir):
    results_cpp_debug = []
    for iteration in N:
        command = f".\{file} {iteration}" # terminal command to run the file
        exec_time = run_command(command, workdir)
        results_cpp_debug.append((f"C++ (debug)", iteration, exec_time))
    return results_cpp_debug

def benchmark_cpp_release(file, workdir):
    results_cpp_release = []
    for iteration in N:
        command = f".\{file} {iteration}" # terminal command to run the file
        exec_time = run_command(command, workdir)
        results_cpp_release.append((f"C++ (release)", iteration, exec_time))
    return results_cpp_release


def benchmark_python(file, workdir):
    results_python = []
    for iterations in N:
        command = f"py {file} {iterations}" # terminal command to run the file
        exec_time = run_command(command, workdir)
        results_python.append(("Python", iterations, exec_time))
    return results_python

def write_to_csv(file, results_all):
    with open(file, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Language", "iteration", "exec time"])

        total_time = 0
        for i in results_all:
            writer.writerow([i[0], i[1], i[2]])
            total_time += i[2]

        # last row displays total runtime
        writer.writerow([f"Total runtime = {total_time}"])


def csv_to_graph(file_name_benchmark, iteration_steps, N):
    df = pd.read_csv(file_name_benchmark, sep=';')

    # creating sublists that contain the time values for the different programs
    cpp_debug_times, cpp_release_times , python_times = [], [], []
    for i in range(len(N)):
        cpp_debug_times.append(df.iloc[i, 2])
        cpp_release_times.append(df.iloc[i + iteration_steps, 2])
        python_times.append(df.iloc[i + iteration_steps * 2, 2])

    # graphing on log scale
    plt.plot(N, cpp_debug_times, label='C++ debug')
    plt.plot(N, cpp_release_times, label='C++ release')
    plt.plot(N, python_times, label='Python')
    plt.xlabel('Iteration size')
    plt.ylabel('runtime (sec)')
    plt.xscale('log')
    plt.xticks(N, labels=[str(iteration) for iteration in N])
    plt.title('C++ debug, C++ release and Python runtimes')
    plt.legend()
    plt.grid(True)
    plt.show()



# function calls to run the benchmarks
if __name__ == "__main__":
    cpp_debug_results = benchmark_cpp_debug(cpp_debug, workdir="cmake-build-debug")
    cpp_release_results = benchmark_cpp_release(cpp_release, workdir="cmake-build-release")
    python_results = benchmark_python(python, workdir=None)
    results_all = cpp_debug_results + cpp_release_results + python_results
    write_to_csv(file_name_benchmark, results_all)
    csv_to_graph(file_name_benchmark, iteration_steps, N)




