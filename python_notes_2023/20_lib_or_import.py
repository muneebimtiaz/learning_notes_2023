# random module
# example 1
import random
coin=random.choice(["heads","tails"])
print(coin)

# another approach
from random import choice
coin=choice(["heads","tails"])
print(coin)

# example 2
import random
xx=1
while xx<10:
    cards=["Jack","Queen","King"]
    random.shuffle(cards)
    for i in cards:
        print(i)
    xx=xx+1


# statistics module
import statistics
english=84
maths=99
computer=78
total_marks=statistics.mean([english,maths,computer])
print(total_marks)


# sys module
# example 1
import sys
try:
    print("My name is ",sys.argv[1])
except IndexError:
    print("Please type only one argument")

# another appoarch
import sys
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("My name is ",sys.argv[1])

# example 2
import sys
if len(sys.argv) < 2:
    print("Too few arguments")
for i in sys.argv:
    print("My name is ",i)

# another appoarch //slice
import sys
if len(sys.argv) < 2:
    print("Too few arguments")
for i in sys.argv[1:]:
    print("My name is ",i)

# importing function from my own create file
from permod import hello
hello()