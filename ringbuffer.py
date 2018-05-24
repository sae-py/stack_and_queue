class Ringbuffer:
	def __init__(self):
		self.queue = [0,0,0,0,0]
		self.p = 0

	def enqueue(self,obj):
		if self.p >= 5:
			self.p =  int(self.p/5)-1
		self.queue[self.p] = obj
		self.p += 1

	def dequeue(self):
		self.queue[self.p-1] = 0
		self.p -= 1

	def disp(self):
		print(self.queue)

if __name__ == "__main__":
	ringbuffer = Ringbuffer()
	data = [2,4,6,8,10]
	for i in range(len(data)):
		ringbuffer.enqueue(data[i])
	ringbuffer.disp()
	for i in range(2):
		ringbuffer.dequeue()
		ringbuffer.disp()
	for i in range(4):
		ringbuffer.enqueue(data[i])
		ringbuffer.disp()


