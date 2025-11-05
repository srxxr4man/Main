print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("----------------STICK GAME------------")#Title
print("Select 1,2 or 3 Sticks from the Stick Pile")
print("The Player who takes LAST Stick LOOSES")
print()

total_Sticks=16
player=1

while total_Sticks>1:
    print(f"Stick Remaing is {total_Sticks}")
    choice=int(input(f"Player {player} pick1,2 or 3 Sticks:"))

    if choice<1 or choice>3:
        print("Invalid")
        continue
    if choice>=total_Sticks:
        print("NO ENOUGH STICKS")
        continue
    total_Sticks-=choice

    if player==1:
        player=2
    else:
        player=1
print("ONLY ONE STICK REMAINING")
print(f"Player {player} is forced to take LAST Stick and LOST")
    
if player==1:
    print("Player 2 Wins")
else:
    print("Player 1 Wins")
