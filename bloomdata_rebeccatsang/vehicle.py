"""
This file holds two classes: Vehicle and Convertible. They are a parent and child class.

"""
# move all the comments to docstrings

class Vehicle:
    """
    This is the class Vehicle docstring.
    Imagine I want to list these vehicles on Craigslist:
    "Parent" class is the more generic of the two classes.
    """

    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage
        # these are 5 new attributes

    def honk(self):
        """
        returns the sound honk
        """
        return "HOOOOOOOOOOONK!"
         
    def drive(self, miles_driven):
        """
        calculate mileage
        """
        # self.mileage = self.mileage + miles_driven
        # or write
        self.mileage += miles_driven
        return self.mileage
    

    def __repr__(self):
        """
        print the class instead of just the address that the object is stored in
        """
        return f"A {self.color} {self.year} {self.make} {self.model} with {self.mileage} miles"
    
# if __name__ == '__main__':
#     my_vehicle = Vehicle('Toyota', 'Camry', 'gray', 2015, 60000)

#     print(my_vehicle.make)
#     print(my_vehicle.mileage)
#     print(my_vehicle.honk())
#     print(my_vehicle.drive(1234))

#     print(my_vehicle) # using the __repr__ method


# Imagine I want to create another specific kind of vehicle and
#   add another method specific to that vehicle type e.g. convertible with a top:
# The more specific class is called a Child class
class Convertible(Vehicle): # Convertible class inherits from Vehicle class
    """
    This class Convertible has one extra method,
    which is to open or close the top.
    """
    def __init__(self, make, model, color,
                 year, mileage, top_down=True):
        # parameter with default value has to go at the end, whatever that is =None or =something
        # if there is no =something, it is a required parameter for that method, and we have to fill it out to avoid an error
        """
        This line creates the class inheritance copying all the parent code.
        """
        super().__init__(make, model, color, year, mileage) # took care of the 5 lines below
        # self.make = make
        # self.model = model
        # self.color = color
        # self.year = year
        # self.mileage = mileage
        # these are 5 new attributes

        # this is the only new line we need in the child class
        # convertible's top up or down?
        self.top_down = top_down  # is open


    # def honk(self):
    #     return "HOOOOOOOOOOONK!"
    
    # def drive(self, miles_driven):
    #     # self.mileage = self.mileage + miles_driven
    #     # or write
    #     self.mileage += miles_driven
    #     return self.mileage
    
    def change_top_status(self):
        """
        To toggle top open or close
        """
        if self.top_down:
            self.top_down = False
            return "Top is now up."
        else:
            self.top_down = True
            return "Top is now down!"
    
    # print the class instead of just the address that the object is stored in
    def __repr__(self):
        return f'''A {self.color} {self.year} {self.make} {self.model}
         convertible with {self.mileage} miles. Is the top open? {self.top_down}''' # multi-line f-string
    
if __name__ == '__main__':
    my_vehicle = Convertible('Toyota', 'Camry', 'gray', 2015, 60000, top_down=False)

    # print(my_vehicle.make)
    # print(my_vehicle.mileage)
    # print(my_vehicle.honk())
    # print(my_vehicle.drive(1234))

    print(my_vehicle) # using the __repr__ method

    print(my_vehicle.top_down)
    print(my_vehicle.change_top_status())
    print(my_vehicle.top_down)

    print(my_vehicle.honk())
    print(my_vehicle.drive(1234))

# ====================================================================
# Is there a way to just add that one specific method for that one specific class,
#   so we don't have to repeat the whole code block?
#   YES! It's called CLASS INHERITANCE
