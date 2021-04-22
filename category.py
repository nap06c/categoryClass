class Category:

    # constructor to initialize category budget, includes category (string) and amount (number)
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
    
    # add money to category budget
    def deposit(self, amount):
        self.amount += amount
        print("You successfully deposited $%.2f to %s budget. Your new balance is $%.2f" % (amount, self.category, self.amount))

    # withdraw money from category budget
    def withdraw(self, amount):
        if (self.amount > amount):
            self.amount -= amount
            print("You successfully withdrew $%.2f from %s budget" % (amount, self.category))
            return True
        
        print("You dont have the required funds")
        return False
            

    # transfer money from one category budget to another
    def transfer(self, amount, obj):
        if(self.withdraw(amount)):
            obj.deposit(amount)
            print("You successfully transferred $%.2f from %s budget to %s budget" % (amount, self.category, obj.category))
        else:
            print("Unable to complete transfer")

    # check current balance in category budget
    def check_balance(self):
        print("Your current balance in %s budget is $%.2f" % (self.category, self.amount))


#create some example categories
car = Category("car", 100)
cell_phone = Category("cell phone", 50)
computer = Category("computer", 200)

car.check_balance()
cell_phone.check_balance()
computer.check_balance()

car.deposit(200)
car.check_balance()

computer.withdraw(50)
computer.check_balance()

computer.transfer(100, cell_phone)
computer.check_balance()
cell_phone.check_balance()
