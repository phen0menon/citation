from collections import defaultdict


class Graph:
    def __init__(self, data):
        self.normalized_list = list()
        self.degree_dict = defaultdict(int)
        self.data = data

    def make_degree_dict(self):
        """
        Makes a dictionary, 
        where key is a degree, 
        where value is a number of elements with this degree

        :return: dict
        """
        vertices_degree_dict = defaultdict(int)

        for vertices_in in self.data.values():
            for vertex_in in vertices_in:
                vertices_degree_dict[vertex_in] += 1

        for degree in vertices_degree_dict.values():
            self.degree_dict[degree] += 1

        return self.degree_dict

    def make_normalized_degree_list(self):
        degree_sum = sum(self.degree_dict.keys())

        return [degree / degree_sum for degree in self.degree_dict.keys()]

    def get_average_degree(self):
        degrees = self.degree_dict.keys()
        degree_sum = sum(degrees)
        degrees_count = len(degrees)

        return degree_sum / degrees_count

    def get_normalized_degree_dict(self):
        return self.normalized_list

    def get_degree_dict(self):
        return self.degree_dict
