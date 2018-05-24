
class Stack:
	def __init__(self):
		self.stack = [0,0,0,0,0]
		self.p = 0

	def push(self,obj):
		self.stack[self.p] = obj
		self.p += 1

	def pop(self):
		del self.stack[self.p-1]
		self.p -= 1

	def disp(self):
		print(self.stack)

if __name__ == "__main__":
	stack = Stack()
	data = [2,4,6,8,10]
	for i in range(len(data)):
		stack.push(data[i])
	stack.disp()
	for i in range(len(data)):
		stack.pop()
		stack.disp()
