# coding: utf-8
# Your code here!
#Print a string in reverse order.

def reverseIter(string):
	n = len(string)
	str1 = ''
	i = n - 1
	while i >= 0:
		str1 += string[i]
		i -= 1
	return str1
#time complexity  O(n), Auxiliary space O(1)

def reverseRecursive(string, i = 0):
	n = len(string)
	if i == n // 2:
		return 
	string[i], string[n-i-1] = string[n-i-1], string[i]
	reverseRecursive(string, i+1)
# Time complexity O(n), Auxiliary space O(n)


#interative using two pointers
def reverseInter2(string):
	n = len(string)
	i, j = 0, n-1
	while i < j:
		string[i], string[j] = string[j], string[i]
		i += 1
		j -= 1
	return string
#Time Complexity O(n), Auxiliary space O(1)

#reverse using stack
def reverseStack(string):
	stack = []
	for i in range(len(string)):
		stack.append(string[i])

	for i in range(len(string)):
		string[i] = stack.pop()

#using library function
def reverseFun(string):
	return string[::-1]

def main():
	string = "Print a string in reverse order."
	print(reverseIter(string))

	string = list(string) #convert to list as string cant be sliced
	reverseRecursive(string)
	string = ''.join(string) #rejoin to string
	print(string)

	string = "Print a string in reverse order."
	string = list(string)
	reverseInter2(string)
	string = ''.join(string)
	print(string)

	string = "Print a string in reverse order."
	string = list(string)
	reverseStack(string)
	string = ''.join(string)
	print(string)

	string = "Print a string in reverse order."
	print(reverseFun(string))



if __name__ == "__main__":
	main()