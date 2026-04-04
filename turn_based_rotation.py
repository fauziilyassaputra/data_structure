class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        # self.prev = None

class CircularLinklist:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next
            if node == self.head:
                break
    
    def __len__(self):
        return sum(1 for _ in self)

    def insert_nth(self,index,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head = new_node
        elif index == 0:
            new_node.next = self.head
            # self.head.prev = new_node
            self.head = new_node
            # self.head.prev = self.tail
            self.tail.next = self.head
            # if self.tail is not None:
            #     self.tail.next = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            # new_node.prev = temp
            new_node.next = temp.next
            # temp.next.prev = new_node
            temp.next = new_node
            if index == len(self) - 1:
                self.tail = new_node
                new_node.next = self.head
              
    
    def insert_head(self,data):
        return self.insert_nth(0,data)

    def insert_tail(self,data):
        return self.insert_nth(len(self), data)

    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print(f"(Back to {current.data}) \n")

    def print_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.tail:
                break
        print(f"(Back to {current.data}) \n")
    
    def print_all(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            if current == self.head:
                break
        print(f"(Back to {current.data})")

    def delete_head(self):
        return self.delete_nth(0)

    def delete_tail(self):
        return self.delete_nth(len(self) - 1) 
    
    def delete_nth(self,index):
        if self.head == self.tail:
            self.head == self.tail == None
        elif index == 0:
            self.head = self.head.next
            self.tail.next = self.head
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            delete_node = temp.next
            temp.next = temp.next.next
            if temp == len(self) - 1:
                self.tail = temp
            return delete_node.data


        
wadah = CircularLinklist()

player1 = Node("Player A")
player2 = Node("Player B")
player3 = Node("Player C")


# tetapkan identitas head dan tail
wadah.head = player1
wadah.tail = player3

# hubungan player
player1.next = player2
player2.next = player3
player3.next = player1

print("Urutan pemain awal:")
wadah.print_forward()

print("Tambah 'Player D' setelah 'Player B':")
wadah.insert_nth(2,"player D")
wadah.print_forward()

print("Simulasi satu putaran penuh:")
wadah.print_all()