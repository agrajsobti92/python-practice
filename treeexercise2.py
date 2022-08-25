class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, input):
        if self.get_level() > input:
            return

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""

        print(prefix + self.name)

        if self.children:
            for child in self.children:
                child.print_tree(input)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_product_tree():
    glob = TreeNode("Global")
    india = TreeNode("India")
    usa = TreeNode("USA")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    cali = TreeNode("California")
    cali.add_child(TreeNode("Mountain View"))
    cali.add_child(TreeNode("San Francisco"))
    cali.add_child(TreeNode("Palo Alto"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa.add_child(nj)
    usa.add_child(cali)

    glob.add_child(india)
    glob.add_child(usa)

    return glob


if __name__ == '__main__':
    root_node = build_product_tree()
    root_node.print_tree(2)
