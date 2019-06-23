import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import src.utils as utils
from src.graph import Graph
from src.dpa_trial import DPATrial


def make_histogram_chart(data, title="histogram chart"):
    histogram_options = {
        "color": "black",
        "linestyle": "None",
        "marker": ".",
        "markersize": 6,
    }
    x = data[0]
    y = data[1]
    plt.loglog(x, y, **histogram_options)
    plt.grid(True)
    plt.title(title)
    plt.show()


def make_log_log_chart(data, base=np.e, title="log log chart"):
    """
    Make log-log plot using data and base of logarithm
    :param data: vertices list
    :param base: logarithm base, by default is an exponent
    :return: None
    """
    chart_options = {"basex": base, "basey": base, "color": "black"}
    x = np.array(data)
    y = x ** base

    fig, ax = plt.subplots()

    ax.loglog(x, y, **chart_options)

    # Format prettier ticks on a plot
    def ticks(y, pos):
        return r"$e^{:.0f}$".format(np.log(y))

    ax.xaxis.set_major_formatter(mtick.FuncFormatter(ticks))
    ax.yaxis.set_major_formatter(mtick.FuncFormatter(ticks))

    plt.title(title)
    plt.show()


def DPA(num_nodes, exist_nodes):
    graph = Graph(utils.make_complete_graph(exist_nodes))
    dpa_instance = DPATrial(exist_nodes)

    for new_node in range(exist_nodes, num_nodes):
        graph[new_node] = dpa_instance.run_trial(exist_nodes)

    return graph


def init():
    asset_filename = "../assets/alg_phys-cite.txt"

    # Main Graph
    graph_main = Graph(utils.parse_file(asset_filename))
    graph_main.make_degree_dict()
    graph_main_norms = graph_main.make_normalized_list()
    make_log_log_chart(graph_main_norms, title="Main graph log-log chart")
    make_histogram_chart(graph_main_norms, title="Main graph histogram")

    # Generated ER Graph
    er_graph = Graph(utils.generate_random_graph(1200, 0.4))
    er_graph.make_degree_dict()
    er_graph_norms = er_graph.make_normalized_list()
    make_log_log_chart(er_graph_norms, title="ER graph log-log chart")
    make_histogram_chart(er_graph_norms, title="ER graph histogram")

    # Generated DPA Graph
    m = int(graph_main.get_average_out_degree())
    n = len(graph_main.get_adjacency_list())

    DPA_graph = DPA(n, m)
    DPA_graph.make_degree_dict()
    DPA_graph_norms = DPA_graph.make_normalized_list()
    make_log_log_chart(DPA_graph_norms, title="DPA Log-log Chart")
    make_histogram_chart(DPA_graph_norms, title="DPA Histogram")


if __name__ == "__main__":
    init()
