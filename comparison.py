import time
import clustered_bis
import random_quick_sort
import generate_tc

def setup():
    tc = generate_tc.generate()
    return tc

def count_execution_time(start, end):
    return (end - start) * 1000

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
        print("Execution Time CBIS: {:.6f} milliseconds".format(execution_time))

        # Count Execution Time for Randomize Quick Sort
        start_time = time.time()
        random_quick_sort.randomized_quick_sort_inplace(b_list, 0, len(b_list) - 1)
        end_time = time.time()
        execution_time = count_execution_time(start_time, end_time)
        print("Execution Time RQS: {:.6f} milliseconds".format(execution_time))

        print()

if __name__ == "__main__":
    main()
