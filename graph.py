from collections import defaultdict

class Graph:
    def __init__(self, data):
        self.data = data

    def make_degree_dict(self):
        """
        Makes a dictionary, 
        where key is a degree, 
        where value is a number of elements with this degree
        """
        degree_dict = defaultdict(int)

        for vertex in self.data.keys():
            curr_degree = len(self.data[vertex])
            degree_dict[curr_degree] += 1

        self.degree_dict = degree_dict

    def get_degree_dict(self):
        """
        :return: dict
        """
        return self.degree_dict