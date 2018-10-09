import os
import sys


def get_adj_dict(input_file):
#    input_file = os.path.join(pgr_folder, graph)
#    output_file = os.path.join(output_folder, graph[:-3] + "txt")
#    print input_file
    adj_dict = {}
    v_count = 0
    e_count = 0
    is_head = True
    with open(input_file, "r") as fp:
        for raw_line in fp:
            line_list = (raw_line.strip()).split()
            if is_head:
                v_count = int(line_list[0])
                e_count = int(line_list[1])
                is_head = False
                continue
            src = int(line_list[0])
            dest = int(line_list[1])
            if src not in adj_dict:
                adj_dict[src] = []
            adj_dict[src].append(dest)

    return v_count, e_count, adj_dict


def write_to_file(adj_dict, v_count, e_count, output_file):

    with open(output_file, "w") as fp:
#        fp.write(str(v_count) + " " + str(e_count) + "\n")
        v_list = sorted(adj_dict.keys())
        for src in v_list:
            fp.write(str(src))
            for dest in sorted(adj_dict[src]):
                fp.write(" " + str(dest))
            fp.write("\n")

def main(graph_folder, output_folder):

    pgr_list = os.listdir(graph_folder)
#    print(pgr_list)
    for graph in pgr_list:
        if graph.endswith("txt"):
            input_file = os.path.join(graph_folder, graph)
            output_file = os.path.join(output_folder, graph[:-3] + "txt")
            print input_file

            v_count, e_count, adj_dict = get_adj_dict(input_file)

            print v_count, e_count

            write_to_file(adj_dict, v_count, e_count, output_file)
#            break


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python <pgr_to_edge_list.py> <edge_list_graph_folder> <output_folder>\n")
        exit(-1)

    main(sys.argv[1], sys.argv[2])
