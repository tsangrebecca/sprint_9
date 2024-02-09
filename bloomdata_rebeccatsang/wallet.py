# create a class
# MUST HAVE def __init__(self, xxx): line
# MUST HAVE self in all the parameters

class Wallet:
    
    # first thing to run when we make a new class!
    # outline required user-provided input values here
    # parameters with default values aka =0 assigned are OPTIONAL, but
    #   if a value is passed through then it'll show in the balance
    def __init__(self, initial_amount=0):
        # save the user-provided initial amount as an attribute
        # self refers to whatever object I'm working with, 
        #   it's automatic with Python
        self.balance = initial_amount

    # spend cash METHOD
    def spend_cash(self, amount):
        if self.balance < amount:
            return "Not enough money"
        else:
            self.balance = self.balance - amount
            return f"remaining balance: {self.balance}"

    def add_cash(self, amount):
        self.balance = self.balance + amount
        return f"New balance of: {self.balance}"
    
    # __repr__ method
    # changes how the "object" looks when it's printed out so we don't get
    #   the memory address of a bunch of weird numbers
    # the presence of the "self" keyword allows me to access or modify
    #   class attributes within this function
    def __repr__(self):
        return f"Wallet with balance of: ${self.balance}"

if __name__ == '__main__':
    wallet1 = Wallet(100)
    print(wallet1)
    # on Git Bash it returns <__main__.Wallet object at 0x0000023ECBD21EB0>
    #   which means the object has been created. It's just a memory address
    print(wallet1.balance) # an attribute, the variable stored in the class

    print(wallet1.spend_cash(120))
    print(wallet1.spend_cash(60))
    
    print(wallet1.add_cash(60))
    print(wallet1.spend_cash(180))
    print(wallet1.balance)

    wallet2 = Wallet(50) # new object, different from wallet1
    wallet3 = Wallet(3000) # new object
    print(wallet1, wallet2, wallet3)

    wallet4 = Wallet() # ok to not have a value because we made it optional
    print(wallet4.balance)  # so the balance will printed as 0