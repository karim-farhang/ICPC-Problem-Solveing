class Node:
    def __init__(self, data):
        self.Data = data
        self.child = []
        self.parent = None

    def add_child(self, child):
        self.parent = self
        self.child.append(child)
