import os
import sys
import csv

import networkx as nx
from numpy import array
import random

def get_stat(graph_label):

    graph_stat = {}

    for gid in graph_label:
        graph = graph_label[gid]
        v = len(graph)

        if v not in graph_stat:
            graph_stat[v] = 0
        graph_stat[v] += 1

    return graph_stat

def convert_one(file_graph, file_label, stat_file):

#    graph_label_list = get_graph_label_matrix(file_graph_label)
#    graph_adj_dict = get_graph_adj_dict(file_graph)
    graph_label = get_graph_label_dict(file_label)

    graph_stat = get_stat(graph_label)

    with open(stat_file, "w") as fp:
        for graph_size in graph_stat:
            fp.write(str(graph_size) + ',' + str(graph_stat[graph_size]) + '\n')

    #print graph_stat

#    print graph_label
#    return graph_matrix, graph_label_list

def get_k(graph_adj, graph_label_dict):
    '''all the graphs are modified to |V|/|G| size'''
    graph_size = []
    for g_i, g_vertices in graph_label_dict.iteritems():
        graph_size.append(len(g_vertices))
    graph_size_sort = sorted(graph_size)
    return graph_size_sort[int(len(graph_size) * 0.8)]
#    num_graph = len(graph_label_dict)
#    v = len(graph_adj)
#    avg_graph_size = v / num_graph
#    print num_graph, v, avg_graph_size

def get_batch_matrix(data_test, label_test, batch_size):
    data_batch = []
    label_batch = []

    data_batch_one = []
    label_batch_one = []
    for i in xrange(len(data_test)):
        if i != 0 and i % batch_size == 0:
            data_batch.append(array(data_batch_one))
            label_batch.append(array(label_batch_one))
            data_batch_one = []
            label_batch_one = []
        data_batch_one.append(data_test[i])
        label_batch_one.append(label_test[i])

    if len(data_batch_one) > 0:
        data_batch.append(array(data_batch_one))
        label_batch.append(array(label_batch_one))
        data_batch_one = []
        label_batch_one = []
    return data_batch, label_batch

def get_bc_k_matrix(graph_adj, graph_label_dict, k):

    graph_matrix = []
    for g_id, g_vertices in graph_label_dict.iteritems():
#        print g_id, g_vertices
        row_list = []
        if len(g_vertices) > k:
            row_list = get_bc_k(graph_adj, g_vertices, k)
        elif len(g_vertices) < k:
            row_list = add_vertex(graph_adj, g_vertices, k)
        else:
            row_list = equal_transfer(graph_adj, g_vertices)
        graph_matrix.append(row_list)
#        print len(row_list)
    return graph_matrix

def get_bc_k(graph_adj, g_vertices, k):

    nx_graph = nx.DiGraph()
    for i in g_vertices:
        nx_graph.add_node(i)
        for j in graph_adj[i]:
            nx_graph.add_edge(i, j)
    bc_dict = nx.betweenness_centrality(nx_graph)
#    print bc_dict
    bc_list = sorted([(value, key) for (key, value) in bc_dict.items()]) # [(value, key)]
    v_list = []

    for i in xrange(k):
        v_list.append(bc_list[i][1])
#    print v_list
#    print sorted(bc_dict.values(), reverse = True)
#    print nx_graph.edges(), len(nx_graph.nodes())

#    v_list = random.sample(g_vertices, k)
    return equal_transfer(graph_adj, v_list)

def get_average_graph_matrix(graph_adj, graph_label_dict, k):
    '''all the graphs are modified to |V|/|G| size'''
#    num_graph = len(graph_label_dict)
#    v = len(graph_adj)
#    avg_graph_size = v / num_graph
#    print num_graph, v, avg_graph_size

    graph_matrix = []
    for g_id, g_vertices in graph_label_dict.iteritems():
#        print g_id, g_vertices
        row_list = []
        if len(g_vertices) > k:
            row_list = get_random_k(graph_adj, g_vertices, k)
        elif len(g_vertices) < k:
            row_list = add_vertex(graph_adj, g_vertices, k)
        else:
            row_list = equal_transfer(graph_adj, g_vertices)
        graph_matrix.append(row_list)
#        print len(row_list)
    return graph_matrix


