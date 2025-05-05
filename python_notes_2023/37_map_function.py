# map(function,iterables)
store=[("shirt",20.50),
       ("pants",30.35),
       ("jacket",55.5),
       ("shoes",45.75)]


# for i in range(len(store)):
#     for j in range(len(store[i])):
#         print(store[i][j])

def to_euros(data):
    return (data[0],data[1]*0.82)

converted=list(map(to_euros,store))
for i in converted:
    print(i)