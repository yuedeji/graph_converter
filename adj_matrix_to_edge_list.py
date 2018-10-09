import os
import os.path
import sys

def convert(adj_matrix, edge_list):
    try:
        fp_in = open(adj_matrix, "r")
        fp_out = open(edge_list, "w")
        for line in fp_in.readlines():
            one = line.split()
            if len(one) > 1:
                u = int(one[0].strip())
                n = int(one[1].strip())
                for i in range(2, 2 + n):
                    v = int(one[i].strip())
                    fp_out.write(str(u) + " " + str(v) + "\n")

        fp_in.close()
        fp_out.close()

    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "\nUsage: python adj_matrix_to_edge_list.py <adj_matrix.graph> <edge_list.graph>\n"
        exit()
    print len(sys.argv), sys.argv[0], sys.argv[1], sys.argv[2]
    convert(sys.argv[1], sys.argv[2])
    print "Done!\n"

