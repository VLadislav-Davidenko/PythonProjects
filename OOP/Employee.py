class Employee:
	'Common base class for all employees'
	empCount = 0

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def displayCount(self):
		print(f"Total number of Employees is {Employee.empCount}")

	def displayEmployee(self):
		print(f"Name: {self.name}\nSalary: {self.salary}")

'Creating the first object of the Employee class'
emp = Employee("Vasya", 12000)

'Calling a class Attributes'
emp.displayCount()
emp.displayEmployee()

'Adding and Modifying our attributes'
emp.age = 15  #Adding
emp.age = 27  #Modifying
print(emp.age)

'Deleting an attribute - age'
del emp.age
try:
	print(emp.age)
except AttributeError:
	print("You didn't mentione the age of the Employee")

	'GRUD Function'
	setattr(emp, 'age', 82)
	print(hasattr(emp, 'age'))
	print(getattr(emp, 'age'))
	delattr(emp, 'age')
	print(hasattr(emp, 'age'))

'Built-In Class Attribute'
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)
