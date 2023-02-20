class SortedList:
	class Node:
		
		# Node is internal.  Feel free to add
		# to the argument list for its init function if you want
		# you can add additonal data members if you like
		#def __init__(self, data,next=None,prev=None):
		def __init__(self, data):
			self.data = data
			self.next = None
			self.prev = None

	# Sorted list is external, do not change its prototype.
	# you can add additional data members if you like
	def __init__(self):
		self.front = None
		self.back = None
    
	def insert(self,data):
		
		nn = SortedList.Node(data)
  
		# if the list is empty
		# node to be inserted at the beginning
		if (self.front == None):
			self.front = nn
			self.back = nn
			self.front.prev = None
			self.front.next = None
   
		# If the node is to be inserted at 
        # the beginning of the doubly linked list
		elif nn.data <= self.front.data :
			nn.prev = None; self.front.prev = nn
			nn.next = self.front
			self.front = nn
		
		# if the node is to be inserted at
		# the end of the doubly linked list
		elif nn.data > self.back.data:
			nn.prev = self.back
			self.back.next = nn
			self.back = nn
			
		else:
			temp = self.front.next
   			# Locate the node after which
            # the new node  is to be inserted
			while (temp.data < nn.data): temp = temp.next
			
			temp.prev.next = nn
			nn.prev = temp.prev
			temp.prev = nn
			nn.next = temp
   
	def remove(self,data):
    	# Linked list is empty
		if (self.front == None): return False

		elif(self.front == self.back and self.front.data == data):
			self.front = None
			self.back = None
			return True
		else:
			# if data is at the start
			if (self.front.data == data):
				self.front = self.front.next
				self.front.prev = None
				return True

			# if data is at the end
			elif (self.back.data == data):
				self.back = self.back.prev
				self.back.next = None
				return True
			# if data is at a specific position within the list
			else:
				ptr = self.front
				while (ptr != None):
					if (ptr.data == data):
						ptr.prev.next = ptr.next
						ptr.next.prev = ptr.prev
						return True
					else:
						ptr = ptr.next

				if(ptr == None):
					return False

	def is_present(self, data):
		ptr = self.front
		while (ptr != None):
			if (ptr.data == data):
				return True
			else:
				ptr = ptr.next
		if(ptr == None):
			return False


	def __len__(self):
		count = 0
		ptr = self.front
		while (ptr != None):
			count= count + 1
			ptr = ptr.next
   
		return count

	# This is the version you need if you do not use sentinels:
	def __iter__(self):
		curr = self.front
		while curr:
			yield curr.data
			curr=curr.next

	def __reversed__(self):
		curr = self.back
		while curr:
			yield curr.data
			curr=curr.prev
