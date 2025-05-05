# a changable unordered,collections of unique key:value pairs
# method 1
mydict={"name":"muneeb","age":21,"city":"lahore"}
# method 2
mydict2=dict(name="muneeb",age=21,city="lahore")

# to update a list
mydict={"name":"muneeb","age":21,"city":"lahore"}
mydict2={"name":"Alex","age":22,"city":"Istanbul"}
mydict.update(mydict2)
print(mydict)

# example 1
dict={0:"a",1:"b",2:"c",3:"d"}
print(dict)
print(dict[3])

dict={"son":"a","daughter":"b","mother":"c","father":"d"}
print(dict)
print(dict["father"])

# example 2
capital_city={"Pakistan":"Islamabad","Turkey":"Ankra","India":"New Dehli"}
print(capital_city)
print(capital_city["Pakistan"])
print(capital_city["India"])

# print(capital_city["germany"])           #error because germany is not there
print(capital_city.get("germany"))
print(capital_city.update({"Germany":"Berlin"}))   
print(capital_city.keys()) 
print(capital_city.values()) 

# print all keys
for key in capital_city.keys():
    print(key)
# print all values
for value in capital_city.values():
    print(value)
# print both keys and values
for key,value in capital_city.items():
    print(key,value)

for i in capital_city:
    print(i,capital_city[i],sep=",")

my_anime_list=[
    {"anime":"aot","year":2013,"rating":9},
    {"anime":"fmab","year":2009,"rating":9.1},
    {"anime":"jjba","year":2012,"rating":8.6},
    {"anime":"mha","year":2014,"rating":8.3}
]
# print(my_anime_list)
for i in my_anime_list:
    print(i["anime"],i["year"],i["rating"],sep=",")

# we can put a tuple as a key or as a value as well but we cannot put list as a key neither as a value