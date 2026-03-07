# Doubly Linked List

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def get_length(self):
        if self.head is None:
            return 0

        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
            return
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
            return

        last_node = self.get_last_node()
        last_node.next = Node(data, None, last_node)

    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_beginning(data)

    def insert_by_index(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.insert_at_beginning(data)

        itr = self.head
        count = 0
        while itr:
            if count == index-1 :
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Linked List is Empty')

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        itr = self.head
        count = 0
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr = itr.next
            count += 1

    def print_frontward(self):
        if self.head is None:
            print('Linked List is empty')

        itr = self.head
        dll_str = ''
        while itr:
            dll_str += str(itr.data) + ' --> '
            itr = itr.next

        print(dll_str)

    def print_backward(self):
        if self.head is None:
            print('Linked List is empty')

        node = self.get_last_node()
        dll_str = ''
        while node:
            dll_str += str(node.data) + ' <-- '
            node = node.prev

        print(dll_str)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

if __name__ == '__main__':
    dll = DoublyLinkedList()
    # dll.insert_at_beginning(10)
    # dll.insert_at_beginning(20)
    dll.insert_values([1,2,3,4,5])
    dll.insert_at_end(11)
    dll.insert_by_index(2,22)
    dll.print_frontward()
    dll.print_backward()
    dll.remove_at(2)
    dll.print_backward()
    dll.print_frontward()