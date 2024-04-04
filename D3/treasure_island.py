def main():
    choices = ["You are at a crossroad, which turn do you take? Type 'RIGHT' or 'LEFT': ",
               "You came to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ",
               "You arrive at the island unharmed. There is a house with doors. One Red, one Yellow, and one Blue. Which colour do you choose? "]
    counter = 0
    for i in choices:
        if input(f'{i}') in ["LEFT", "wait", "Yellow"]:
            counter+=1
            if counter == 3:
                 print("You made it alive! ")  
        else:    
            print("You are dead! ")
            return # End the game if the choice is incorrect

    

if __name__ == "__main__":
    print(""" __          __  _                                        _                 _                       
 \ \        / / | |                              /\      | |               | |                      
  \ \  /\  / /__| | ___ ___  _ __ ___   ___     /  \   __| |_   _____ _ __ | |_ _   _ _ __ ___ _ __ 
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \   / /\ \ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ '__|
    \  /\  /  __/ | (_| (_) | | | | | |  __/  / ____ \ (_| |\ V /  __/ | | | |_| |_| | | |  __/ |   
     \/  \/ \___|_|\___\___/|_| |_| |_|\___| /_/    \_\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|_|   
                                                                                                    
                                                                                                    """)
    print("Welcome to the treasure island! ")
    print("Your mission is to find the treasure ^-^ ")

    if input("This adventure requires precision, Do you accept the challenge? Type 'YES' if you want to continue: ") == "YES":
        main()
        while input("Do you want to play again? You think you are worthy? Type 'YES' if you are: ") == "YES":
            main()    
    print("Thank you for visiting")
