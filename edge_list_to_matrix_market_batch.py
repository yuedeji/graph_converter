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


def main(graph_folder, output_folder):

    graph_list = os.listdir(graph_folder)
#    print(pgr_list)
    for graph in graph_list:
        if graph.endswith("txt"):
            input_file = os.path.join(graph_folder, graph)
            output_file = os.path.join(output_folder, graph[:-3] + "txt")
            if os.path.isfile(output_file):
                continue
            print input_file

            edge_to_matrix(input_file, output_file)


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python <edge_list_to_matrix_market.py> <edge_list_graph_folder> <output_folder>\n")
        exit(-1)

    main(sys.argv[1], sys.argv[2])
