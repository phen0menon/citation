import matplotlib.pyplot as plt
import numpy as np
import src.utils as utils
from src.graph import Graph


def make_log_log_chart(data, base=3):
    np_data_x = np.array(data)
    np_data_y = np_data_x ** base

    plt.loglog(np_data_x, np_data_y, basex=base, basey=base)
    plt.show()


def trial_graph(adj_list):
    graph = Graph(adj_list)
    graph.make_degree_dict()

    # norms = graph.make_normalized_degree_dict().get_normalized_degree_dict()
    # make_log_log_chart(norms)
    print(graph.get_average_degree())


def do_graphs_trials(N):
    # trial N graphs
    average_degrees = [
        Graph(utils
              .generate_random_graph(100 * i, 0.5))
              .make_degree_dict()
              .get_average_degree()
        for i in range(1, N)]

    print(sum(average_degrees) / N)


def init():
    asset_filename = "../assets/alg_phys-cite.txt"

    adj_list = utils.parse_file(asset_filename)

    # main graph
    trial_graph(adj_list)

    # trials
    do_graphs_trials(5)


if __name__ == "__main__":
    init()
