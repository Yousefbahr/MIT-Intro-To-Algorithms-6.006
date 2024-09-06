class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        node = Doubly_Linked_List_Node(x)
        if self.head is None or self.tail is None:
            self.head = self.tail = node

        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insert_last(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        node = Doubly_Linked_List_Node(x)
        if self.head is None or self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node


    def delete_first(self):
        # x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        # Make sure there is atleast one element
        assert self.head
        x = self.head
        self.head = x.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None

        return x.item

    def delete_last(self):
        # x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        # Make sure there is atleast one element
        assert self.tail
        x = self.tail
        self.tail = x.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None

        return x.item

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! # 
        ###########################
        L2.head = x1
        L2.tail = x2
        if x1 == self.head:
            self.head = x2.next
        else:
            x1.prev.next = x2.next

        if x2 == self.tail:
            self.tail = x1.prev
        else:
            x2.next.prev = x1.prev

        return L2

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! # 
        ###########################
        x1 = L2.head
        x2 = L2.tail
        xn = x.next
        L2.head = None
        L2.tail = None
        x1.prev = x
        x.next = x1
        x2.next = xn
        if xn is None:
            self.tail = x2
        else:
            xn.prev = x2


