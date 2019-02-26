import os
import sys
import random
import math

def dump_list_to_file(output_list, output_file):

    with open(output_file, "w") as fp:
        for line in output_list:
            fp.write(line + '\n')
    print("File is saved in %s\n" %(output_file))

def main(graph_list_file, output_folder):
    graph_dict = {}
    with open(graph_list_file, "r") as fp:
        for raw_line in fp:
            line = raw_line.strip()
            graph_name = line.split('/')[-1]
            if "g500" in graph_name:
                continue
            scale = int(graph_name.split('_')[3])
            v = int(math.pow(2, scale))
            if v not in graph_dict:
                graph_dict[v] = []
            graph_dict[v].append(line)

    for key in graph_dict:
        output_file = os.path.join(output_folder, "rmat_graph_%s.txt" %(key))
        output_list = graph_dict[key]
        random.shuffle(output_list)

        dump_list_to_file(output_list, output_file)

#        print(key, len(graph_dict[key]))


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python split_vertex_group.py <input_graph_list.file> <output_folder>\n")
        exit(-1)

    main(sys.argv[1], sys.argv[2])


