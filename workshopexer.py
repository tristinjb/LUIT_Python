#!/usr/bin/env python3.7

#formats
first_name = "Mike"
surname = "Wazowski"
print("The best character in monsters inc is {}. his last name is {}".format(first_name, surname))

# f string method
firstname = "Mike"
surname = "Wazowski"
print(f"The best character in monsters inc is {firstname}. his last name is {surname}")

# using number varibables in strings
my_int = 50
sentence = "The total comes to: "
print("sentence + my_int")

my_int = 50
sentence = "The total comes to: "
print(sentence + str(my_int))

#Dictionaries
#Dictionaries can be created by assigning the key-values
user = {"first_name":"Ada"}
print(user)
{'first_name': 'Ada'}

#read
#To read the value associated with a key, you need to provide the name of the dictionary and the the value of the key inside square brackets.
user = {"first_name":"Ada"}
print(user["first_name"])
("Ada")

#update
#Dictionaries are mutable, which means they can be changed after you create them. You can add, update or delete the key-value pairs in a dictionary.
user["family_name"] = "Byron"
print(user)
{'first_name': 'Ada', 'family_name': 'Byron'}

#modify a vaule
#To modify a value in a similar way to adding it. You provide the new value after the = sign.
user["family_name"] = "Lovelace"
print(user)
{'first_name': 'Ada', 'family_name': 'Lovelace'}

#delete a key-vaule pair
#To remove a key-value pair you use the del statement with the name of the dictionary and the key you want to delete.
del user["family_name"]
print(user)
{'first_name': 'Ada'}

#List
#A list is an ordered sequence of values separated by spaces.
#Create
#Lists can be created by assigning the values you want to store in a list to a variable
fruit = ["apples","oranges","bananas"]
print(fruit)

#Read
#Objects stored in list are given an index number starting at 0. To read an element from a list you use the index number of the stored value.
fruit = ["apples","oranges","bananas"]
print(fruit[1])
len(fruit)

print(fruit[-1])

print(fruit[-2])

#update a list using append
fruit.append("kiwi")
print(fruit)
['apples', 'oranges', 'bananas', 'kiwi']

#updating a list using insert
fruit.insert(2, "passion fruit")
print(fruit)
['apples', 'oranges', 'passion fruit', 'bananas', 'kiwi']

#Organizing a list
print(sorted(fruit))
['apples', 'bananas', 'kiwi', 'oranges', 'passion fruit']
print(fruit)
['apples', 'oranges', 'passion fruit', 'bananas', 'kiwi']
#using sort to not alter the original list
fruit.sort()
print(fruit)
['apples', 'bananas', 'kiwi', 'oranges', 'passion fruit']
#reversing a list
fruit.sort()
print(fruit)
['apples', 'bananas', 'kiwi', 'oranges', 'passion fruit']

#deleting from list
#deleting from index position
del fruit[1]
print(fruit)
['passion fruit', 'kiwi', 'bananas', 'apples']
#deleting using pop()
fresh_fruit = fruit.pop(1)
print(fresh_fruit)
#deleting using remove()
fruit.remove('passion fruit')
print(fruit)

#Determining type
#type() method
my_variable = "A string"
print(type(my_variable))

#aws python workshop: Getting started, variables, data types