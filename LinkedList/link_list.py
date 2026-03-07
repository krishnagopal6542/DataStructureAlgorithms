class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at_index(self, idx, data):
        if idx < 0 or idx > self.get_length():
            raise Exception("Invalid Index")

        if idx == 0:
            self.insert_at_beginning(data)
            return

        itr = self.head
        counter = 0
        while itr.next:
            counter += 1
            if counter == idx - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next

    def insert_after_value(self, data_to_insert, data_after):
        pass

    def remove_at_index(self, idx):
        if idx < 0 or idx > self.get_length():
            raise Exception('Invalid Index')

        if idx == 0:
            self.head = self.head.next

        itr = self.head
        counter = 0
        while itr.next:
            counter += 1
            if counter == idx - 1:
                itr.next = itr.next.next
                break
            itr = itr.next

    def remove_by_value(self, value):
        pass

    def get_length(self):
        if self.head is None:
            return 0

        itr = self.head
        length = 0
        while itr:
            length += 1
            itr = itr.next

        return length

    def print(self):
        if self.head is None:
            print("Link List is empty !")
            return

        itr = self.head
        ll_str = ''
        while itr:
            ll_str += str(itr.data) + '-->'
            itr = itr.next
        print(ll_str)

    def insert_values(self, values):
        """ Creating new Link List """
        self.head = None

        for value in values:
            self.insert_at_end(value)


if __name__ == '__main__':
    val = [10, 20, 30, 50]
    ll = LinkList()
    ll.insert_values(values=val)
    ll.print()
    print('Length: ', ll.get_length())
    ll.insert_at_index(4, 40)
    ll.print()
