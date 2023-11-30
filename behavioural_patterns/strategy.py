import types #Import the types module

class Strategy:
    """The Strategy Pattern class"""
    
    def __init__(self, function=None):
        self.name = "Default Strategy"
        
        if function:
            self.execute = types.MethodType(function, self)
            
    def execute(self): 
        print("{} is used!".format(self.name))

# Replacement method 1
def strategy_one(self):
    print(f"{self.name} is used to execute method 1")

# Replacement method 2    
def strategy_two(self):
	print(f"{self.name} is used to execute method 2")


if __name__ == '__main__':    
    # create our default strategy
    s0 = Strategy()
    # execute our default strategy
    s0.execute()

    # create the first variation of our default strategy by providing a new behavior
    s1 = Strategy(strategy_one)
    # set its name
    s1.name = "Strategy One"
    # execute the strategy
    s1.execute()

    s2 = Strategy(strategy_two)
    s2.name = "Strategy Two"
    s2.execute()
