from collections import defaultdict
from statistics import mean


class Graph:
    def __init__(self, data):
        self._normalized_list = list()
        self._degree_dict = defaultdict(int)
        self._adjacency_list = data

    def get_adjacency_list(self):
        return self._adjacency_list

    def compute_in_degrees(self):
        vertices_degree_dict = defaultdict(int)

        for edges in self._adjacency_list.values():
            for vertex_in in edges:
                vertices_degree_dict[vertex_in] += 1

        return vertices_degree_dict

    def compute_out_degrees(self):
        return {v: len(e) for v, e in self._adjacency_list.items()}

    def get_average_out_degree(self):
        return mean(self.compute_out_degrees().values())

    def make_degree_dict(self):
        """
        Makes a dictionary, 
        where key is a degree, 
        where value is a number of elements with this degree

        :return: dict
        """
        self.vertices_degree_dict = self.compute_in_degrees()

        for degree in self.vertices_degree_dict.values():
            self._degree_dict[degree] += 1

        return self._degree_dict

    def normalize(self, some_list):
        divisor = float(sum(some_list))
        return [element / divisor for element in some_list]

    def make_normalized_list(self):
        keys = sorted(self._degree_dict.keys())
        values = [self._degree_dict[key] for key in keys]

        return [self.normalize(keys), self.normalize(values)]

    def get_average_degree(self):
        return mean(self.vertices_degree_dict.values())

    def get_normalized_degree_dict(self):
        return self._normalized_list

    def get_degree_dict(self):
        return self._degree_dict

    def __setitem__(self, node, edges):
        self._adjacency_list[node] = edges.copy()
        return self

    def __getitem__(self, node):
        return self._adjacency_list[node].copy()

    def __str__(self):
        output = ""

        for key, value in self._adjacency_list.items():
            output += str(key) + " => " + ", ".join(list(map(str, value))) + "\n"

        return output
