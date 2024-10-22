import random
choice=["rock","paper","seissor"]
print("Welcome to the Rock,Paper,Seissor games.")
def games():
    computer_score,user_score=0,0
    while True:
        computer_choice=random.choice(choice)
        user_choice=input("Enter your Choice(Rock,Paper.Seissor):").lower()
        if computer_choice=="rock":
            if user_choice=="rock":
                print(f"Your choice is {user_choice} and computer choice is {computer_choice}.You both choose same.tie")
                print(f"Your Score is {user_score} and computer score is {computer_score}")
            elif user_choice=="paper":
                print(f"your choise is {user_choice} and computer choice is {computer_choice}. You win and computer loose")
                user_score+=1
                print(f"Your Score is {user_score} and computer score is {computer_score}")
            elif user_choice=="seissor":
                print(f"your choise is {user_choice} and computer choice is {computer_choice}. You loose and computer win")
                computer_score+=1
                print(f"Your Score is {user_score} and computer score is {computer_score}")
        elif computer_choice=="paper":
            if user_choice=="paper":
                print(f"Your choice is {user_choice} and computer choice is {computer_choice}.You both choose same.tie")
                print(f"Your Score is {user_score} and computer score is {computer_score}")
            elif user_choice=="seissor":
                print(f"your choise is {user_choice} and computer choice is {computer_choice}. You win and computer loose")
                user_score+=1
                print(f"Your Score is {user_score} and computer score is {computer_score}")
            elif user_choice=="rock":
                print(f"your choise is {user_choice} and computer choice is {computer_choice}. You loose and computer win")
                computer_score+=1
                print(f"Your Score is {user_score} and computer score is {computer_score}")
        elif computer_choice=="seissor":
            if user_choice=="seissor":
                print(f"Your choice is {user_choice} and computer choice is {computer_choice}.You both choose same.tie")
                print(f"Your Score is {user_score} and computer score is {computer_score}")
            elif user_choice=="rock":
                print(f"your choise is {user_choice} and computer choice is {computer_choice}. You win and computer loose")
                user_score+=1
                print(f"Your Score is {user_score} and computer score is {computer_score}")
            elif user_choice=="paper":
                print(f"your choise is {user_choice} and computer choice is {computer_choice}. You loose and computer win")
                computer_score+=1
                print(f"Your Score is {user_score} and computer score is {computer_score}")
        if computer_score==3:
            print(f'Computer score is {computer_score} and computer win')
            break
        elif user_score==3:
            print(f"Your score is {user_score} and you win")
            break
    continues=input("Do you want to Continue? Yes or No.").lower()
    if continues=="yes":
        games()
    elif continues=="no":
        print("Thank you for playing")
games()