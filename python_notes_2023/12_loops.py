# while loop
# run code until the condition evaluates to false
# example 1
n=int(input("Enter the number of time you want to run the program:"))
j=0
while j<n:
    print("Come On!!!")
    j+=1

# example 2
total=0
num=int(input("Enter a number:"))
while num!=0:
    total=total+num
    num=int(input("Enter a number:"))

print("total sum:",total)


# example 3
while True:
    n=int(input("Enter any number to guess:"))
    if n!=0:
        continue        #The continue keyword is used to skip the rest of the current iteration of a loop and move to the  next iteration
    else:
        break           #The break keyword is used to exit or terminate a loop prematurely. 
                        #When encountered within a loop (such as a for or while loop), 
                        #it immediately ends the loop and continues with the next statement after the loop. I
    

# for loop
# for loop is use to iterating over a sequence or iterables(list,tuple,string,range,dictionary,set)
# example 1
#   i in [0,1,2,3,4]     
for i in [2,4,6,8,10]:
    print(i)

# example 2
digits=[1,3,5,7,9]
for i in digits:
    print(i)
else:
    print("No digits left")

# example 3
anime=["attack on titan","onepiece","bleach","monster"]
for i in anime:
    print(i)
else:
    print("sorry naruto fans")

# example 4
for i in "hellofriend":
    print(i)

# example 5
for i in range(0,7):
    print("message")
# alternative
for _ in range(3):
    print("hello")
# alternative
print("alternative" * 5)

# example 6
anime=["attack on titan","onepiece","bleach","monster"]
for i in range(len(anime)):
    print(i+1,anime[i])

# example 7
names=[]
for _ in range(3):
    abc=input("Enter Name:")
    names.append(abc)

for i in sorted(names):
    print(i)

# example 8
import time
for index in range(10,0,-1):         #range(start,stop,step)
    print(index)
    time.sleep(1)
print("Very Well Then")

# example 9
# nested loops 
# the "inner loops" completes all of its iterations before finishing one iteration of "outer loop"
rows=int(input("enter number of rows:"))
columns=int(input("enter number of colums:"))
symbol=input("enter symbol:")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    # for new line after every inner loop iteration
    print()                                      


# loop statements 
# break--->use to terminate the loop entirely
# continue--->skip to next iteration of the loop
# pass--->does nothing,act as a placeholder

while True:
    user_name=input("Enter your Name:")
    if user_name != "":
        break

phone_number="923-234234-454"
for i in phone_number:
    if i != "-":
        print(i,end="")