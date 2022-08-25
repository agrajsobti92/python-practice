class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        des = " (" + self.designation + ")"
        if input == "name":
            print(prefix + self.name)
        elif input == "designation":
            print(prefix + self.designation)
        elif input == "both":
            print(prefix + self.name + des)

        if self.children:
            for child in self.children:
                child.print_tree(input)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_product_tree():
    nilupul = TreeNode("Nilupul", "CEO")
    chinmay = TreeNode("Chinmay", "CTO")

    gels = TreeNode("Gels", "HR Head")
    gels.add_child(TreeNode("Peter", "Rec Manager"))
    gels.add_child(TreeNode("Waqas", "Policy Manager"))

    vishwa = TreeNode("Vishwa", "Infra Head")
    vishwa.add_child(TreeNode("Dhaval", "Cloud Manager"))
    vishwa.add_child(TreeNode("Abhijit", "App Manager"))

    nilupul.add_child(chinmay)
    nilupul.add_child(gels)
    chinmay.add_child(vishwa)
    chinmay.add_child(TreeNode("Aamir", "Apps Head"))

    return nilupul


if __name__ == '__main__':
    root_node = build_product_tree()
    # root_node.print_tree("name")  # prints only name hierarchy
    # root_node.print_tree("designation")  # prints only designation hierarchy
    # # prints both (name and designation) hierarchy
    root_node.print_tree("both")
