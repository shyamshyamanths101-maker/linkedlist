class SNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    # 1. Insert at beginning
    def insert_begin(self, data):
        n = SNode(data)
        n.next = self.head
        self.head = n

    # 2. Insert at end
    def insert_end(self, data):
        n = SNode(data)
        if self.head is None:
            self.head = n
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = n

    # 3. Insert at position
    def insert_pos(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return
        if pos == 1:
            self.insert_begin(data)
            return
        temp = self.head
        for _ in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next
        if temp is None:
            print("Invalid position")
            return
        n = SNode(data)
        n.next = temp.next
        temp.next = n

    # 4. Delete from beginning
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    # 5. Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    # 6. Delete from position
    def delete_pos(self, pos):
        if pos < 1 or self.head is None:
            print("Invalid position or empty list")
            return
        if pos == 1:
            self.delete_begin()
            return
        temp = self.head
        for _ in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next
        if temp is None or temp.next is None:
            print("Invalid position")
            return
        temp.next = temp.next.next

    # 7. Display
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")



# DOUBLY LINKED LIST (DLL)

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    # 1. Insert at beginning
    def insert_begin(self, data):
        n = DNode(data)
        n.next = self.head
        if self.head:
            self.head.prev = n
        self.head = n

    # 2. Insert at end
    def insert_end(self, data):
        n = DNode(data)
        if self.head is None:
            self.head = n
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = n
        n.prev = temp

    # 3. Insert at position
    def insert_pos(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return
        if pos == 1:
            self.insert_begin(data)
            return
        temp = self.head
        for _ in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next
        if temp is None:
            print("Invalid position")
            return
        n = DNode(data)
        n.next = temp.next
        n.prev = temp
        if temp.next:
            temp.next.prev = n
        temp.next = n

    # 4. Delete from beginning
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    # 5. Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None

    # 6. Delete from position
    def delete_pos(self, pos):
        if pos < 1 or self.head is None:
            print("Invalid position or empty list")
            return
        if pos == 1:
            self.delete_begin()
            return
        temp = self.head
        for _ in range(pos - 1):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next
        if temp is None:
            print("Invalid position")
            return
        if temp.next:
            temp.next.prev = temp.prev
        temp.prev.next = temp.next

    # 7. Display
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

# CIRCULAR LINKED LIST (CLL)

class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CLL:
    def __init__(self):
        self.head = None

    # 1. Insert at beginning
    def insert_begin(self, data):
        n = CNode(data)
        if self.head is None:
            self.head = n
            n.next = n
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        n.next = self.head
        temp.next = n
        self.head = n

    # 2. Insert at end
    def insert_end(self, data):
        n = CNode(data)
        if self.head is None:
            self.head = n
            n.next = n
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = n
        n.next = self.head

    # 3. Insert at position
    def insert_pos(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return
        if pos == 1:
            self.insert_begin(data)
            return
        if self.head is None:
            print("Invalid position")
            return
        temp = self.head
        for _ in range(pos - 2):
            temp = temp.next
            if temp == self.head:
                print("Invalid position")
                return
        n = CNode(data)
        n.next = temp.next
        temp.next = n

    # 4. Delete from beginning
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        self.head = self.head.next
        temp.next = self.head

    # 5. Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        temp.next = self.head

    # 6. Delete from position
    def delete_pos(self, pos):
        if pos < 1 or self.head is None:
            print("Invalid position or empty list")
            return
        if pos == 1:
            self.delete_begin()
            return
        temp = self.head
        for _ in range(pos - 2):
            temp = temp.next
            if temp.next == self.head:
                print("Invalid position")
                return
        if temp.next == self.head:
            print("Invalid position")
            return
        temp.next = temp.next.next

    # 7. Display
    def display(self):
        if self.head is None:
            print("Empty list")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

# MAIN PROGRAM / TEST
s = SLL()
s.insert_begin(20)
s.insert_begin(10)
s.insert_end(40)
s.insert_pos(30, 3)
print("SLL:")
s.display()
s.delete_begin()
s.delete_end()
s.delete_pos(1)
s.display()

d = DLL()
d.insert_begin(20)
d.insert_begin(10)
d.insert_end(40)
d.insert_pos(30, 3)
print("\nDLL:")
d.display()
d.delete_begin()
d.delete_end()
d.delete_pos(1)
d.display()

c = CLL()
c.insert_begin(20)
c.insert_begin(10)
c.insert_end(40)
c.insert_pos(30, 3)
print("\nCLL:")
c.display()
c.delete_begin()
c.delete_end()
c.delete_pos(1)
c.display()
