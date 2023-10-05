class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        llist = ''
        itr = self.head
        while itr:
            llist += str(itr.data)+ '-->'
            itr = itr.next
        print(llist)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_value(self, data_list):
        for items in data_list:
            self.insert_at_end(items)
        return
    
    def get_lenght(self):
        lenght = 0
        itr = self.head
        while itr:
            lenght += 1
            itr = itr.next
        print(f'lenght of linked list: {lenght}')

    def remove_elem(self, index):
        itr = self.head
        cwi = 0
        while itr.next:
            if cwi == index-1:
                itr.next = itr.next.next
                return
            cwi += 1
            itr = itr.next

    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_begining(data)
            return

        cwi = 0
        itr = self.head
        while itr:
            if cwi == index-1:
                new_node = Node(data, itr.next)
                itr.next = new_node
            
            cwi += 1
            itr = itr.next
        return 

    def insert_after_value(self, value, data):
        itr = self.head
        while itr:
            if itr.data == value:
                new_node = Node(data, itr.next)
                itr.next = new_node
            itr = itr.next
        return

    def remove_by_value(self, value):
        itr = self.head
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next

            itr = itr.next
        return

if __name__ == '__main__':
    ll = Linkedlist()
    ll.insert_at_begining(69)
    ll.insert_at_end(77)
    ll.insert_value([43,67,78,99])
    ll.remove_elem(3)
    ll.insert_at_index(5, 52)
    ll.insert_after_value(52, 25)
    ll.print()
    ll.remove_by_value(99)
    ll.get_lenght()

    ll.print()