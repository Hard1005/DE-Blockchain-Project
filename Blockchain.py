import time
import hashlib

class Block:
	def __init__(self , data , prev_hash , height , timestamp = None):
		self.prev_hash = prev_hash
		self.height = height
		self.data = data
		self.timestamp = timestamp or time.time()
		self.hash = self.calculate_hash()

	def calculate_hash(self):
		strr = "{}{}{}".format(self.prev_hash , self.height , self.data )
		return hashlib.sha256(strr.encode()).hexdigest()

class Blockchain:

	def __init__(self):
		self.chain = []
		self.curr_data = {}
		self.create_genesis()

	def create_genesis(self):
		self.curr_data = {"0" : "The first Block of the chain"}
		self.Create_Block("0")

	def Create_Block(self , prev_hash = None):
		blk = Block(  self.curr_data , prev_hash or self.get_last_block().hash , len(self.chain))
		self.chain.append(blk)
		self.curr_data = {}
		return blk

	def get_last_block(self):
		return self.chain[-1]


	def add_data(self):

		ch = 'Y'
		data = {}
		while(ch == 'Y'):
			idd = input("Enter the id of the patient: ")
			rec = input("Enter the record: ")
			data[idd] = rec
			ch = input("Press (Y) to enter more records: ")
			print(data)
		self.curr_data = data
		self.Create_Block()

	def disp_chain(self):
		for x in self.chain:
			print(x.data)

	def see_records(self):
		idd = input("Enter the id whose records u want to see..")
		disp_data = []
		for x in self.chain:
			disp_data.append(x.data.get(idd , None))

		disp_data.remove(None)
		if(len(disp_data) == 0):
			print("The given id could not be found.")
		else:
			print("Here are the medical records of ID: " + str(id))
			for x in disp_data:
				print(x)




bc = Blockchain()
print(bc.chain[0].hash)

while(1):
	ch = input("1 - Add Data \n2 - Display Chain \n3 - Display Specific Records:- ")
	if ch == '1':
		bc.add_data()
	elif ch == '2':
		bc.disp_chain()
	elif ch == '3':
		bc.see_records()
