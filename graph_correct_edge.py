import os
import sys
import math

def main(input_folder):

    num_corrected = 0
    for file_one in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_one)

        name_list = file_one.split('_')
        scale = int(name_list[-2])
        v = int(math.pow(2, scale))
        e = int(name_list[-1].split('.')[0])

        d = int(e / v)
        e_corrected = v * d
        if e == e_corrected:
            continue
        num_corrected += 1
        output_name = name_list[0] + '_' + name_list[1] + '_' + name_list[2] + '_' + name_list[3] + '_' + str(e_corrected) + '.graph'

        cmd = "mv %s %s" %(file_path, os.path.join(input_folder, output_name))
        os.system(cmd)
    print "num_corrected = %s" %(num_corrected)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python graph_remove_size_zero.py input_folder\n")
        exit(-1)
    main(sys.argv[1])

