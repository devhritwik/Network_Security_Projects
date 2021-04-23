from flask import Flask
app = Flask(__name__)

import random

#Inverts the permutation by reversing the order
def InversePermutation(lis):
	pop = [0]*len(lis)
	for j in range(len(lis)):
		pop[lis[j]-1] = j+1
	return pop

#Creates the permutation by deleting the items in ignor list
def CreatePermutation(lis,ignor):
	for j in ignor:
		lis.remove(j)
	return lis

#Randomly shuffles the content of the array
def RandomShuffle(i,lis):
	size = len(lis)
	for j in range(i):
		a = random.randint(0,size)%size
		b = random.randint(0,size)%size
		lis[a],arr[b] = lis[b],lis[a]
	return lis

#Creates the randomly shuffled array
def CreateArray(pop):
	return RandomShuffle(50,[j+1 for j in range(pop)])

#Module to generate S-P Boxes
class SpBoxGenerator:
	
    @app.route('/SP-Generator')
	def __init__(self,blockSize,seed):
		random.seed(seed)
		self.seed = seed
		self.blockSize = blockSize
		self.run()

	def run(self):
		ignor = self.blockSize//8
        #Inverted Permuation
		self.IP = CreatePermutation(CreateArray(self.blockSize),[])
		self.IP_ = InversePermutation(self.IP)
		self.S_BOX = []
		#Initial Per,utation
        self.PC1 = CreatePermutation(CreateArray(self.blockSize),CreateArray(ignor))
		self.PC2 = CreatePermutation(CreateArray(self.blockSize-ignor),CreateArray(ignor))
		
		for i in range(ignor):
			pop = [x for x in range(16)]
			s_pop = []
			for k in range(4):
				s_pop.append(RandomShuffle(50,pop))
			self.S_BOX.append(s_pop)
		
		#P-Box which shuflles the 32bit block
		self.P = createPermutation(CreateArray(ignor*4),[])

		#ECreating the Exapnsive Box
		E_pop = [i+1 for i in range(ignor*4)]
		self.E = []
		for i in range(0,len(E_pop),4):
			self.E.append(E_pop[i-1])
			for j in range(i,i+4,1):
				self.E.append(E_pop[j])
			self.E.append(E_pop[(i+4)%len(E_pop)])

		#Matrix that determine the shift for each round of keys
		self.SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]