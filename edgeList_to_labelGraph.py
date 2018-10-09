import os
import os.path
import sys

def convert(edge_list, label_graph):
    try:
        fp_in = open(edge_list, "r")
        line_num = 0
        v_set = set()
        for line in fp_in.readlines():
            one = line.split()
            if len(one) > 1:
                u = int(one[0].strip())
                v = int(one[1].strip())
                if u not in v_set:
                    v_set.add(u)
                if v not in v_set:
                    v_set.add(v)

            if line_num < 10:
                print v_set
                print sorted(v_set)
            line_num += 1
        fp_in.close()

        print "v_count, " + str(len(v_set)) + "\ne_count, " + str(line_num)

        fp_out = open(label_graph, "w")
        fp_out.write("t # 0\n")
        for one in sorted(v_set):
            fp_out.write("v "+str(one)+" 0\n")

        fp_in = open(edge_list, "r")
        for line in fp_in.readlines():
            one = line.split()
            if len(one) > 1:
                u = int(one[0].strip())
                v = int(one[1].strip())
                fp_out.write("e "+ str(u) + " " + str(v) + " 0\n")

        fp_in.close()
        fp_out.close()

    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "\nUsage: python edgeList_to_labelGraph <edge_list.graph> <label_graph.graph>\n"
        exit()
    print len(sys.argv), sys.argv[0], sys.argv[1], sys.argv[2]
    convert(sys.argv[1], sys.argv[2])
    print "Done!\n"

