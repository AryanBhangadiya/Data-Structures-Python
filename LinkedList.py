# Creating a node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # inserting at beginning of the list
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    # inserting at the end 
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    # inserting the values from the list
    def insert_list_values(self, my_list):
        self.head = None
        for data in my_list:
            self.insert_at_end(data)

    # inserting value at specified index
    def insert_at(self, index, data):
        if index < 0 or index > self.list_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    # inserting an element after first occurence of the element
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            raise Exception("Linked List is empty")
        
        self.seacrh_engine(data_after)

        itr = self.head

        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                return
            itr = itr.next
    # finding the length of the list
    def list_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    # removing the element from specified index
    def remove_index(self, index):
        if index < 0 or index >= self.list_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        itr = self.head 
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1
    
    # removing an element by value
    def remove_by_value(self, data):
        if self.head is None:
            raise Exception("Linked List is empty")
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        count1 = 0
        itr = self.head        
        while itr:
            count1 += 1
            if itr.data == data:
                break
            itr = itr.next
        
        count2 = 1
        itr = self.head
        while itr:
            if count2 == count1-1:
                itr.next = itr.next.next
                break
            count2 += 1
            itr = itr.next

    # searching an element
    def seacrh_engine(self, element):
        itr = self.head
        count = 1
        while itr:
            if itr.data == element:
                print("Element Found:", itr.data)
                break

            if count == self.list_length():
                print("Invalid Element")
                break 

            itr = itr.next
            count += 1

    # printing the Linked list
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        ptr = self.head
        llstr = ''

        while ptr:
            llstr += str(ptr.data) + '-->'
            ptr = ptr.next
        print(llstr)


if __name__ == '__main__':

    ll = LinkedList()

    # ll.insert_at_begining(5)
    # ll.insert_at_begining(10)
    # ll.insert_at_begining(15)
    # ll.insert_at_end(0)

    ll.insert_list_values([1, 2, 3, 4, 5])

    ll.print()
    print("length:", ll.list_length())

    # ll.remove_index(2)
    
    ll.insert_at(0, 0)
    ll.insert_at(3, 2.5)
    ll.print()
    
    # ll.seacrh_engine(5)
    # ll.seacrh_engine(11)

    ll.insert_after_value(2, 2.4)
    ll.insert_after_value(10, 11)
    ll.print()

    ll.remove_by_value(5)
    ll.print()