class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = Node(data)

    def insert_list(self, list):
        for data in list:
            self.insert(data)

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                temp.next = temp.next.next
                break

            count += 1
            temp = temp.next

    def insert_at(self, index, data):
        add = Node(data)

        if index == 0:
            add.next = self.head
            self.head = add
            return

        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                add.next = temp.next
                temp.next = add
                break

            count += 1
            temp = temp.next

    def __repr__(self):
        tmp = self.head
        list = []
        while tmp is not None:
            list.append(tmp.data)
            tmp = tmp.next
        return str(list)


llist = LinkedList()
llist.insert('a')
llist.insert('agraj')
llist.insert_list(['a', 'b', 'c'])
print(llist)
llist.remove(1)
print(llist)
llist.insert_at(1, 'anuj')
print(llist)


# llist = LinkedList()
# first_node = Node('a')
# print(first_node)
# llist.head = first_node

# print(llist)

# second_node = Node("b")
# third_node = Node("c")
# first_node.next = second_node
# second_node.next = third_node

# print(llist)
