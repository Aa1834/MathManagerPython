class mathmanager:

	def add(self, a, b):
			return a+b

	def subtract(self, a, b):
			return a-b

	def multiply(self, a, b):
			return a*b

	def interest (self,a,b):
		if a == 3.8:
			return 1.038^12 * b
		else:
			return 3.6 * b
	def degree (self,grade):
		grade = [] 
		total = 0
		for i in grade:
			total = total + grade[i] 
		classification = total/grade.length
		return classification 
		
