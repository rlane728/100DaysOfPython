print('''
                                       /\
                                      /`:\
                                     /`'`:\
                                    /`'`'`:\
                                   /`'`'`'`:\
                                  /`'`'`'`'`:\
                                   |`'`'`'`:|
     _ _  _  _  _                  |] ,-.  :|_  _  _  _
    ||| || || || |                 |  |_| ||| || || || |
    |`' `' `' `'.|                 | _'=' |`' `' `' `'.|
    :          .:;                 |'-'   :          .:;
     \-..____..:/  _  _  _  _  _  _| _  _'-\-..____..:/
      :--------:_,' || || || || || || || `.::--------:
      |]     .:|:.  `' `'_`' `' `' `' `'    | '-'  .:|
      |  ,-. .[|:._     '-' ____     ___    |   ,-.'-|
      |  | | .:|'--'_     ,'____`.  '---'   |   | |.:|
      |  |_| .:|:.'--' ()/,| |`|`.\()   __  |   |_|.:|
      |  '=' .:|:.     |::_|_|_|\|::   '--' |  _'='.:|
      | __   .:|:.     ;||-,-,-,-,|;        | '--' .:|
      |'--'  .:|:. _  ; ||       |:|        |      .:|
      |      .:|:.'-':  ||       |;|     _  |]     _:|
      |      '-|:.   ;  ||       :||    '-' |     '--|
      |  _   .:|].  ;   ||       ;||]       |   _  .:|
      | '-'  .:|:. :   [||      ;|||        |  '-' .:|
  ,', ;._____.::-- ;---->'-,--,:-'<'--------;._____.::.`.
 ((  (          )_;___,' ,' ,  ; //________(          ) ))
  `. _`--------' : -,' ' , ' '; //-       _ `--------' ,'
       __  .--'  ;,' ,'  ,  ': //    -.._    __  _.-  -
   `-   --    _ ;',' ,'  ,' ,;/_  -.       ---    _,
       _,.   /-:,_,_,_,_,_,_(/:-\   ,     ,.    _
     -'   `-'--'-'-'-'-'-'-'-''--'-' `-'`'  `'`' `-SSt-
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
player_choice = input("Would  you like to go left or right? ")
player_choice = player_choice.lower()
if (player_choice != "left"):
    print(f"You fall into a cleverly laid pitfall trap and die!")
    print("Game Over.")
else:
    print("You are standing on the edge of a lake, looking at a keep on an island far beyond.")
    player_choice = input("Would you like to swim, or wait? ")
    player_choice = player_choice.lower()
    if (player_choice == "swim"):
        print(f"You swim out into the pristine waters, cool sheets of glass-like water lap around you...")
        print(f"...when you're suddenly swallowed by a giant lake trout and DIE!!!!!")
        print("Game Over.")
    else:
        print(f"In time, you notice a canoe up the shoreline.  You use it to reach the island beyond.")
        print(f"Upon reaching the island you stand at the foot of the keep.")
        print(f"There are three doors standing before you, one red, one blue, one yellow.")
        player_choice = input("Which door will you enter? ")
        player_choice = player_choice.lower()
        if (player_choice == "yellow"):
            print("You Win!")
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
        elif (player_choice == "blue"):
            print("The room is filled with mugabugs!  They swarm and devour you!")
            print("Game Over.")
        elif (player_choice == "red"):
            print("Entering the room, you glimpse a doorway beyond.")
            print("You step forward, only to step upon a trapped stone!")
            print("Fire bellows forth from hidden cracks in the walls and ceiling, engulfing you in searing flames!")
            print("Your skin melts from your bones as you scream in agony!")
            print("Game Over.")
        else:
            print("Game Over.")
