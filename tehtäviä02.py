#LUOKKO

""" class Computer:
    def __init__(self, mobile, model, OS) -> None:
        self.mobile = mobile
        self.model = model
        self.OS = OS

    def portable(self):
        if self.mobile == 'laptop':
            print(f"A {self.mobile} is easy to take away")
        elif self.mobile == 'PC':
            print(f"A {self.mobile} is fixed and hard to transport")

pc1 = Computer("PC", "Asus", "windows")
pc1.portable()
            
pc2 = Computer("laptop", "Samsung", "Linux")
pc2.portable()
 """
# Task OOP-01
# Program your own class and objects
# Person class with name, age
# personstats()
# personsays(arg)
# Create 2 persons

""" class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def personstats(self):
        print(f"{self.name} is {self.age} years old")

    def personsays(self, message):
        print(f"{self.name} says: '{message}'")

person1 = Person("Albert", 20)
person1.personstats()
person1.personsays("My name is not Albert")

person2 = Person("Bernard", 55)
person2.personstats()
person2.personsays("I don't say anything") """

# Task OOP-02
# change previous solution as follows:
# add class variable number
# its value is increased by 1 whenever new
# person is added
# print how many persons you have created
# i.e. how many Person objects you have

""" class Person:
    number = 0
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        Person.number+=1

    def personstats(self):
        print(f"{self.name} is {self.age} years old")

    def personsays(self, message):
        print(f"{self.name} says: '{message}'")

print(Person.number)
person1 = Person("Albert", 20)
print(Person.number)
person2 = Person("Bernard", 55)
print(Person.number) """

# Task OOP-03
# create class PersonToo
# without default constructor
# attributes are name and age
# methods are personstats() and personsays(arg)

""" class PersonToo:
    name = ''
    age = 1

    def personstats(self):
        print(f"{self.name} is {self.age} years old")

    def personsays(self, message):
        print(f"{self.name} says: '{message}'")

person1 = PersonToo()
person1.name = 'Conrad'
person1.age = 33
person1.personstats()
person1.personsays("My name is not Albert")

person2 = PersonToo()
person2.name = 'David'
person2.age = 44
person2.personstats()
person2.personsays("My name is not Albert")
 """
# Task OOP-04
# Use class functions and find out following...
# 1) Value of age in both persons.
# 2) Is qwerty a object variable?
# 3) Delete age of one of the persons.

""" print(person1.age)
print(getattr(person1,"age"))

print(hasattr(person2,"qwerty"))

print(person1.age)
delattr(person1, "age")
print(hasattr(person1,"age"))
print(person1.age) """

# Task OOP-005
# afternoon's programming task.
# create a class BankAccount for accounts
# with attributes: 
#   name (string), 
#   saldo (float), 
#   id (int)
# with methods: 
#   changebalance(float) for X amount withdrawal/accumulation
#   accountinfo() that describes account info
# Then add all account objects to a list named accountlist.

# Next create a following bank interface to test out your class and list:
#
# MY BANK
# 1: Add account
# 2: Show account info for one account
# 3: Show account info for all accounts
# 0: Quit banking program

class BankAccount:
    def __init__(self, name: str, saldo: float, id: int) -> None:
        self.name = name
        self.saldo = saldo
        self.id = id

    def changebalance(self, amount):
        if amount < 0:
            print(f"\n{self.name.upper()} your new balance is {self.saldo} - {abs(amount)} = {self.saldo+amount} €")
        elif amount >=0:
            print(f"\n{self.name.upper()} your new balance is {self.saldo} + {amount} = {self.saldo+amount} €")
        self.saldo = self.saldo + amount

    def accountinfo(self):
        print(f"\n{(self.name).upper()}, your account ID {self.id} has a balance of {self.saldo} € ")

accountlist = []
testi_account1 = BankAccount('testi1', 10000, 123456)
accountlist.append(testi_account1)
testi_account2 = BankAccount('testi2', 30000, 987654)
accountlist.append(testi_account2)

def addaccount():
    name = input("Account name?: ")
    saldo = float(input("Account balance?: "))
    id = int(input("Account id?: "))
    account = BankAccount(name, saldo, id)
    print(type(account))
    accountlist.append(account)

def show_one_account():
    print("What account do you want to search?\nAccount list:\n")
    for account in accountlist:
        print('-',account.name)
    account_name = input("\nAccount name?: ")
    #name_list = [x.name for x in accountlist]
    #if account_name in name_list:
    found = False
    for account in accountlist:
            if account.name == account_name:
                found = True
                account.accountinfo()
    if found == False:
        print("\nERROR -- Account not found -- ")

def showaccountall():
    for account in accountlist:
        account.accountinfo()

def deposit():
    print("Please select an account: ")
    for account in accountlist:
        print('-',account.name)
    account_name = input("\nAccount name?: ")
    #name_list = [x.name for x in accountlist]
    found_account = False
    for account in accountlist:
        if account.name == account_name:
            found_account = True
            account_id = int(input("What is your acc ID?: "))
            if account_id == account.id:
                sum = int(input("Sum to desposit: "))
                account.changebalance(sum)
            else:
                print("\nWrong ID")
    if found_account == False:
        print("\nERROR -- Account not found -- ")


while True:
    answer = input("\nWhat do you want to do? \n1 Add account\n2 Show account info for one account\n3 Show account info for all accounts\n4 Change balance\n0 Quit banking program\n")
    if answer == '1':
        addaccount()
    elif answer == '2':
        show_one_account()
    elif answer == '3':
        showaccountall()
    elif answer == '4':
        deposit()        
    elif answer == '0':
        break
    else:
        print("\nCommand not recognised")

#name_list = [x.name for x in accountlist]
#print(name_list)