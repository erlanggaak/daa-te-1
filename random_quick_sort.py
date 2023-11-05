import random
import generate_tc

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Pilih elemen pivot secara acak
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    # Inisialisasi list untuk elemen yang lebih kecil, sama, dan lebih besar dari pivot
    lesser = []
    equal = []
    greater = []

    # Pisahkan elemen-elemen ke dalam tiga list berdasarkan hubungan dengan pivot
    for element in arr:
        if element < pivot:
            lesser.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)

    # Rekursif sorting pada elemen-elemen yang lebih kecil dan lebih besar dari pivot
    sorted_lesser = randomized_quick_sort(lesser)
    sorted_greater = randomized_quick_sort(greater)

    # Gabungkan hasil sorting
    return sorted_lesser + equal + sorted_greater

def randomized_quick_sort_inplace(arr, low, high):
    if low < high:
        # Pilih elemen pivot secara acak
        pivot_index = random.randint(low, high)
        
        # Tukar elemen pivot dengan elemen terakhir
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        
        # Temukan indeks partisi dan urutkan elemen-elemen dalam partisi
        partition_index = partition(arr, low, high)
        
        # Rekursif sorting pada partisi-partisi
        randomized_quick_sort_inplace(arr, low, partition_index - 1)
        randomized_quick_sort_inplace(arr, partition_index + 1, high)

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
    randomized_quick_sort_inplace(a_list, 0, len(a_list) - 1)
    print(a_list)

if __name__ == "__main__":
    main()