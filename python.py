  
# Python

'''
This is also an example of a multi-line comment
'''


'''
Basic Stuff
'''

# In terminal, 'python' starts interpreter



'''
Naming conventions
'''

# Variables should be snake_case

# Constants should be UPPER_CASE

# Methods should be snake_case







'''
I/O Commands
'''

# Print to screen with print()
print('hello')

# Get user input with input(optional_prompt=None)
user_input = input('Input something!')






'''
Basic Data Types
'''

# Python is dynamically typed! :dance:
# Type hinting was included in Python 3.5, but is not required

### Numbers ###

# Numeric conversions
int(4.5)    # >>> 4, through truncating. floor() and ceil() also convet to int
long(x)     # converts to long type
float(3)    # >>> 3.0


# Python supports +=, -=, *=, /=, //=, and **=
# It does not support ++, --, etc. :(
i = 1
i += 1
print(i)
# >>> 2

# Useful numeric and math functions
3 // 2          # >>> 1. // instead of / returns a floored quotient
abs(-2)         # >>> 2
complex(re, im) # a complex number with real parts re and imaginary part im. im defaults to 0
c.conjugate     # conjugate of the complex number c
pow(3, 2)       # >>> 9, or x to the y
3 ** 2          # >>> 9, shorthand of pow()



### Strings ###

# Strings in Python in immutable

# Strings can be defined with 'single' or "double" quotes

# String conversion
str(5)      # >>> '5'

# Concatenation
# plus (+) and .join() work
# + is slower! .join is the prefered and optimized method
'this' + 'is' + 'a' + 'string'
''.join(['this', 'is', 'a', 'faster', 'string'])

# Formatting
# Formatting can be done with plus (+), .format(), or f-strings
# f-strings are the most readable and apparntly most efficient!
print('i am formatting a string')
print('i have {0} apples and {1} chips'.format(5, 2.3))

cookie_count, gallons_of_milk = 2, 5
print(f'i have {cookie_count} cookies and {gallons_of_milk} gallons of milk!')


# Escape characters
'\''    # Single quote
'\\'    # Backslash
'\n'    # New line
'\r'    # Carriage return
'\t'    # Tab
'\b'    # Backspace
'\f'    # Form feed
'\ooo'  # Octal value
'\xhh'  # Hex value

# Other common and useful string methods (all of these return a NEW string!)
'word'.capitalize()     # >>> Word
'WORD'.lower()          # >>> word
'word'.upper()          # >>> WORD
'my word'.title()       # >>> My Word
'yes.'.endswith('.')    # >>> True
'abcd'.find('b')        # >>> 1, but -1 if not found
'abcd'.index('c')       # >>> 2, but raises ValueError if not found
'123abc'.isalnum()      # >>> True; true if all characters in string are alphanumeric
'123abc'.isalpha()      # >>> False; true if all characters in string all alpha
'123'.isnumeric()       # >>> True; true if all characters in string are numeric
'ABC'.isupper()         # >>> True
'this string'.split()   # >>> ['this', 'string']



### Booleans ###
# Python uses True and False. Make sure those names are capitalized
my_bool = True
my_false_bool = False



### Nothing ###

# the nothing value is denoated with 'None', like null or nil

# None, False, 0, and an empty string will all evaluate to None











'''
Collections: Lists, Typles, Set, Dictionary
'''

'''
Type        | Ordered?  | Mutable?  | Accessor  | Duplicates allowed?
List        | Yes       | Yes       | Index     | Yes
Tuple       | Yes       | No        | Index     | Yes
Set         | No        | Yes       | Key       | No
Dictionary  | No        | Yes       | Key       | No
'''

### Lists ###
# Ordered, mutable collection. Length is dynamic, like an ArrayList (Java) or Vector (C++)

# Create a list with [square brackets] or with list()
my_list = []
my_list = [1, 2, 3]
my_list = list()
my_list = list((1, 2, 3))   # Note the ((double round brackets!))

# Accessing lists is standard. Negative indicies return elements from the end
my_list[0]      # >>> 1
my_list[-1]     # >>> 3
my_list[0:2]    # >>> [1, 2]; first value is inclusive, second is not
my_list[:2]     # >>> [1, 2]
my_list[2:]     # >>> [3]

