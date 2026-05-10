from stack_with_array import Stack

filename = "tinyTale.txt"
try:
    with open(filename, "r") as file:
        text = file.read()

    words = text.split()
    stack = Stack()

    for word in words:
        stack.push(word)

    while not stack.is_empty():
        print(stack.pop(), end=" ")

except FileNotFoundError:
    print("File not found")

