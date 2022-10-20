# ASCII art used below can be found at ascii.co.uk/art
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Headers 
print("\n")
print("Welcome to the Detective Game \n")
print("Your mission is to find the stolen treasure \n") 

# Using .lower() to convert answer into all lowercase
move_1 = input("You walk into the suspects home, where would you like to go? living room or garden? \n").lower()

# First move
if move_1 == "living room":
  move_2 = input("You walk into the living room, would you like to explore the living room further or move onto the kitchen? living room or kitchen? \n").lower()

  # Second move
  if move_2 == "living room":
    move_3 = input("What would you like to explore in the living room?, inside cupboard, under sofa or behind tv? \n").lower()

    # Third move
    if move_3 == "inside cupboard":
      print("YOU FOUND THE STOLEN TRASURE!, well done detective :)")
    elif move_3 == "under sofa":
      print("The sofa fell on you and you got squashed, GAME OVER :(")
    elif move_3 == "behind tv":
      print("You got electrocuted, GAME OVER :(")
    else:
      print("GAME OVER:(")

      
  else:
    print("The suspects kitchen floor was slippery, you fell and hurt yourself, GAME OVER :(")

  
else:
  print("You walked into a boobie trap, GAME OVER :(")