# Check if item is in list:
2 in my_list    # >>> True; 2 is in my_list

# len() returns length
len(my_list)    # >>> 3

# List can function as a stack, where append and pop are push and pop
my_list.append(16)  # >>> [1, 2, 3, 16]; inserts at end of list
my_list.pop()       # >>> [16]; list is now [1, 2, 3]

# Insert at a specified location with insert()
my_list.insert(0, 10)   # >>> [10, 1, 2, 3]

# Remove at a specified location with remove()
my_list.remove(0)       # >>> [1, 2, 3]

# del keyword can delete a specific element or the entire list

# clear() empties the list
my_list.clear()     # >>> []



## Copying lists

# Lists are REFERENCES in Python!
list1 = [1, 2, 3]
list2 = list1
list2.append[4]
print(f'list1: {list1}, liste2: {list2}')
# >>> list1: [1, 2, 3, 4], list2: [1, 2, 3, 4]

# Instead, use .copy()
list1 = [1, 2, 3]
list2 = list1.copy()
list2.append(4)
print(f'list1: {list1}, liste2: {list2}')
# >>> list1: [1, 2, 3], list2: [1, 2, 3, 4]

# Using the list() method also works:
list1 = [1, 2, 3]
list2 = list(list1)
list2.append(4)
print(f'list1: {list1}, liste2: {list2}')
# >>> list1: [1, 2, 3], list2: [1, 2, 3, 4]



## List concatenation
# plus (+), .append(), and .extend() all work
# .extend() is the preferred method if adding multiple elements
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list1.extend(list2)     # >>> ['a', 'b', 'c', 1, 2, 3]


## Sorting
# .sort() sorts in place (mutable), while sorted() returns a new sorted list (immutable)
list1 = [5, 1, 10]
sorted(list1)       # >>> [1, 5, 10]; list1 is unchanged
list1.sort()        # >>> [1, 5, 10]; list1 is now sorted




## List Comprehension
# List comprehension is a readable, efficient, and pythonic way of making lists

# Syntax is this:
new_list = [expression for element in list() if optional_conditions]

# For example, find the squares of a number:
numbers = [1, 2, 3, 4]
squares = []

for n in numbers:
    squares.append(n**2)

# >>> [1, 4, 9, 16]

# With list comprehension, it would look like this:
squares = [n**2 for n in numbers]
# >>> [1, 4, 9, 16]




### Tuples ###
# Ordered, immutable collection. Written with round brackets
# Tuples have the same indexing properties as lists, but no modification methods because they are immutable

# Create a tuple with () or the tuple() constructor
my_tuple = ()
my_tupe = (1, 2, 3)
my_tuple = tuple()
my_tuple = tuple(1, 2, 3)

# Unpacking tuples
# Although tuple elements can be accessed with an index, they can also be unpacked like this:
first, second, third = my_tuple

# first => 1
# second => 2
# third => 3



### Sets ###
# Unordered and unindexed collection. Written with curley brackets. Similar to hash set
# All values are unique

# Create a set with {} or set()
my_set = {'1', '2', '3'}
my_set = set()
my_set = set([1, 2, 3])

# To add an element to a set, call .add()
my_set.add('4')     # >>> {'1', '2', '3', '4'}

# To add multiple elements, call .update()
my_set.update(['5', '6'])   # >>> {'1', '2', '3', '4', '5', '6'}

# .remove() and .discard() will both remove an item
# if the item does not exist, .remove() will raise an error
my_set.remove('7')  # KeyError is raised
my_set.discard('7') # nothing happens

# Join two sets with .union() or .update()
# .union() will return a new set, while .update() modifies the first set
# Duplicate items will be excluded
new_set = my_set.union({'8', '9'})

# Other useful set methods:
my_set.clear()      # clears set to a new empty set
del my_set          # deletes the set entirely
my_set.pop()        # removes AN element (not ordered, so probs don't do this)
5 in my_set         # returns if 5 is a key in my_set
my_set.difference(another_set)  # returns a new set contain the difference between two or more sets
my_set.difference_update(another_set)   # removes the items in my_set that are included in another_set
my_set.intersection(another_set)   # returns a set of elements that are common between my_set and another_set
my_set.isdisjoint(another_set)  # returns whether two sets have an intersection or not
my_set.issubset(another_set)    # returns whether another_set contains my_set
my_set.issuperset(another_set)  # returns whether my_set contains another_set




