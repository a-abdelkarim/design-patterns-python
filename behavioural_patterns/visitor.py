class House(object): #The class being visited 
	def accept(self, visitor):
		"""Interface to accept a visitor"""
		visitor.visit(self) #Triggers the visiting operation!

	def work_on_hvac(self, hvac_specialist):
		print(self, "worked on by", hvac_specialist) #Note that we now have a reference to the HVAC specialist object in the house object!

	def work_on_electricity(self, electrician):
		print(self, "worked on by", electrician) #Note that we now have a reference to the electrician object in the house object!

	def __str__(self):
		"""Simply return the class name when the House object is printed"""
		return self.__class__.__name__


class Visitor(object):
	"""Abstract visitor"""
	def __str__(self):
		"""Simply return the class name when the Visitor object is printed"""
		return self.__class__.__name__


class HvacSpecialist(Visitor): # Inherits from the parent class, Visitor
	"""Concrete visitor: HVAC specialist"""
	def visit(self, house):
		house.work_on_hvac(self) # Note that the visitor now has a reference to the house object


class Electrician(Visitor): # Inherits from the parent class, Visitor
	"""Concrete visitor: electrician"""
	def visit(self, house):
		house.work_on_electricity(self) # Note that the visitor now has a reference to the house object


if __name__ == '__main__':
    hv = HvacSpecialist() # Create an HVAC specialist
    e = Electrician() # Create an electrician

    home = House() # Create a house
    home.accept(hv) # Accept the HVAC specialist
    home.accept(e) # Accept the electrician

