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

def balanced_parantheses(soal_kurung):
    stack = Stack()
    tipe_kurung = {"(":")","[":"]", "{":"}"}
    for kurung in soal_kurung:
        if kurung in tipe_kurung:
            stack.push(kurung)
        elif kurung in (")","]","}") and (
            stack.is_empty() or tipe_kurung[stack.pop()] != kurung
        ):
            return False
    return stack.is_empty()

stack = Stack()
stack.is_empty()
print(balanced_parantheses("([]{})"))
print(balanced_parantheses('[()]{}{[()()]()}'))
print(balanced_parantheses('[(]'))
