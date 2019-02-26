#!/usr/bin/
import os
import sys
import random
import math

group = 9
n = 100000
ratio_dict = {5:0.1, 6:0.15, 7:0.25, 8:0.25, 9:0.15, 10:0.1}

for scale, ratio in ratio_dict.iteritems():
    l = int(n * ratio)
    for i in range(l):
        d = 20 * random.random()
        v = int(math.pow(2, scale))
        if d < 4:
            d = 4
        if d > 16:
            d = 16
        e = int(v * d)
        graph_name = "g500_%s_%s_%s_%s.graph" %(group, i, scale, e)
        cmd_1 = "./generator_test_mpi %s %s 1 1" %(scale, int(d))
        os.system(cmd_1)

        input_graph = "scale-%s-rank-0.bin" %(scale)
        cmd_2 = "mv %s g500_graph/%s" %(input_graph, graph_name)
        os.system(cmd_2)


