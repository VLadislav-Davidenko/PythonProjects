class Pet:
	number_of_pets = 0

	def __init__(self, name, age):
		self.name = name
		self.age = age
		Pet.add_number()
		
	def voice(self):
		print("I do not know what to do")

	@classmethod
	def add_number(cls):
		cls.number_of_pets += 1

	@classmethod
	def get_number(cls):
		print(cls.number_of_pets)

class Cat(Pet):

	def __init__(self, name, age, colour):
		super().__init__(name, age)
		self.colour = colour

	def voice(self):
		print("Meaw")

class Dog(Pet):

	def __init__(self, name, age, sex):
		super().__init__(name, age)
		self.sex = sex

	def voice(self):
		print("Bark")

p = Pet("Tim", 12)
p.voice()
c = Cat("Bill", 10, "grey")
print(f"I am {c.colour}")
c.voice()
d = Dog("John", 23, 'M')
print(f"I am {d.sex}")
d.voice()
print("----------")
Pet.get_number()
