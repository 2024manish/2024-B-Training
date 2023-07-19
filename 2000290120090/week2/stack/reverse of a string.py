# Python program to reverse a string using stack

# Function to create an empty stack.
# It initializes size of stack as 0


def createStack():
	stack = []
	return stack

# Function to determine the size of the stack


def size(stack):
	return len(stack)

# Stack is empty if the size is 0


def isEmpty(stack):
	if size(stack) == 0:
		return true

# Function to add an item to stack .
# It increases size by 1


def push(stack, item):
	stack.append(item)

# Function to remove an item from stack.
# It decreases size by 1


def pop(stack):
	if isEmpty(stack):
		return
	return stack.pop()

# A stack based function to reverse a string


def reverse(string):
	n = len(string)

	stack = createStack()

	for i in range(0, n, 1):
		push(stack, string[i])

	string = ""

	for i in range(0, n, 1):
		string += pop(stack)

	return string


string = "oraganic farming"
string = reverse(string)
print("Reversed string is " + string)

# This code is contributed by Sunny Karira
