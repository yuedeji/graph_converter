import os
import sys


def get_edge_dict(input_file):
#    input_file = os.path.join(pgr_folder, graph)
#    output_file = os.path.join(output_folder, graph[:-3] + "txt")
#    print input_file
    edge_dict = {}
    v_count = 0
    e_count = 0
    v_start = False
    e_start = False
    with open(input_file, "r") as fp:
        for raw_line in fp:
            line = raw_line.strip()
            if line == "#vertices":
                v_start = True
            elif line == "#edges":
                v_start = False
                e_start = True
            else:
                if v_start:
                    v_count += 1
                elif e_start:
                    e_count += 1
                    line_list = line.split()
                    src_v = int(line_list[1])
                    dest_v = int(line_list[3])

                    if src_v not in edge_dict:
                        edge_dict[src_v] = []
                    edge_dict[src_v].append(dest_v)

#                    if is_reverse:
#                        if dest_v not in edge_dict:
#                            edge_dict[dest_v] = []
#                        edge_dict[dest_v].append(src_v)

    return v_count, e_count, edge_dict


def reverse_edge(edge_dict):
    v_list = edge_dict.keys()
    for src_v in v_list:
        for dest in edge_dict[src_v]:
            if dest not in edge_dict:
                edge_dict[dest] = []
# using set() if it is slow
            if src_v not in edge_dict[dest]:
                edge_dict[dest].append(src_v)

def write_to_file(edge_dict, v_count, e_count, output_file):

    with open(output_file, "w") as fp:
        fp.write(str(v_count) + " " + str(e_count) + "\n")
        v_list = sorted(edge_dict.keys())
        for src in v_list:
            for dest in sorted(edge_dict[src]):
                fp.write(str(src) + " " + str(dest) + "\n")


def main(pgr_folder, output_folder, is_reverse):

    pgr_list = os.listdir(pgr_folder)
#    print(pgr_list)
    for graph in pgr_list:
        if graph.endswith("pgr"):
            input_file = os.path.join(pgr_folder, graph)
            output_file = os.path.join(output_folder, graph[:-3] + "txt")
            if os.path.isfile(output_file):
                continue
            print input_file

            v_count, e_count, edge_dict = get_edge_dict(input_file)

            print v_count, e_count
            if is_reverse:
                reverse_edge(edge_dict)
                e_count = 0
                for src in edge_dict:
                    e_count += len(edge_dict[src])
            print e_count

            write_to_file(edge_dict, v_count, e_count, output_file)


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python <pgr_to_edge_list.py> <pgr_graph_folder> <output_folder> <reverse edge? 0 for not, 1 for reverse>\n")
        exit(-1)

    main(sys.argv[1], sys.argv[2], int(sys.argv[3]))
