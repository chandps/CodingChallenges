class Node(object):

    """Node class"""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def add_next(self, new_next):
        self.next = new_next


def print_list(head):
    end = False
    current = head
    while end is not True:
        print(current.get_data())
        if current.get_next() is None:
            end = True
        else:
            current = current.get_next()


def reverse_list(head):
    prev = None
    current = head
    next_node = a.get_next()
    while next_node is not None:
        current.add_next(prev)
        prev = current
        current = next_node
        next_node = next_node.get_next()
        if next_node is None:
            current.add_next(prev)


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.add_next(b)
b.add_next(c)
c.add_next(d)

print_list(a)

print('reversed list:')

reverse_list(a)
print_list(d)
