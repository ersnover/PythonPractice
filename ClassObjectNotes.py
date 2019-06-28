#classes and objects
#class Car:                  #convention is capital letters for class name
#    def __init__(self):     #__init__() function (self refers to object) constructor/initializer
#        self.make = ""      
#        self.model = ""
#        self.color = ""

 #   def drive(self):        #self says that function will be available to objects of class Car
 #       print("driving the car")

class Car:                  
    def __init__(self, make, model):     #can pass in attributes during initialization::::ALWAYS pass in attributes needed to create the object (SSN, Make/Model, general intrinsic characteristics)
        self.make = make      
        self.model = model
        self.color = ""

    def drive(self):        #self says that function will be available to objects of class Car
        print("driving the car")

car = Car("Honda", "Accord")                 #must specify attributes during object initialization

#create an object of the car class
car = Car()   #Car() calls initializer for new object
car.make = "BMW"
car.model = "Series 3"
car.color = "White"

car2 = Car()
car2.make = "Honda"
car2.model = "Accord"
car2.color = "Black"

cars = []           #create array to hold multiple objects
cars.append(car)
cars.append(car2)

Beamer = cars[0]    #saves object from array to specific variable

#drive the car
car.drive()
class Address:
    def __init__(self, street, city, state, zipCode,):
        self.street = street
        self.city = city
        self.state = state
        self.zipCode = zipCode

class BankAccount:
    def __init__(self, first_name, last_name, middle_name, address, account_type):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.address = address
        self.account_type = account_type
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

#create the address object
address = Address("1200 Richmond Ave", "Houston", "TX", "77025")

bank_account = BankAccount("John", "Doe", "JB", address, "Checking")

city = bank_account.address.city

bank_account.deposit(50)            #call deposit function (available to all objects with class == BankAccount)

savings_account = BankAccount("John", "Doe", "JB", address, "savings")  #create second bank account with account_type = savings

savings_account.deposit(500)

print(bank_account.balance)         #will print 50
print(savings_account.balance)      #will print 500


class Person:                           #class names should always start with a capital letter
    def __init__(self, name, age, address):
        self.name = name                #variable names should never start with capital letter
        self.age = age
        self.addresses = []             #create array to handle multiple possible addersses

    def add_address(self, address):
        self.addresses.append(address)

person = Person("John", "Doe",34)
address = Address("c","s","ee","aaaaa")     #calls previously defined Address class
person.add_address(address)

for address in person.addresses:
    print(address)

#Put classes in different file, import from ClassFile
#Same as with functions