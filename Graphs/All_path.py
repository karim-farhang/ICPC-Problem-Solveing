class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for statr, end in edges:
            if statr in self.graph_dict:
                self.graph_dict[statr].append(end)
            else:
                self.graph_dict[statr] = [end]
        print("graph", self.graph_dict)

    def get_pahts(self, start, end, path=[]):
        path = [start] + [end]
        allpaths = list()
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_pahts(node, end, path)
                for x in new_path:
                    allpaths.append(x)
        return allpaths

