# filter(function,iterables)

details=[("muneeb",20),
         ("taimoor",20),
         ("ahmed",22),
         ("kiseem",19),
         ("alex",16),
         ("jason",14)]


# for i in range(len(details)):
#     for j in range(len(details[i])):
#         print(details[i][j])

def to_chk(data):
    return (data[1]>=18)

endgame=list(filter(to_chk,details))
for i in endgame:
    print(i)