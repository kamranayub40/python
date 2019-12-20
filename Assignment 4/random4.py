import random
winning_nbr=random.randint(10,30)
guess=1
number=int(input("Enter your guess number between 10 to 30 :"))
game_over=false
while not game_over:
    if number==winning_nbr:
        print(f"You win and yu guess the number in {guess} times :")
        game_over=True
    else:
        if number<winning_nbr:
            print("To Low")
            guess+=1
            number=int(input("Guess Again"))
        else:
            print("To High")
            guess+=1
            print(int(input("Guess Again")))
            