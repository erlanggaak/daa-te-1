import time
import clustered_bis
import random_quick_sort
import generate_tc
from memory_profiler import profile

def setup():
    tc = generate_tc.generate()
    return tc

def count_execution_time(start, end):
    return (end - start) * 1000

@profile
def main():
    for name, values in setup().items():
        a_list = values.copy()
        b_list = values.copy()

        print(name, ':')

        # Count Execution Time for Clustered Binary Insertion Sort
        start_time = time.time()
        clustered_bis.clustered_binary_insertion_sort(a_list) 
        end_time = time.time()
        execution_time = count_execution_time(start_time, end_time)
        print("Execution Time CBIS: {:.4f} ms".format(execution_time))

        # Count Execution Time for Randomize Quick Sort
        start_time = time.time()
        random_quick_sort.randomized_quick_sort(b_list, 0, len(b_list) - 1)
        end_time = time.time()
        execution_time = count_execution_time(start_time, end_time)
        print("Execution Time RQS: {:.4f} ms".format(execution_time))

        print()

def execute_cbis(array, title):
    print(f'{title}: ')

    # Count Execution Time for Clustered Binary Insertion Sort
    start_time = time.time()
    clustered_bis.clustered_binary_insertion_sort(array) 
    end_time = time.time()
    execution_time = count_execution_time(start_time, end_time)
    print("Execution Time CBIS: {:.4f} ms".format(execution_time))

def execute_rqs(array):
    # Count Execution Time for Randomize Quick Sort
    start_time = time.time()
    random_quick_sort.randomized_quick_sort(array, 0, len(array) - 1)
    end_time = time.time()
    execution_time = count_execution_time(start_time, end_time)
    print("Execution Time RQS: {:.4f} ms".format(execution_time))
    print()

def main2():
    sorted_kecil = generate_tc.generate_sorted(200)
    sorted_sedang = generate_tc.generate_sorted(2000)
    sorted_besar = generate_tc.generate_sorted(20000)
    random_kecil = generate_tc.generate_random(200)
    random_sedang = generate_tc.generate_random(2000)
    random_besar = generate_tc.generate_random(20000)
    reversed_kecil = generate_tc.generate_reversed(200)
    reversed_sedang = generate_tc.generate_reversed(2000)
    reversed_besar = generate_tc.generate_reversed(20000)

    execute_cbis(sorted_kecil.copy(), 'Sorted Kecil')
    execute_rqs(sorted_kecil.copy())

    execute_cbis(sorted_sedang.copy(), 'Sorted Sedang')
    execute_rqs(sorted_sedang.copy())
    
    execute_cbis(sorted_besar.copy(), 'Sorted Besar')
    execute_rqs(sorted_besar.copy())

    execute_cbis(random_kecil.copy(), 'Random Kecil')
    execute_rqs(random_kecil.copy())

    execute_cbis(random_sedang.copy(), 'Random Sedang')
    execute_rqs(random_sedang.copy())

    execute_cbis(random_besar.copy(), 'Random Besar')
    execute_rqs(random_besar.copy())

    execute_cbis(reversed_kecil.copy(), 'Reversed Kecil')
    execute_rqs(reversed_kecil.copy())

    execute_cbis(reversed_sedang.copy(), 'Reversed Sedang')
    execute_rqs(reversed_sedang.copy())

    execute_cbis(reversed_besar.copy(), 'Reversed Besar')
    execute_rqs(reversed_besar.copy())

if __name__ == "__main__":
    main2()
