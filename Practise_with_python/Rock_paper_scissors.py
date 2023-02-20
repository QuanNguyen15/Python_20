def main():
    from random import randint

    while True:
        player = str(input("\nInput Dam, La, Keo: "))
        if (player == "Dam") or (player == "La") or (player == "Keo"):
            break

    computer = randint(0,2)

    if computer == 0:
        computer = "Dam"
    if computer == 1:
        computer = "La"
    if computer == 2:
        computer = "Keo"

    print("---")
    print("You chose: " + player)
    print("Computer choses: " + computer)
    print("---")


    if player == computer:
        print("Draw")
    else:
        if player == "Keo":
            if computer == "Dam":
                print("Lose")
            else:
                print("Win")

        elif player == "Dam":
            if computer == "Keo":
                print("Win")
            else:
                print("Lose")

        elif player == "La":
            if computer == "Keo":
                print("Lose")
            else:
                print("Win")
        else:
            print("Input wrong!")
main()   

