import csv
import sys
import os
import struct
import time

chunk_size = 8
def rmat_bin_to_edge_list(input_file, output_file):
    index = 0
    edge_list = []
    fp_out = open(output_file, "w")
    with open(input_file, "rb") as fp:
        while True:
            chunk = fp.read(chunk_size)
            if chunk:
                v = struct.unpack('l', chunk)[0]
            else:
                break
            edge_list.append(v)
            if index % 2 == 1:
                fp_out.write(str(edge_list[0]) + ' ' + str(edge_list[1]) + '\n')
                edge_list = []
            index += 1
    print index
    fp_out.close()

def main(input_folder, output_folder):

    file_list = os.listdir(input_folder)

    for input_file in file_list:
        if input_file.endswith("graph"):
            input_path = os.path.join(input_folder, input_file)
            output_path = os.path.join(output_folder, input_file)
            rmat_bin_to_edge_list(input_path, output_path)

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Usage: python <rmat_bin_to_edge_list.py> <input_folder> <output_folder>\n")
        exit(-1)
    main(sys.argv[1], sys.argv[2])

#    time_begin = time.time()
#    rmat_bin_to_edge_list("rmat_graph/rmat_4_128.graph", "test.txt")
#    time_end = time.time()
#    print "time (s), %s" %(time_end - time_begin)


