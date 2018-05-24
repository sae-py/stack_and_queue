class Queue:
	def __init__(self):
		self.queue = [0,0,0,0,0]
		self.p = 0

	def enqueue(self,obj):
		self.queue[self.p] = obj
		self.p += 1

	def dequeue(self):
		del self.queue[0]
		self.p -= 1

	def disp(self):
		print(self.queue)

if __name__ == "__main__":
	queue = Queue()
	data = [2,4,6,8,10]
	for i in range(len(data)):
		queue.enqueue(data[i])
	queue.disp()
	for i in range(len(data)):
		queue.dequeue()
		queue.disp()
