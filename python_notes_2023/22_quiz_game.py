# question_answers={"which planet is closest to the sun":"b","who was the first man in space":"b","which is the largest moon in the solar system":"a","which is the largest planet in the solar system":"c"}


question_answers = [
    "which planet is closest to the sun",
    "who was the first man in space",
    "which is the largest moon in the solar system",
    "which is the largest planet in the solar system"
]
correct=["b","b","a","c"]


q1 =["a.Earth", "b.Mercury", "c.Venus", "d.Mars"],
q2 =["a.Neil Armstrong","b.Yuri Gagarin","c.John Glenn","d.Buzz Aldrin"]
q3=["a.Ganymede","b.Titan","c.Callisto","d.Io"]
q4=["a.Earth","b.Mars","c.Jupiter","d.Saturn"]
options=[q1,q2,q3,q4]

# opt=",".join(options)

user_input = []
for i in range(len(question_answers)):
    print(question_answers[i])
    # print(opt[i])
    print(options[i])
    user_input.append(input())

print("You Selected options:",user_input)
print("Correct options:     ",correct)

if correct==user_input:
    print("Your options are correct")
else:
    print("Your options are wrong")