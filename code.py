import random
options = ["rock", "paper", "scissor"]

print("welcome to rock paper scissor game")
while True:
    cump = random.choice(options)
    print("type 'q' or 'Q' to exit the game")
    hum = input("enter rock or paper or scissor :-  ")
    try:
        if float(hum):
            print("error : enter only rock or paper or scissor")
            break
    except ValueError:
        pass
    if hum == cump:
        print(f"computer's choice {cump} , your choice {hum}")
        print("nobody won")
        break
    elif hum == "rock" and cump == "scissor":
        print(f"computer's choice : {cump} , your's choice {hum} ")
        print("congratulations you won")
        break
    elif hum == "scissor" and cump == "paper":
        print(f"computer's choice {cump} , your choice {hum}")  
        print("congratulations you won")
        break  
    elif hum == "paper" and cump == "rock":
        print(f"computer's choice {cump} , your choice {hum}")
        print("congratulations you won")
        break
    elif hum == "rock" and cump == "paper":
        print(f"computer's choice {cump} , your choice {hum}")
        print("computer won")
        break
    elif hum == "scissor" and cump == "rock":
        print(f"computer's choice {cump} , your choice {hum}")
        print("computer won")
        break
    elif hum == "paper" and cump == "scissor":
        print(f"computer's choice {cump} , your choice {hum}")
        print("computer won")
        break
    elif hum == "q" or "Q":
        print("exiting the game, thank you for playing")
        break
    else:
        print("error")
        
        


      