#Basic List List
List = [1, 2,  3, "ABC", 2.3]
print(List)

# Creating a List with
# the use of multiple values
List = ["Python", "For", "Beginners"]
print("\nList containing multiple values: ")
print(List)

# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List2 = [['Python', 'For'], ['Beginners']]
print("\nMulti-Dimensional List: ")
print(List2)

# accessing a element from the
# list using index number
print("Accessing element from the list")
print(List[0])
print(List[2])

# accessing a element using
# negative indexing
print("Accessing element using negative indexing")

# print the last element of list
print(List[-1])

# print the third last element of list
print(List[-3])


## Dictionary
my_dict = {'name': 'Alice', 'age': 25}
print(my_dict['name'])
my_dict['age'] = 26
print(my_dict['age'])

##
# Creating a Dictionary
Dict = {'Name': 'alice', 1: [1, 2, 3, 4]}
print("Creating Dictionary: ")
print(Dict)

# accessing a element using key
print("Accessing a element using key:")
print(Dict['Name'])

# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(1))

# creation using Dictionary comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)

# Tuples
# Creating a Tuple with
# the use of Strings
Tuple = ('Python', 'For')
print("\nTuple with the use of String: ")
print(Tuple)

# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
Tuple = tuple(list1)

# Accessing element using indexing
print("First element of tuple")
print(Tuple[0])

# Accessing element from last
# negative indexing
print("\nLast element of tuple")
print(Tuple[-1])

print("\nThird last element of tuple")
print(Tuple[-3])

#sets
# Creating a Set with
# a mixed type of values
# (Having numbers and strings)
Set = (1, 2, 'python', 4, 'For', 6, 'beginners')
print("\nSet with the use of Mixed Values")
print(Set)

# Accessing element using
# for loop
print("\nElements of set: ")
for i in Set:
    print(i, end =" ")
print()

# Checking the element
# using in keyword
print("python" in Set)
