print('''                                                                           
                                                                           
  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          
                                                                           
                                                                           
                                                               
           88           88                                 88  
           ""           88                                 88  
                        88                                 88  
 ,adPPYba, 88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
a8P_____88 88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
8PP""""""" 88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
"8b,   ,aa 88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
 `"Ybbd8"' 88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8  
                                                               
                                                               
''')



print('Welcome to the Treasure Island')
print('Your mission is to find the treasure')
first_choose = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()


if first_choose == 'left':
    second_choose = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim cross\n').lower()
    if second_choose == 'wait':
        third_choose = input("You arrive at the island unharmed. There is a house with 3 doors. One red, One yellow and One blue. Which colour do you choose? (red, yellow or blue)\n").lower()
        if third_choose == 'yellow':
            print('You Win!')
        elif third_choose == 'red':
            print("Burned by fire. Game Over")
        elif third_choose == 'blue':
            print("Eaten by beasts. Game Over")
        else:
            print('Game Over.')
    else:
        print('Attacked by trout. Game Over.')
else:
    print('Fall into a hole. Game Over.')

