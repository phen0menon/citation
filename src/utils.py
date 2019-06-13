from collections import defaultdict
from scipy.stats import binom

import numpy as np


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


def binominal_probability(k, n, p):
    return binom.pmf(k, n, p)


def generate_random_graph(nodes_count, prob):
    labels_set = defaultdict(set)
    vertices = range(nodes_count)

    for i in vertices:
        for j in vertices:
            if i != j:
                prob_a = np.random.sample()

                if prob_a < prob:
                    labels_set[i].add(j)

                prob_a = np.random.sample()

                if prob_a < prob:
                    labels_set[j].add(i)

    labels_list = {k: list(v) for k, v in labels_set.items()}

    return labels_list
