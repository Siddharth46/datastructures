class Node:
    def __init__(self, data= None, next= None, prev= None):
        self.data = data
        self.next = next
        self.prev = prev

class Linkedlist:
    def __init__(self):
        self.head = None

    def print_forward(self):
        itr = self.head
        llist = ''
        while itr:
            llist = llist +str(itr.data)+'-->'
            itr = itr.next
        print(llist)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def print_backward(self):
        last_node = self.get_last_node()
        itr = last_node
        llist = ''
        while itr:
            llist  += str(itr.data)+'-->'
            itr = itr.prev
        print(llist)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)

#    def insert_values(self, list_values):

if __name__ == '__main__':
    ll = Linkedlist()
    ll.insert_at_end(23)
    ll.insert_at_end(46)
    ll.insert_at_end(53)
    ll.print_forward()
    ll.print_backward()