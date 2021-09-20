# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import calendar


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# # Getting input / printing input # #

# var1 = "Simone"
# print(var1)
# var1 = input("Inserisci un nuovo nome\n")
# print(var1)


# # lists and tuples
# Main differences: lists are mutable, vector-ish; tuples are "read-only"-ish obj
# list = []; tuple = ()

list1 = []
list1.insert(0, "1")
print(list1.pop(0))

tuple1 = (1, 2, 4)
print(tuple1)

# # Dictionaries
# Hash table-ish obj; key can by any type
# dict = {}

dict1 = {"one": "Object value for key: 'one'"}
print(dict1["one"])
dict1["two"] = "Object value for key: 'two'"
print(dict1["two"])
dict1[1] = "Object value for key: 1"
print(dict1[1])
print(dict1)
print(dict1.keys())
print(dict1.values())


# # Class in python
class Animal:
    # here there are the 'public' attr
    friendly = ''
    domestic = ''
    __name = "NO_NAME"

    __private_attr1 = "I'm private"
    _protected_attr1 = "i'm protected"

    def __init__(self, gender="male", friendly=0, domestic=0):
        # Protected member, cannot be accessed directly
        self.__gender = gender
        self.friendly = friendly
        self.domestic = domestic

    # A sample method
    def print_info(self):
        print("\nAnimal info")
        if self.friendly:
            print("I'm friendly")
        else:
            print("I'm not friendly")
        if self.domestic:
            print("I'm domestic")
        else:
            print("I'm not domestic")
        print("My name is: " + self.__name)
        print("I'm a " + self.__gender)
        print("Private attr: " + self.__private_attr1)
        print("Protected attr: " + self._protected_attr1)

    def set_gender(self, gender):
        if gender == 'm':
            self.__gender = "male"
        if gender == 'f':
            self.__gender = "female"
        else:
            print("Incorrect choice: please insert 'm' or 'f'")

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


dog = Animal()
print("\nDog instance with default value")
dog.print_info()

dog.domestic = 1
dog.friendly = 1
dog.set_gender('f')
dog.set_name("Laila")

print("\nDog instance with updated value")
dog.print_info()


class Mammal(Animal):
    def __init__(self):
        Animal.__init__(self, "male", 1, 1)
        self.set_name("Curious Dolph")

        # Accessing protected members is ok
        self._protected_attr1 = "New protected attr1"

        # Accessing private members is NOT ok
        # This would launch an error
        # print(self.__gender)


dolphin = Mammal()
dolphin.print_info()


# # String in python

string1 = "Hello world"
print(string1)
print(string1[0])  # print the 0° elem of string
print(string1[6:])  # print from 6° elem of string
print(string1[:5])  # print until 5° elem of string

print(string1)
string2 = string1.replace("world", "Simone")
print(string2)
name = "Simone"
height = float(1.83)
print("My name is %s and height is %.2f!" % (name, height))
