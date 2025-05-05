import random
while True:
    try:
        player=input("rock,paper or scissor?:")
        list=["rock","paper","scissor"]
        comp=random.choice(list)
    
        if player not in list:
            print("Invalid input.please enter only from rock,paper or scissor:")
            continue
        else:
            print(f"computer:{comp}")
            print(f"player:{player}")
            
    
        if player=="rock" and comp=="paper":
            print("You lose :(")

        elif player=="rock" and comp=="scissor":
            print("You win :)")

        elif player=="paper" and comp=="rock":
            print("You win :)")

        elif player=="paper" and comp=="scissor":
            print("You lose :(")

        elif player=="scissor" and comp=="rock":
            print("You lose :(")

        elif player=="scissor" and comp=="paper":
            print("You win :)")

        else:
            print("Tie")

        xx=input("Play again? (yes/no):")
        if xx!="yes":
            break
    except:
        pass #he pass keyword is a placeholder statement that does nothing. It is used when you need a statement syntactically but don't want to include any code. It acts as a null operation and is often used as a placeholder to prevent syntax errors.


print("Thank You for playing")

