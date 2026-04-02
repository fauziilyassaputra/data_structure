class Node:
  def __init__(self,data,_id):
    self.data = data
    self._id = _id
    self.next = None
  
 
class LinkedList:
  def __init__(self):
    self.head = None
  
  def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

  def __len__(self):
    return sum(1 for _  in self)

  def insert_head(self,new_value,_id):
    self.insert_nth(0,new_value,_id)

  def insert_tail(self,new_value, _id):
    self.insert_nth(len(self),new_value, _id)
  

  def insert_nth(self, index, new_value,_id):
    new_node = Node(new_value, _id)
    if self.head == None:
      self.head = new_node
    elif index == 0 :
      new_node.next = self.head
      self.head = new_node
    else:
      temp = self.head
      for _ in range(index - 1):
        temp = temp.next
      new_node.next = temp.next
      temp.next = new_node

  def print_list(self):
    current = self.head
    while current is not None:
      print(current.data, end=" -> ")
      current = current.next
    print('None')

  def search(self,target):
    current = self.head
    while current is not None:
      if current._id == target:
        return f"buku dengan id {current._id} yaitu {current.data} tersedia"
      current = current.next
    return f"buku dengan id {target} tidak tersedia"

  def delete_id(self,target):
    current = self.head
    while current is not None:
      if current._id != target:
        current = current.next
        current.next = current.next.next
        return current
      current = current.next
    return None

  def all_node(self):
    print( f"seluruh node berjumlah: {len(self)}")

# menambahkan buku
linked_list = LinkedList()
linked_list.insert_head("bumi", "tr1")
linked_list.insert_tail("bulan", "tr2")
linked_list.insert_tail("matahari", "tr3")
linked_list.print_list()

#  mencari buku berdasarkan id
print(linked_list.search("tr3"))

# menghapus buku berdasarkan id
linked_list.delete_id("tr2")
linked_list.print_list()


linked_list.insert_head("bintang","tr4")
linked_list.insert_tail("komet","tr5")
linked_list.insert_tail("komet minor", "tr5")
linked_list.print_list()

# menghitung panjang node
linked_list.all_node()
