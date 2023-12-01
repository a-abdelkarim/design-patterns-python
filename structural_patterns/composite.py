class Component:
	"""Abstract class"""

	def __init__(self, *args, **kwargs):
		pass

	def component_function(self):
		pass

class Child(Component): #Inherits from the abstract class, Component
	"""Concrete class"""

	def __init__(self, *args, **kwargs) -> None:
		Component.__init__(self, *args, **kwargs)

		#This is where we store the name of your child item!
		self.name: str = args[0]

	def component_function(self) -> None:
		#Print the name of your child item here!
		print("{}".format(self.name))

class Composite(Component): #Inherits from the abstract class, Component
	"""Concrete class and maintains the tree recursive structure"""

	def __init__(self, *args, **kwargs):
		Component.__init__(self, *args, **kwargs)

		#This is where we store the name of the composite object
		self.name: str = args[0]

		#This is where we keep our child items
		self.children: list = []

	def append_child(self, child) -> None:
		"""Method to add a new child item"""
		self.children.append(child)

	def remove_child(self, child) -> None:
		"""Method to remove a child item"""
		self.children.remove(child)

	def component_function(self) -> None:

		#Print the name of the composite object
		print("{}".format(self.name))

		#Iterate through the child objects and invoke their component function printing their names
		for i in self.children:
			i.component_function()


if __name__ == '__main__':
    sub1: Composite = Composite("submenu1") # Build a composite submenu 1

    sub11: Child = Child("sub_submenu 11") # Create a new child sub_submenu 11
    sub12: Child = Child("sub_submenu 12") #Create a new Child sub_submenu 12

    sub1.append_child(sub11) # Add the sub_submenu 11 to submenu 1
    sub1.append_child(sub12) # Add the sub_submenu 12 to submenu 1

    top: Composite = Composite("top_menu") # Build a top-level composite menu

    sub2: Child = Child("submenu2") # Build a submenu 2 that is not a composite

    top.append_child(sub1) # Add the composite submenu 1 to the top-level composite menu
    top.append_child(sub2) # Add the plain submenu 2 to the top-level composite menu
    top.component_function() # test if our Composite pattern works!