### Dictionaries ###
# Unordered and mutable. Like a hash, hash table, or hash map. A set of key-value pairs.
# All keys are unique

# Create a dictionary with {curly braces} the dict() constructor
my_dict = {}
my_dict = {'key1': 1, 'key2': 2}
my_dict = dict()
my_dict = dict(key1=1, key2=2)


# Access elements with a [key] in square brackets
my_dict['key1']     # >>> 1

# Looping through a dictionary returns a list of keys
for key in my_dict:
    print(key)
# >>> 'key1'
# >>> 'key2'

# .values() returns a list of values
for value in my_dict.values():
    print(value)
# >>> 1
# >>> 2

# .items() returns a list of tuple(key, item)
for key, value in my_dict.items():
    print(f'{key}: {value}')
# >>> 'key1': 1
# >>> 'key2': 2


# Check if a key exists in a dictionary with 'in'
'key1' in my_dict   # >>> True
'key5' in my_dict   # >>> False

# len() returns the number of items in a dictionary
len(my_dict)        # >>> 2


# Add an item by using a new index key and assigning a value
my_dict['key3'] = 3
# If the key already exists, the value will be overridden


# Remove an item from a dictionary with pop(key), popitem(), or del
my_dict.pop('key3')
del my_dict['key3']
my_dict.popitem()   # Removes a random item because dictionaries are unordered

# Remove all items with clear()
my_dict.clear()

# Like lists, dictionaries must be copied with .copy() or constructing a new dictionary
new_dict = my_dict.copy()
new_dict = dict(my_dict)






'''
Conditionals
'''

# If statesments look like this:
if something == True:
    # something happens here
elif something == False:
    # something else happens here
else:
    # otherwise do this

# == compares equality of values
1 == 1  # True
1 == 2  # False

# >, <, >=, <= works like normal

# is checks for object equality
'string1' == 'string1'      # >>> True
'string1' is 'string1'      # >>> False
my_string = 'string1'
another_string = my_string
another_string is my_string # >>> True


# Python does not have case / switch statements :(




'''
Loops
'''

## For Loops in Python are more like for-each loops in other languages
items = ['apple', 'strawberry', 'kiwi']

for fruit in items:
    print(fruit)

# For a more traditional for-loop with an index, use the range method:
# The range syntax is range(stop), range(start, stop), range(start, stop, step_size)
# By default, start and step_size are 0 and +1, respectively
# Range only creates a list, which the for loop would treat like a standard for-each-number-in-range
for index in range(1,6,2):
    print(index)

# >>> 1
# >>> 3
# >>> 5

# To iterate through both the item and index of an iterable, use the enumerate() method:
for index, item in items:
    print(f'{index}: {item}')

# >>> 'apple'
# >>> 'strawberry'
# >>> 'kiwi'






## While Loops
i = 0
while i < 5:
    # do something
    i += 1




# continue keyword moves on to the next iteration
# break exits the current loop




'''
Functions
'''

def function_name(arguments = 'default parameters'):
    # do something
    new_thing = arguments
    return new_thing

# As of Python 3.5, type-hinting is allowed, like this:
def type_hinted_function(my_int: int, my_string: str, my_default_int = 0: int) -> bool:
    return True





'''
DECORATORS 

Decorators are functions that take another function as an argument, enabling
consistent pre- and post-processing of a function
'''
def decorator(function):
    print('Decorator called')

    def wrapper(*args, **kwargs):
        # Pre-processing happens here
        print('Doing some stuff before calling the function')

        # Calling the function argument actually runs the function that is being deocorated
        function()

        # Post-processing happens here
        print('Doing some stuff after calling the function')

    return wrapper

# This is a decorator in use:
@decorator
def hello_world():
    print('Hello world!')

# output:
# >>> Doing some stuff before calling the function
# >>> Hello world!
# >>> Doing some stuff after calling the function