import random
computer_choise=random.randint(1,21)
def number_guessing_game():
    print("Welcome to Number Guessing Game.")
    life=0
    while True:
        level=input("PLease Choose your Level 'Easy','Medium','Hard': ").lower()
        if level=="easy":
            life=10
            break
        elif level=="medium":
            life=6
            break
        elif level=="hard":
            life=3
            break
        else:
            print("Invalid Input!")
    while True:
        users_choise=input("Please choose a number between 1 to 20: ")
        if users_choise.isdigit():
            users_choise=int(users_choise)
            if users_choise<=0:
                print("Please enter a number larger than 0")
            else:
                if users_choise<computer_choise:
                    print("Your guess is wrong.Please enter a larger number")
                    life-=1
                    print(f"You have {life} life left.")
                elif users_choise>computer_choise:
                    print("Your guess is wrong.Please enter a smaller number")
                    life-=1
                    print(f"You have {life} life left.")
                elif users_choise==computer_choise:
                    print(f"Bingo you guess the write number.The number is {computer_choise}")
                    break
                else:
                    print("Please enter a valid number.")
        else:
            print("Please enter a number next time.")
            quit()
        if life==0:
            print(f"You loose the game.The number is {computer_choise}")
            break
        else:
            continue
    game_continue=input("Do you want to Condinue? 'Yes' or 'No': ").lower()
    if game_continue=="yes":
        number_guessing_game()
    else:
        print("Thank you for playing.")

number_guessing_game()


        
