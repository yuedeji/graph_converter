import os
import sys


def edge_to_matrix(input_file, output_file):

    fp_out = open(output_file, 'w')

    is_head = True
    with open(input_file, 'r') as fp:
        for raw_line in fp:
            line_list = raw_line.strip().split()
            if is_head:
                fp_out.write('%s %s %s\n' %(line_list[0], line_list[0], line_list[1]))
                is_head = False
            else:
                fp_out.write('%s %s\n' %(int(line_list[0]) + 1, int(line_list[1]) + 1))

    fp_out.close()

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python <edge_list_to_matrix_market.py> <edge_list_file> <output_file>\n")
        exit(-1)

    edge_to_matrix(sys.argv[1], sys.argv[2])
