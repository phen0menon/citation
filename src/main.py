import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import src.utils as utils
from src.graph import Graph
from src.dpa_trial import DPATrial


def make_log_log_chart(data, base=np.e):
    """
    Make log-log plot using data and base of logarithm
    :param data: vertices list
    :param base: logarithm base, by default is an exponent
    :return: None
    """
    x = np.array(data)
    y = x ** base

    fig, ax = plt.subplots()

    ax.loglog(x, y, basex=base, basey=base)

    # Format prettier ticks on a plot
    def ticks(y, pos):
        return r'$e^{:.0f}$'.format(np.log(y))

    ax.xaxis.set_major_formatter(mtick.FuncFormatter(ticks))
    ax.yaxis.set_major_formatter(mtick.FuncFormatter(ticks))

    plt.show()


def do_graphs_trials(N):
    # trial N graphs
    average_degrees = [
        Graph(utils.generate_random_graph(100 * i, 0.5))
            .make_degree_dict()
            .get_average_degree()
        for i in range(1, N)
    ]

    print(sum(average_degrees) / N)


def init():
    asset_filename = "../assets/alg_phys-cite.txt"

    # Main Graph
    adj_list = utils.parse_file(asset_filename)
    graph_main = Graph(adj_list)
    graph_main.make_degree_dict()
    norms = graph_main.make_normalized_degree_list()
    make_log_log_chart(norms)

    # Generated ER Graph
    er_graph = Graph(utils.generate_random_graph(1200, 0.4))
    er_graph.make_degree_dict()
    er_graph_norms = er_graph.make_normalized_degree_list()
    make_log_log_chart(er_graph_norms)


def DPA(num_nodes, exist_nodes):
    graph = Graph(utils.make_complete_graph(exist_nodes))

    for new_node in range(exist_nodes, num_nodes):
        degree_dict = graph.make_degree_dict()
        degree_sum = sum([v for v in degree_dict.values()])
        trial = DPATrial(degree_sum)
        graph.data[new_node] = trial.run_trial(exist_nodes)

    print(graph.data)


if __name__ == "__main__":
    # init()

    DPA(25, 12)
