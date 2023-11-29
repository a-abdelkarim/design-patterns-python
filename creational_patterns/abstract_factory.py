from abc import ABC, abstractmethod

class Pet(ABC):
    """Simple Animal class"""
    
    def __init__(self, name) -> None:
        self._name = name
        
    @abstractmethod
    def speak(self) -> str:
        pass


class Dog(Pet):
    """Simple Dog class"""
        
    def speak(self) -> str:
        return "Woof!"
    
    def __str__(self) -> str:
          return "Dog"
    

class Cat(Pet):
    """Simple Cat class"""
    
    def speak(self) -> str:
        return "Meow!"
    
    def __str__(self) -> str:
          return "Cat"
    

class DogFactory:
    """Concrete Dog Factory"""
    def get_pet(self) -> object:
        return Dog("Hope")

    def get_food(self):
        """Returns a Dog Food object"""
        return "Dog Food!"


class CatFactory:
    """Concrete Cat Factory"""

    def get_pet(self) -> object:
        return Cat("Losi")

    def get_food(self):
        """Returns a Dog Food object"""
        return "Cat Food!"

class PetStore:
	""" PetStore houses our Abstract Factory """

	def __init__(self, pet_factory=None):
		""" pet_factory is our Abstract Factory """

		self._pet_factory = pet_factory


	def show_pet(self):
		""" Utility method to display the details of the objects returned by the DogFactory """

		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print("Our pet is '{}'!".format(pet))
		print("Our pet says hello by '{}'".format(pet.speak()))
		print("Its food is '{}'!".format(pet_food))

if __name__ == '__main__':
    #Create a Concrete Dog Factory
    dog_factory = DogFactory()
    #Create a pet store housing our Abstract Factory
    shop = PetStore(dog_factory)
    #Invoke the utility method to show the details of our pet
    shop.show_pet()
    
    #Create a Concrete Cat Factory
    cat_factory = CatFactory()
    #Create a pet store housing our Abstract Factory
    shop = PetStore(cat_factory)
    #Invoke the utility method to show the details of our pet
    shop.show_pet()
