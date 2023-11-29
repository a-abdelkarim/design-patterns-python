import copy


class Prototype:
    
    def __init__(self) -> None:
        self._objects = {}
        
    def register_object(self, name, obj) -> None:
        """Register new object"""
        self._objects[name] = obj
        
    def unregister_object(self, name) -> None:
        """Unregister an object"""
        del self._objects[name]
        
    def clone(self, name, **attrs) -> object:
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attrs)
        return obj
    
    
class Car:
    
    def __init__(self, model, color) -> None:
        self.model = model
        self.color = color
        
    def __str__(self) -> str: 
        return f'{self.model} || {self.color}'
    

if __name__ == '__main__':
    car1: Car = Car("M1", "Black")
    
    prototype: Prototype = Prototype()
    prototype.register_object("M1", car1)
    
    car2 = prototype.clone("M1")
    print(car2) # output: M1 || Black