def get_random_k(graph_adj, g_vertices, k):

    v_list = random.sample(g_vertices, k)
    return equal_transfer(graph_adj, v_list)


def add_vertex(graph_adj, g_vertices, k):
    #print "add dummy vertex"

    row_list = []
    for u in g_vertices:
        for v in g_vertices:
            if v in graph_adj[u]:
                row_list.append(1)
            else:
                row_list.append(0)
        for i in xrange(k - len(g_vertices)):
            row_list.append(0)
    for i in xrange(k - len(g_vertices)):
        for j in xrange(k):
            row_list.append(0)

    return row_list

def equal_transfer(graph_adj, g_vertices):

    row_list = []

    for u in g_vertices:
        for v in g_vertices:
            if v in graph_adj[u]:
                row_list.append(1)
            else:
                row_list.append(0)
    return row_list

def get_graph_adj_dict(file_graph):
    graph_adj = {}
    fp_graph = csv.reader(open(file_graph))
    max_v = 0
    for line in fp_graph:
        u = int(line[0])
        v = int(line[1].strip())
        if u not in graph_adj:
            graph_adj[u] = []
        graph_adj[u].append(v)
        if u > max_v:
            max_v = u
        if v > max_v:
            max_v = v
# add the vertices which are not in edge_list
    for i in xrange(max_v + 1):
        if i > 0 and i not in graph_adj:
            graph_adj[i] = []
    return graph_adj

def get_graph_label_dict(file_label):
    fp_label = open(file_label, "r")
    graph_label = {}
    index = 1
    for line in fp_label.readlines():
        g_index = int(line)
        if g_index not in graph_label:
            graph_label[g_index] = []
        graph_label[g_index].append(index)
        index += 1
    fp_label.close()
    return graph_label

def get_graph_label_matrix(file_graph_label):
    '''Given a graph label list, return a |G| * |L| matrix, |G| stands for number of graphs, |L| stands for number of labels'''
    graph_label_dict = {}
    fp_graph_label = open(file_graph_label, "r")
    for line in fp_graph_label.readlines():
#        graph_label_list.append(int(line))
        if int(line) not in graph_label_dict:
            graph_label_dict[int(line)] = 0
        graph_label_dict[int(line)] += 1
#    print graph_label_dict
    fp_graph_label.close()
    print graph_label_dict

#    graph_label_list = []
#    fp_graph_label = open(file_graph_label, "r")
#    label_order_list = sorted(graph_label_dict.iterkeys())
#    for line in fp_graph_label.readlines():
#        cur_label = int(line)
#        row_list = []
#        for i in label_order_list:
#            if cur_label == i:
#                row_list.append(1)
#            else:
#                row_list.append(0)
#        graph_label_list.append(row_list)
#    return graph_label_list

def graph_to_matrix_enlarge(graph_adj, graph_label):
    graph_matrix = []

# enlarge graph
    length = 0
    for g_i in graph_label:
        if len(graph_label[g_i]) > length:
            length = len(graph_label[g_i])

    for g_i in graph_label:
        row_graph = []
        graph = graph_label[g_i]
        for row_id in xrange(len(graph)):
            u = graph[row_id] # src vertex
            for col_id in xrange(len(graph)):
                v = graph[col_id] # dest vertex
#                print u, v
                if v in graph_adj[u]:
                    row_graph.append(1)
                else:
                    row_graph.append(0)
        # enlarge each row to have length vertex
            for col_id in xrange(length - len(graph)):
                row_graph.append(0)
        # enlarge row number to length
        for row_id in xrange(length - len(graph)):
            for col_id in xrange(length):
                row_graph.append(0)

        graph_matrix.append(row_graph)

    return graph_matrix

usage = "Usage: python <graph_converter.py> <input_graph> <graph_indictor> <graph_stat.csv>"
description = "Description: given an input_graph (edge list format, 'src_id, dest_id'), the converter will create the files needed for classical CNN"
if __name__ == "__main__":

    print description
    if len(sys.argv) != 4:
        print "Wrong paramters!"
        print usage
        print "\n"
        exit(-1)
    else:
        convert_one(sys.argv[1], sys.argv[2], sys.argv[3])

        print "Done!\n"

