import os
import sys


def remove_size_zero(input_folder):
    num_zero_file = 0
    for file_one in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_one)
        file_size = os.path.getsize(file_path)
        if file_size < 1:
            os.remove(file_path)
            num_zero_file += 1
    print("removed zero size file, %s" %(num_zero_file))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python graph_remove_size_zero.py input_folder\n")
        exit(-1)
    remove_size_zero(sys.argv[1])

