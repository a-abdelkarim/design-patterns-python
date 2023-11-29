"""
Scenario: We have a method returns "Hello, World!" and we need to create a decorator to 
override the returned string of this function to make some style for example add <b></b> tag 
to make the string BOLD 
"""

from functools import wraps


def make_bold(function):
    """Defines the decorator"""
    
    #This makes the decorator transparent in terms of its name and docstring
    @wraps(function)
    def decorator():
        ret = function()

        return "<b>" + ret + "</b>"

    return decorator


@make_bold
def hello_world():
    return "Hello, World!"


if __name__ == '__main__':
    print(hello_world())