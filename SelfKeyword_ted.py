

class Person:
	def __init__(self):
		print("Address of person = ",id(self))
		self.person_age = 324

	def set_name(self, name):
		self.person_name = name

	def set_age(self, age ):
		self.person_age = age

	# Error: get_age() takes 0 positional arguments but 1 was given
	# def get_age():
	# 	return self.ted_age

	def get_age(self):
		return self.person_age

	def get_name(self):
		return self.person_name

	def print_person():
		print("I'm " + self.get_name() + ". I'm" + self.get_age() + " years old.")

objTed = Person()
objOliver = Person()
print("Address of Ted object = ",id(objTed))
# *** notice that print("Address of Ted = ",id(self)) and print("Address of Ted object = ",id(obj))
# both print the same value!

print("Ted age: ",objTed.get_age())

# this fails because print_ted() doesn't have the self keyword
# every function with the self keyword gains an implicit parameter which allows self (the instanced object, AKA objTed) to be passed into the function 
# when using the '.' operator. Example: objTed.get_age(), its clear we're passing no params, but under the hood its something like: objTed.get_age(address_of(objTed))

# This happens so the code (functions) in a class isn't replicated under the hood for each instance of the class.
# In the case of the Ted class, we could create 10,000 instances of Ted but under the hood, somewhere in the python interpreter there is only
# one copy of the code for get_age(). when we call get_age() for those 10,000 instances, we're simply doing something like: objTed.get_age(address_of(objTed))
# now get_age knows it can use the same code, but use the implicit parameter as the 'self' keyword in the function's code. See get_age(), self.ted_age is asking
# the code for the age of the Ted instance passed in.

# Error: print_ted() takes 0 positional arguments but 1 was given
# obj.print_ted()

# this works because we're directly accessing the function through the non-instanced class Ted

objTed.set_age(13)
objOliver.set_age(20)
objTed.print_person()
print("Ted age: ",objTed.get_age())