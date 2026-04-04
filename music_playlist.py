class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinked:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self):
        return sum(1 for _ in self)
    
    def insert_head(self,data):
        self.insert_nth(0,data)

    def insert_tail(self,data):
        self.insert_nth(len(self),data)
    
    def insert_nth(self,index,data):
        if self.head == None:
            self.head = data
        new_node = Node(data)
        # insert head
        if index == 0:
            self.head.prev = new_node
            new_node.next = self.head 
            self.head = new_node
        # insert tail
        elif index == len(self):
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
        # insert nth 
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            temp.prev.next = new_node
            new_node.prev = temp.prev
            new_node.next = temp
            temp.prev = new_node

    def delete_head(self):
        return self.delete_nth(0)

    def delete_tail(self):
        return self.delete_nth(len(self) - 1)

        
    def delete_nth(self,index):
        if len(self) == 1:
            self.head = self.tail = None
        # Delete head
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        # Delete tail
        elif index == len(self) - 1:
            delete_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        # Delete Nth
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            delete_node = temp
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
        return delete_node.data


    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <=> ")
            current = current.next
        print('\n')

    def print_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <=> ")
            current = current.prev
        print('\n')


# pemanggil
dll = DoubleLinked()

node1 = Node("Numb")
node2 = Node("In The End")
node3 = Node("Faint")
node4 = Node("Breaking the habit")

# insert head and tail
dll.head = node1
dll.tail = node4

# set node 1
node1.next = node2

#set node 2
node2.prev = node1
node2.next = node3

#set node 3
node3.prev = node2
node3.next = node4

#set node 4
node4.prev = node3

print("playlist awal (forward): ")
dll.print_forward()
print("playlist awal (backward): ")
dll.print_backward()

print("Tambah lagu 'One More Light' di depan: ")
dll.insert_head("One More Light")
dll.print_forward()

print("Tambah lagu 'PaparCut' setelah 'in the end': ")
dll.insert_nth(4,"PaperCut")
dll.print_forward()

print("Hapus lagu 'faint':")
dll.delete_nth(4)
dll.print_forward()

print("Playlist akhir (backward):")
dll.print_backward()