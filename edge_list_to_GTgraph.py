import os
import sys


def write_gtgraph_head(file_name, v_count, e_count, fp_out):

    fp_out.write("c FILE          : %s\n" %(file_name))
    fp_out.write("c No. of vertices   : %s\n" %(v_count))
    fp_out.write("c No. of directed edges : %s\n" %(e_count))
    fp_out.write("c Max. weight       : 1\n")
    fp_out.write("c Min. weight       : 1\n")
    fp_out.write("c A directed arc from u to v of weight w\n")
    fp_out.write("c is represented below as ' a  u  v  w '\n")
    fp_out.write("p sp %s %s\n" %(v_count, e_count))


def edge_to_gtgraph(input_file, output_file):

    fp_out = open(output_file, 'w')

    is_head = True
    with open(input_file, 'r') as fp:
        for raw_line in fp:
            line_list = raw_line.strip().split()
            if is_head:
                v_count = line_list[0]
                e_count = line_list[1]
                is_head = False
                write_gtgraph_head(output_file.strip().split('/')[-1], v_count, e_count, fp_out)
            else:
                fp_out.write('a %s %s 1\n' %(int(line_list[0]), int(line_list[1])))

    fp_out.close()

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python <edge_list_to_GTgraph.py> <edge_list_file> <output_file>\n")
        exit(-1)

    edge_to_gtgraph(sys.argv[1], sys.argv[2])
