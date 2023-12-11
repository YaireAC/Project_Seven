# Section 1
"""A design that would complete these subclasses would be a design with coffee, class Coffee. As the generic exception to handle the object would be
CoffeeError. Raised when there are issues when coffee is sold. The subclasses for class Coffee would then be Exresso_made and Normal_made classes. Fo when the coffee is made either with a machine or normal drip.
The subclasses for the exceptions could then be water_error and milk_error. Detecting if there is too much water or the milk is spoiled.
Diagram:

                class Coffee
                /          \
             expresso     drip
                      |
                  CoffeeError
                 /       \
             water_error milk_error

The subclasses of Coffe are the type of coffee,
The subclasses for CoffeeError are milk error and milk_error
But CoffeeError is raised when there is an issue in either types. The type of issue is then raised (milk or water based)

"""

class Coffee():
    """Generic Electronics class"""
    def __init__(self, water, milk_date, type_beans):
        self._water = 0
        self._milk_date = 0
        self._type_beans = type_beans

    def displayer(self):
        print("Information of the object")
        print("Water amount: {water} Milk Date: {milk_date} Type of Beans: {type_beans")


"""Since we are working with integers for the levels of water and dates. The best type of tests that should be tested are those of input validity. Checking whether the the variables are appropriate.
As well as checking what to do in certain events. Such as, when the milk is expired, the program should do something in cause of it. Such as stating it will use new milk or creating a new milk variable. 
For water, depending on its level it would also act accordinglly. If the water level is too low then it should add to the integer. If too high then state it will remake the coffee, and set it back to zero.""" 
