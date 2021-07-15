import os
import sys
from sets import Set


def get_undirected_edge_list(input_file):

    undirected_edge_list = []
    edge_set = Set()
    is_head = True
    n = 0
    m = 0
    index = 0
    with open(input_file, 'r') as fp:
        for raw_line in fp:
            line_list = raw_line.strip().split()
            if is_head:
                n = int(line_list[0])
                m = int(line_list[1])
                is_head = False
            else:
                u = int(line_list[0])
                v = int(line_list[1])

                if (u, v) not in edge_set:
                    undirected_edge_list.append((u, v))
                    edge_set.add((u, v))

                if (v, u) not in edge_set:
                    undirected_edge_list.append((v, u))
                    edge_set.add((v, u))
            index += 1
            if index % 1000000 == 0:
                print index

    return undirected_edge_list, n

def dump_undirected_edge_list_to_file(undirected_edge_list, n, output_file):
    with open(output_file, "w") as fp:
        fp.write('%{} {}\n'.format(n, len(undirected_edge_list)))
        for one in sorted(undirected_edge_list):
            fp.write('{} {}\n'.format(one[0], one[1]))

    print("new edge list is saved to {}".format(output_file))

def directed_to_undirected(input_file, output_file):

    undirected_edge_list, n = get_undirected_edge_list(input_file)

    dump_undirected_edge_list_to_file(undirected_edge_list, n, output_file)

#    fp_out = open(output_file, 'w')
#    is_head = True
#    with open(input_file, 'r') as fp:
#        for raw_line in fp:
#            line_list = raw_line.strip().split()
#            if is_head:
#                fp_out.write('%s %s %s\n' %(line_list[0], line_list[0], line_list[1]))
#                is_head = False
#            else:
#                fp_out.write('%s %s\n' %(int(line_list[0]) + 1, int(line_list[1]) + 1))
#    fp_out.close()

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python <directed_edge_list_to_undirected.py> <edge_list_file> <output_file>\n")
        exit(-1)

    directed_to_undirected(sys.argv[1], sys.argv[2])

