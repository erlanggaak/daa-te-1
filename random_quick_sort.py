import random
import generate_tc

def randomized_quick_sort(arr, low, high):
    if low < high:
        # Pilih elemen pivot secara acak
        pivot_index = random.randint(low, high)
        
        # Tukar elemen pivot dengan elemen terakhir
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        
        # Temukan indeks partisi dan urutkan elemen-elemen dalam partisi
        partition_index = partition(arr, low, high)
        
        # Rekursif sorting pada partisi-partisi
        randomized_quick_sort(arr, low, partition_index - 1)
        randomized_quick_sort(arr, partition_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def main():
    # Contoh penggunaan
    a_list = generate_tc.generate_random(20)
    print(a_list)
    randomized_quick_sort(a_list, 0, len(a_list) - 1)
    print(a_list)

if __name__ == "__main__":
    main()