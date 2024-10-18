1. Lists
Overview
Lists are mutable sequences in Python, meaning they can be modified after their creation. They can hold a variety of data types, including integers, floats, strings, and even other lists.
Example Code
python
Copy code
# Creating a list with different data types
List = [1, 2, 3, "ABC", 2.3]
print(List)  # Output: [1, 2, 3, "ABC", 2.3]

# Creating a list containing multiple string values
List = ["Python", "For", "Beginners"]
print("\nList containing multiple values: ")
print(List)  # Output: ['Python', 'For', 'Beginners']

# Creating a multi-dimensional list (a list of lists)
List2 = [['Python', 'For'], ['Beginners']]
print("\nMulti-Dimensional List: ")
print(List2)  # Output: [['Python', 'For'], ['Beginners']]
Key Points
Lists can contain mixed data types.
They can be accessed using indexing (both positive and negative).
Lists can also be nested, creating multi-dimensional lists.
2. Dictionaries
Overview
Dictionaries are mutable, unordered collections of key-value pairs. Each key is unique, and you can access values quickly using their keys.
Example Code
python
Copy code
# Creating a dictionary with key-value pairs
my_dict = {'name': 'Alice', 'age': 25}
print(my_dict['name'])  # Output: Alice

# Updating the value associated with the key 'age'
my_dict['age'] = 26
print(my_dict['age'])  # Output: 26

# Creating another dictionary with mixed key types
Dict = {'Name': 'alice', 1: [1, 2, 3, 4]}
print("Creating Dictionary: ")
print(Dict)  # Output: {'Name': 'alice', 1: [1, 2, 3, 4]}
Key Points
You can update dictionary values easily.
Keys can be of various immutable types, while values can be of any type.
Dictionaries provide efficient data retrieval.
3. Tuples
Overview
Tuples are immutable sequences in Python. Once created, their elements cannot be changed. They can hold items of different data types.
Example Code
python
Copy code
# Creating a tuple with strings
Tuple = ('Python', 'For')
print("\nTuple with the use of String: ")
print(Tuple)  # Output: ('Python', 'For')

# Creating a tuple using a list
list1 = [1, 2, 4, 5, 6]
Tuple = tuple(list1)
print("\nTuple using List: ")
print(Tuple)  # Output: (1, 2, 4, 5, 6)
Key Points
Tuples support indexing similar to lists but cannot be modified.
They can be used to store a collection of items that should not change.
4. Sets
Overview
Sets are unordered collections of unique items. They automatically remove duplicates and are useful for membership testing.
Example Code
python
Copy code
# Creating a set with mixed types of values
Set = {1, 2, 'python', 4, 'For', 6, 'beginners'}
print("\nSet with the use of Mixed Values")
print(Set)  # Output: {1, 2, 4, 6, 'python', 'For', 'beginners'}
Key Points
Sets do not support indexing or slicing.
You can use the in keyword to check for membership in a set.
5. List Comprehensions
Overview
List comprehensions provide a concise way to create lists. They can include conditions and are generally more readable than traditional for loops.
Example Code
python
Copy code
# Creating a list of squares for numbers from 0 to 4
squares = [x**2 for x in range(5)]
print("Squares:", squares)  # Output: [0, 1, 4, 9, 16]

# Creating a list of even numbers from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]
print("Even Numbers:", evens)  # Output: [0, 2, 4, 6, 8]
Key Points
List comprehensions can simplify the syntax for generating lists.
You can include conditions to filter elements.
6. Dictionary Comprehensions
Overview
Dictionary comprehensions allow for the creation of dictionaries in a concise way, similar to list comprehensions.
Example Code
python
Copy code
# Creating a dictionary mapping numbers to their squares
squares_dict = {x: x**2 for x in range(5)}
print("Squares Dictionary:", squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
Key Points
Dictionary comprehensions provide a compact way to create dictionaries.
Conditions can also be applied to filter keys and values.
