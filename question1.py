class Calculator():
	
	def __init__(self, array):
		self.array = array
		
	def sum(self):
		if self.array[1] == ',':
			self.array = [int(x) for x in self.array.split(',')]
		elif self.array[1] == '|':
			self.array = [int(x) for x in self.array.split('|')]
		else:
			pass
		sum = 0
		for x in self.array:
			sum+=int(x)
			
		return sum

array = ('1|2|3|4|5')
t = Calculator(array)
print(t.sum())
