class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head, None)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
            self.tail = node
            return

        node = Node(data, None, self.tail)
        self.tail.next = node
        self.tail = node

    def print_forward(self):
        # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def print_backward(self):
        # Print linked list in reverse direction. Use node.prev for this.
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.tail
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.prev else str(itr.data)
            itr = itr.prev
        print(llstr)


ll = LinkedList()
ll.insert_at_end("Apple")
ll.insert_at_end("Orange")
ll.insert_at_end("Banana")
ll.insert_at_end("Apple123")
ll.print_forward()
ll.print_backward()
