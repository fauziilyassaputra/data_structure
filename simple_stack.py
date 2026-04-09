class Stack:
    def __init__(self):
        self.data = []

    def push(self,data):
        return self.data.append(data)

    def pop(self):
        if self.is_empty():
            print("data is empty")
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            print("Data is empty")
        print(self.data[-1])

    def is_empty(self):
        return len(self.data) == 0
    
    def print_data(self):
        print(self.data)
    
    def size_data(self):
        print(len(self.data))

data_lagu = Stack()

data_lagu.push("The Feded")
data_lagu.push("on my way")
data_lagu.push("hello hello")
data_lagu.peek()
data_lagu.print_data()
data_lagu.pop()
data_lagu.print_data()
data_lagu.size_data()
