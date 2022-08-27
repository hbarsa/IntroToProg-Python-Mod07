# ------------------------------------------------- #
# Title: Assignment 07
# Description: A demonstration of pickling and structured error handling
# ChangeLog: (Who, When, What)
# Hbarsa,8.26.2022,Created Script
# ------------------------------------------------- #
import pickle   #built into Python standard library

# Data -------------------------------------------- #
example_number = None
example_string = ""
example_tuple = ()
example_list = []
example_dictionary = {}
new_string = ""

# Processing -------------------------------------- #
class example_class:    #make a class with different data types
    example_number = 1
    example_string = "Haley"
    example_tuple = (1,2,3)
    example_list = [1,2,3]
    example_dictionary = {"1":"eat", "2":"a", "3":"pickle"}

class NewNumberError(Exception):
    """  Error message for entering the same number  """
    def __str__(self):
        return 'You entered the same number. Please enter a different number.'

# Presentation ------------------------------------ #
my_object = example_class() #make an instance of the object
print("This is my object...")
print("Number:", my_object.example_number)
print("String:",my_object.example_string)
print("Tuple:",my_object.example_tuple)
print("List:",my_object.example_list)
print("Dictionary:",my_object.example_dictionary, "\n")

my_pickled_object = pickle.dumps(my_object) #pickle the instance
print("This is my pickled object (in a byte string)...")
print(my_pickled_object, "\n")

try:    #enter new data
    new_number = float(input("Insert a different number:"))
    print("")
    if float(new_number) == float(my_object.example_number):
        raise NewNumberError()
except ValueError as e:
    print("You entered non-numeric characters. Please enter a number.")

my_object.example_number = new_number  # change object properties

my_unpickled_object = pickle.loads(my_pickled_object) #unpickle back to Python object
print("This is my pickled object unpickled...") #test if pickle is a true copy
print("Number:", my_unpickled_object.example_number,"<-- The Number Stayed the Same") #maintains the state of the object when you pickled it
print("String:", my_unpickled_object.example_string)
print("Tuple:", my_unpickled_object.example_tuple)
print("List:", my_unpickled_object.example_list)
print("Dictionary:", my_unpickled_object.example_dictionary,"<-- Note the data type was preserved through pickling","\n")

print("This is my object that was not pickled...")
print("Number:", my_object.example_number,"<-- The Number Changed") #the state of the object is changed
print("String:", my_object.example_string)
print("Tuple:", my_object.example_tuple)
print("List:", my_object.example_list)
print("Dictionary:", my_object.example_dictionary, "\n")