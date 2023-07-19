# Python3 Program to check whether valid
# expression is redundant or not

def checkRedundancy(Str):
	
	st = []

	for ch in Str:

		if (ch == ')'):
			top = st[-1]
			st.pop()

			flag = True

			while (top != '('):

				if (top == '+' or top == '-' or
					top == '*' or top == '/'):
					flag = False

				top = st[-1]
				st.pop()

			if (flag == True):
				return True

		else:
			st.append(ch) 
	return False

def findRedundant(Str):
	ans = checkRedundancy(Str)
	if (ans == True):
		print("Yes")
	else:
		print("No")

# Driver code
if __name__ == '__main__':
	Str = "((a+b))"
	findRedundant(Str)


