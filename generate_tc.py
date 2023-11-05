import random
import os

def generate_sorted(n):
    data = []
    for i in range(n):
        data.append(i+1)
    return data

def generate_random(n):
    data = generate_sorted(n)
    random.shuffle(data)
    return data

def generate_reversed(n):
    data = []
    for i in range(n, 0, -1):
        data.append(i)
    return data

def generate_cases():
    # Generate the testcases
    tc = {
        'sorted_kecil' : generate_sorted(200),
        'sorted_sedang' : generate_sorted(2000),
        'sorted_besar' : generate_sorted(20000),
        'random_kecil' : generate_random(200),
        'random_sedang' : generate_random(2000),
        'random_besar' : generate_random(20000),
        'reversed_kecil' : generate_reversed(200),
        'reversed_sedang' : generate_reversed(2000),
        'reversed_besar' : generate_reversed(20000),
    }
    return tc

def generate():
    # Generate the testcases
    tc = generate_cases()

    # Create the directory if it doesn't exist
    TC_DIR = './cases/'

    if not os.path.exists(TC_DIR):
        os.makedirs(TC_DIR)

    # Save the testcases to files
    for name, testcase in tc.items():
        file_path = TC_DIR + str(name) + '.in'
        with open(file_path, 'w') as file_input:
            for num in testcase:
                file_input.write(str(num) + '\n')

    return tc