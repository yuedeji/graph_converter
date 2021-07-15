import os
import sys

def dump_dict_to_file(edge_dict, output_file):

    fp = open(output_file, "w")
    for i in sorted(edge_dict.keys()):
        for j in sorted(edge_dict[i]):
            fp.write(str(i) + ' ' + str(j) + '\n')
    fp.close()


def main(input_folder, output_folder):
    for file_one in os.listdir(input_folder):
        if not file_one.endswith("txt"):
            continue
        file_path = os.path.join(input_folder, file_one)
        output_file = os.path.join(output_folder, file_one)

        edge_dict = {}
        with open(file_path, "r") as fp:
            for raw_line in fp:
                line = raw_line.strip()
                src = int(line.split(' ')[0])
                dest = int(line.split(' ')[1])
                if src not in edge_dict:
                    edge_dict[src] = []
                edge_dict[src].append(dest)
        dump_dict_to_file(edge_dict, output_file)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python unsorted_edgelist_to_sorted.py input_folder output_folder\n")
        exit(-1)
    main(sys.argv[1], sys.argv[2])

