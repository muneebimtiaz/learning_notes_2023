# example 1
anime=["attack on titan","monster","onepiece"]
tv_series=["game of therons","the walking dead","breaking bad"]
movies=["titanic","endgame","the dark knight"]
# what_to_watch=[index 0,index 1,index 2]
what_to_watch=[anime,tv_series,movies]
print(what_to_watch)

print(what_to_watch[0])
print(what_to_watch[1])
print(what_to_watch[2])

# print(what_to_watch[0][0])
# print(what_to_watch[0][1])
# print(what_to_watch[0][2])
# print(what_to_watch[1][0])
# print(what_to_watch[1][1])
# print(what_to_watch[1][2])
# print(what_to_watch[2][0])
# print(what_to_watch[2][1])
# print(what_to_watch[2][2])
# # # print(what_to_watch[2][3])      error out of index

for i in range(len(what_to_watch)):
    for j in range(len(what_to_watch[i])):
        print(what_to_watch[i][j],end=' ')
        print()   #break line


# example 2
list_of_number=[1,3,5,7,9]
list_of_alphbets=["a","b","c","d","e"]
list_of_characters=['!','@','#','$','%','^','&']

multidem_list=[list_of_number,list_of_alphbets,list_of_characters]


for i in range(len(multidem_list)):
    for j in range(len(multidem_list[i])):  
        print(multidem_list[i][j],end=",")