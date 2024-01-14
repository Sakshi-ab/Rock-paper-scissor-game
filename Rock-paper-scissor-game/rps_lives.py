print("rock paper scissor game !!")

print("Enter below choice to play")
print("0 -> Rock")
print("1 -> paper")
print("2 -> Scissor")
print("\n")

import random

user_lives = 3
pc_lives = 3
user_score = 0
pc_score = 0

while user_lives > 0 and pc_lives > 0:
    user = int(input())
    pc = random.randrange(3)

    print("user :", user)
    print("pc :", pc)
    

    if(user == 0):
        if( pc == 0):
            print("its draw !!")
            print("\n\n")
        elif(pc == 1):
            print("pc won")
            pc_score += 1
            user_lives -= 1
            print("user live : ", user_lives)
            print("pc live :", pc_lives)
            print("\n")
            print("User Score:", user_score)
            print("PC Score:", pc_score)
            print("\n\n")
        elif(pc == 2):
            print("user won")
            user_score += 1
            pc_lives -= 1
            print("pc live :", pc_lives)
            print("user live : ", user_lives)
            print("\n")
            print("User Score:", user_score)
            print("PC Score:", pc_score)
            print("\n\n")

    elif(user == 1):
        if( pc == 1):
            print("its draw")
            print("\n\n")
        elif(pc == 0):
            print("user won")
            user_score += 1
            pc_lives -= 1
            print("pc live :", pc_lives)
            print("user live : ", user_lives)
            print("\n")
            print("User Score:", user_score)
            print("PC Score:", pc_score)
            print("\n\n")
        elif(pc == 2):
            print("pc won")
            pc_score += 1
            user_lives -= 1
            print("user live : ", user_lives)
            print("pc live :", pc_lives)
            print("\n")
            print("User Score:", user_score)
            print("PC Score:", pc_score)
            print("\n\n")

    elif(user == 2):
        if( pc == 2):
            print("its draw")
            print("\n\n")
        elif(pc == 1):
            print("user won")
            user_score += 1
            pc_lives -= 1
            print("pc live :", pc_lives)
            print("user live : ", user_lives)
            print("\n")
            print("User Score:", user_score)
            print("PC Score:", pc_score)
            print("\n\n")
        elif(pc == 0):
            print("pc won")
            pc_score += 1
            user_lives -=1
            print("user live : ", user_lives)
            print("pc live : ", pc_lives)
            print("\n")
            print("User Score:", user_score)
            print("PC Score:", pc_score)
            print("\n\n")
            
    else:
        print("invalid input")


print("\n\n")
print("User Score:", user_score)
print("PC Score:", pc_score)

if user_score > pc_score:
    print("User wins!")
elif user_score < pc_score:
    print("PC wins!")
else:
    print("It's a draw!")





 

