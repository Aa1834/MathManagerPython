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
	def degree (self,grade1,grade2,grade3,grade4,grade5,grade6): 
		total = (grade1+grade2+grade3+grade4+grade5+grade6)/6
		if total >= 70:
			print("first")
		elif total >60:
			print("2:1")
		elif total > 50:
			print("2:2")
		else:
			print("3rd class")
		
