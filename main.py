from graph import Graph

import utils as utils


def init():
    asset_filename = "assets/alg_phys-cite.txt"

    adj_list = utils.parse_file(asset_filename)

    graph = Graph(adj_list)
    graph.make_degree_dict()
    graph.normalize_degree_dict()

if __name__ == "__main__":
    init()
