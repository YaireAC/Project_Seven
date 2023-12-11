from ProjectSeven import Coffee

class CoffeeError(Coffee):
    """Represents the class for Coffee errors"""
    def __init__(self, water, milk_date, type_beans):
        super().__init__(water, milk_date, type_beans)

    def check_water(self):
        if self._water < 10:
            self._water += 20
        elif self._water > 50:
            print("Too much water. Restart")
