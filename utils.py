from collections import defaultdict

import os


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
