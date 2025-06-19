import sys
import xxhash
import os

def delete_txt_files():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for fname in os.listdir(current_dir):
        if fname.endswith(".txt") and fname[0].isdigit():  
            try:
                os.remove(os.path.join(current_dir, fname))
            except Exception as e:
                print(f"Couldn't delete {fname}: {e}")
                
delete_txt_files()

try:
    n = int(sys.argv[1])
    s = int(sys.argv[2])
    
    if n <= 0 or s<= 0: 
        print("how does this make sense hah?\nplease enter positive integers")
        exit()
    
except ValueError as e:
    print("please enter valid integers.")
    exit()

bucket_sizes = {i: 0 for i in range(1, n+1)}
overflow_sizeS = {}  # key = (bucket, overflow_index)

try:
    while 1:
        string = input("Please enter the string: ")
        string_size = len(string) + 1    # counting coma
    
        while len(string) > s or not string:
            string = input("please enter another string inside the bounds: ")
            string_size = len(string) + 1   
        
        hash_val = xxhash.xxh64(string).intdigest()
        key = (hash_val % n) + 1
    
        if bucket_sizes[key] + string_size <= s:
            with open(f"{key}.txt","a") as file:
                file.write(f'{string},')
            bucket_sizes[key] += string_size
            print(f"{string} added to {key}.txt")
        elif bucket_sizes[key] + len(string) <= s:
            with open(f"{key}.txt","a") as file:
                file.write(f'{string}')
            bucket_sizes[key] += string_size
            print(f"{string} added to {key}.txt")
        else: 
            overflow_index = 1
        
            while 1:
                overflow_key = (key, overflow_index)
            
                if overflow_key not in overflow_sizeS:
                    overflow_sizeS[overflow_key] = 0
                
                if overflow_sizeS[overflow_key] + string_size <= s:
                    with open(f"{key}_{overflow_index}.txt","a") as file:
                        file.write(f'{string},')
                    overflow_sizeS[overflow_key] += string_size
                    print(f'{string} added to {key}_{overflow_index}.txt')
                    break
                elif overflow_sizeS[overflow_key] + len(string) <= s:
                    with open(f"{key}_{overflow_index}.txt","a") as file:
                        file.write(f'{string}')
                    overflow_sizeS[overflow_key] += string_size
                    print(f'{string} added to {key}_{overflow_index}.txt')
                    break
                else:
                    overflow_index +=1    
except KeyboardInterrupt as e:
    print("program stopped by user.")