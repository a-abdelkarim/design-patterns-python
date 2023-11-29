class Arabian:
	"""Arabic speaker"""
	def __init__(self):
		self.name = "Arabian"

	def speak_arabic(self):
		return "Ahlan!"

class British:
	"""English speaker"""
	def __init__(self):
		self.name = "British"	

	#Note the different method name here!
	def speak_english(self):
		return "Hello!"	

class Adapter:
	"""This changes the generic method name to individualized method names"""

	def __init__(self, object, **adapted_method):
		"""Change the name of the method"""
		self._object = object

		#Add a new dictionary item that establishes the mapping between the generic method name: speak() and the concrete method
		#For example, speak() will be translated to speak_arabian() if the mapping says so
		self.__dict__.update(adapted_method)

	def __getattr__(self, attr):
		"""Simply return the rest of attributes!"""
		return getattr(self._object, attr)


if __name__ == '__main__':	
	#List to store speaker objects
	objects = []

	#Create a Arabian object
	arabian = Arabian()

	#Create a British object
	british = British()

	#Append the objects to the objects list
	objects.append(Adapter(arabian, speak=arabian.speak_arabic))
	objects.append(Adapter(british, speak=british.speak_english))

	for obj in objects:
		print("{} says '{}'\n".format(obj.name, obj.speak()))
