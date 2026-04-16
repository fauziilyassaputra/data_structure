class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
        

    def push(self,data):
        return self.stack.append(data)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        return print(self.stack[-1])

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
        

    def enqueue(self,data):
        return self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            print("queue is empty")
        return print(self.queue[0])


class Document():
    def __init__(self,nama):
        self.nama = nama
        self.theStack = Stack()
        
    def addPage(self,page):
        self.theStack.push(page)

    def print_page(self):
        if self.theStack.is_empty():
            print("page is empty")
        print(self.theStack.stack)

    def is_empty(self):
        return self.theStack.is_empty()

    def __repr__(self):
        return f"{self.nama}  {self.theStack.stack}"


class PrintQueue:
    def __init__(self):
        self.theQueue = Queue()

    def addDocument(self,data):
        self.theQueue.enqueue(data)

    def printDocument(self):
        while not self.theQueue.is_empty():
            document_current = self.theQueue.dequeue()
            print(f"{document_current.nama}")
            while not document_current.is_empty():
                page_current = document_current.theStack.pop()
                print(page_current)

            

documentA = Document("dokumen A")
documentA.addPage("Page 1")
documentA.addPage("Page 2")
documentA.addPage("Page 3")

documentB = Document("Dokumen B")
documentB.addPage("Page 1")
documentB.addPage("Page 2")

folder = PrintQueue()
folder.addDocument(documentA)
folder.addDocument(documentB)
folder.printDocument()

"""
output:
dokumen A
Page 3
Page 2
Page 1
Dokumen B
Page 2
Page 1
"""

