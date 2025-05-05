""" 
lists are used to store multiple data at once. For example,
Suppose we need to record the ages of 5 students. Instead of creating 5 separate variables, we can simply create a list"""

list_of_anime=["aot","fmab","jjba","mha"]
print(list_of_anime)

list_of_digits=[1,3,7,9,11]
print(list_of_digits)

list_of_mixed=[5,"muneeb","imtiaz",11,'@']
print(list_of_mixed)

list_of_vowels=["a","e","i","o","u"]
print(list_of_vowels)

# access list items 
print(list_of_anime[0])
print(list_of_anime[1])
print(list_of_anime[-1])
print(list_of_anime[-2])

print(list_of_vowels[0])
print(list_of_vowels[-5])

# appent item in a list~appent()
list_of_digits.append(5)
print(list_of_digits)

# insert item in a list~insert()
list_of_digits.insert(2,"x")
print(list_of_digits)

# extend one list to another~extend()
list_of_even_numbers=[2,4,6,8,10]
list_of_prime_numbers=[2,3,5,7,11]
list_of_even_numbers.extend(list_of_prime_numbers)
"""print(list_of_prime_numbers)---->wrong"""
print(list_of_even_numbers)

# slicing of list items

print(list_of_mixed)       #correct
# print(list_of_mixed[])   #error
print(list_of_mixed[:])    #correct
print(list_of_mixed[1:3])
print(list_of_mixed[:4])
created_list=[1,2,3,4,5,6,7,8,9]   #new list created
print(created_list[::2])           #step 2 
print(created_list[::3])
print(created_list[::-1])           #reverse the list


# deleting the list item
del list_of_anime[1]
print(list_of_anime) 

# sort() or sorted()
mylist=[-1,4,6,8,-3,-5]
mylist.sort()
print(mylist)

new_list=sorted(mylist)
print(mylist)       #[-1,4,6,8,-3,-5]
print(new_list)     #[-1,-3,-5,4,6,8]


"""
Python List Methods
Python has many useful list methods that makes it really easy to work with lists.

append()--->add an item to the end of the list
extend()--->add items of lists and other iterables to the end of the list
insert()--->inserts an item at the specified index
remove()--->removes item present at the given index
pop()--->returns and removes item present at the given index
clear()--->removes all items from the list
index()--->returns the index of the first matched item
count()--->returns the count of the specified item in the list
sort()--->sort the list in ascending/descending order
reverse()--->reverses the item of the list
copy()--->returns the shallow copy of the list
"""
