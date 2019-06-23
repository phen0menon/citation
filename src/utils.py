from collections import defaultdict

import numpy as np
from numpy import random


def parse_file(filename):
    fstream = open(filename, "r")

    parsed_data = defaultdict(list)

    for line in fstream:
        articles = line.split()
        articles_list = list(map(int, articles))

        article_vertex_in = articles_list.pop(0)
        parsed_data[article_vertex_in].extend(articles_list)

    fstream.close()

    return parsed_data


def generate_random_graph(nodes_count, prob):
    labels_set = defaultdict(set)
    vertices = range(nodes_count)

    for i in vertices:
        for j in vertices:
            if i != j:
                if prob > random.sample():
                    labels_set[i].add(j)

                if prob > random.sample():
                    labels_set[j].add(i)

    labels_list = {k: list(v) for k, v in labels_set.items()}

    return labels_list


def make_complete_graph(nodes_count):
    graph = dict()

    for node in range(nodes_count):
        graph[node] = list(
            set([node_in for node_in in range(nodes_count) if node != node_in])
        )

    return graph
