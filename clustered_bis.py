import generate_tc

def clustered_binary_insertion_sort(a_list):
    POP = 0 # position pointer
    for i in range(1, len(a_list)):
        COP = i
        key = a_list[COP]
        if key >= a_list[POP]:
            place = binary_loc_finder(a_list, POP+1, COP-1, key)
        else:
            place = binary_loc_finder(a_list, 0, POP-1, key)
        
        POP = place # POP is updated
        a_list = place_inserter(a_list, place, COP) # Insert COP in sorted list

def binary_loc_finder(a_list, start, end, key):
    if start == end:
        if a_list[start] > key:
            loc = start
            return loc
        else:
            loc = start + 1
            return loc

    if start > end:
        loc = start
        return loc
    else:
        middle = (start + end) // 2

        if a_list[middle] < key:
            return binary_loc_finder(a_list, middle + 1, end, key)
        elif a_list[middle] > key:
            return binary_loc_finder(a_list, start, middle - 1, key)
        else:
            return middle

def place_inserter(a_list, start, end):
    temp = a_list[end]
    for k in range(end, start, -1):
        a_list[k] = a_list[k-1]
    a_list[start] = temp
    return a_list

def main():
    # Contoh penggunaan
    a_list = generate_tc.generate_random(20)
    print(a_list)
    clustered_binary_insertion_sort(a_list)
    print(a_list)

if __name__ == "__main__":
    main()