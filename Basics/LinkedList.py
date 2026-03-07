# LINKED LIST
from logging import raiseExceptions


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkList:
    def __init__(self):
        self.head = None

    def get_length(self):
        if self.head is None:
            return 0

        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count+=1

        return count

    def insert_at_beginning(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return

        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)
        return

    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_beginning(data)

    def remove_by_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        if self.get_length() <= 0:
            raise Exception("Linked List Empty")

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def insert_by_index(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            node = Node(data, self.head)
            self.head - node

        itr = self.head
        count = 0
        while itr:
            if count == index-1 :
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.get_length() <= 0:
            raise Exception("Linked List is empty")

        if self.head.data == data_after:
            node = Node(data_to_insert, self.head.next)
            self.head.next = node
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

    def print(self):
        if self.head is None:
            raise Exception("Linked List is empty")

        itr = self.head
        ll_str = ''

        while itr:
            ll_str += str(itr.data) + '--> '
            itr = itr.next

        print(ll_str)

if __name__ == '__main__':
    ll = LinkList()
    # ll.insert_at_beginning(10)
    # ll.insert_at_beginning(20)
    ll.insert_values([10,20,30,40,50])
    ll.insert_at_end(34)
    ll.print()
    ll.insert_by_index(2,100)
    # ll.print()
    # ll.remove_by_value(100)
    ll.print()
    ll.insert_after_value(34, 35)
    ll.print()
