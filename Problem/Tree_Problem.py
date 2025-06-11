class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p.parent:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        space = (self.get_level() + 4) * ' '
        print(space, self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_Tree():
    root = TreeNode('Electronic')
    laptop = TreeNode('laptop')
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Surface'))
    laptop.add_child(TreeNode('Thinkpad'))

    cellPhone = TreeNode('cell phone')
    cellPhone.add_child(TreeNode('iphone'))
    cellPhone.add_child(TreeNode('google pixel'))
    cellPhone.add_child(TreeNode('vivo'))

    tv = TreeNode('tv')
    tv.add_child(TreeNode('suamsung'))
    tv.add_child(TreeNode('lg'))

    root.add_child(laptop)
    root.add_child(cellPhone)
    root.add_child(tv)
    return root


if __name__ == '__main__':
    x = build_product_Tree()
    x.print_tree()
