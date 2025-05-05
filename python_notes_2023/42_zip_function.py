username=["abcdefghijxyzl","muneebimtiaz6","ishow"]
passwords=["12345678","password","guest"]
last_login=["1/1/23","3/3/23","4/4/23"]
speed=["3mbs","4mbs","5mbs"]

new=(zip(username,passwords,last_login,speed))
# new=list(zip(username,passwords,last_login,speed))
print(type(new))
for i in new:
    print(i)



# dict
username=["abcdefghijxyzl","muneebimtiaz6","ishow"]
passwords=["12345678","password","guest"]

new=dict(zip(username,passwords))
print(type(new))
for key,value in new.items():
    print(f"{key}:{value}")
