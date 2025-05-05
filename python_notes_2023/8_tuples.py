# tuples are ordered and immutable(unchangable)
# method 1
tuple=("hello","bye",3000)
# method 2
tuple="hello","bye",3000

mytuple=("hello")        #it is a string instead of tuple
print(type(mytuple))     #str

mytuple=("hello",)
print(type(mytuple))     #tuple


tuple_of_anime=("aot","fmab","jjba","mha")
print(tuple_of_anime)

tuple_of_digits=[1,3,7,9,11]
print(tuple_of_digits)

tuple_of_mixed=[5,"muneeb","imtiaz",11,'@']
print(tuple_of_mixed)

tuple_of_vowels=["a","e","i","o","u"]
print(tuple_of_vowels)

# access tuple items 
print(tuple_of_anime[0])
print(tuple_of_anime[1])
print(tuple_of_anime[-1])
print(tuple_of_anime[-2])

print(tuple_of_vowels[0])
print(tuple_of_vowels[-5])

# appent item in a tuple~appent()
tuple_of_digits.append(5)
print(tuple_of_digits)

# insert item in a tuple~insert()
tuple_of_digits.insert(2,"x")
print(tuple_of_digits)

# extend one tuple to another~extend()
tuple_of_even_numbers=[2,4,6,8,10]
tuple_of_prime_numbers=[2,3,5,7,11]
tuple_of_even_numbers.extend(tuple_of_prime_numbers)
# print(tuple_of_prime_numbers)---->this line of code doesnot give an error but it is a wrong
print(tuple_of_even_numbers)

# slicing of tuple items
print(tuple_of_mixed)       #correct
# print(tuple_of_mixed[])   #error
print(tuple_of_mixed[:])    #correct
print(tuple_of_mixed[1:3])
print(tuple_of_mixed[:4])
created_tuple=[1,2,3,4,5,6,7,8,9]   #new tuple created
print(created_tuple[::2])           #step 2 
print(created_tuple[::3])
print(created_tuple[::-1])           #reverse the tuple


# deleting the tuple item
del tuple_of_anime[1]
print(tuple_of_anime) 

# sort() or sorted()
mytuple=[-1,4,6,8,-3,-5]
mytuple.sort()
print(mytuple)

new_tuple=sorted(mytuple)
print(mytuple)       #[-1,4,6,8,-3,-5]
print(new_tuple)     #[-1,-3,-5,4,6,8]

