"""
Scenario:
You have a pets shop, your were selling only dogs now you will sell cats too.
"""

from abc import ABC, abstractmethod

class Pet:
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
    

class Cat(Pet):
    """Simple Cat class"""
    
    def speak(self) -> str:
        return "Meow!"
    

def get_pet(pet="dog"):
    pets = dict(
        dog = Dog("Hope"),
        cat = Cat("Losi")
    )
    
    return pets[pet]


if __name__ == '__main__':
    d = get_pet("dog")
    print(d.speak()) # output: Woof!
    
    c = get_pet("cat")
    print(c.speak()) # output: Meow!