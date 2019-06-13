from collections import defaultdict

class Graph:
    def __init__(self, data):
        self.data = data

    def make_degree_dict(self):
        """
        Makes a dictionary, 
        where key is a degree, 
        where value is a number of elements with this degree

        :return: dict
        """
        self.degree_dict = defaultdict(int)
        vertices_degree_dict = defaultdict(int)

        for vertices_in in self.data.values():
            for vertex_in in vertices_in:
                vertices_degree_dict[vertex_in] += 1

        for degree in vertices_degree_dict.values():
            self.degree_dict[degree] += 1

    def normalize_degree_dict(self):
        degree_sum = sum(self.degree_dict.keys())

        for degree in self.degree_dict.keys():
            print(degree / degree_sum, end='\t')

    def get_degree_dict(self):
        """
        :return: dict
        """
        return self.degree_dict