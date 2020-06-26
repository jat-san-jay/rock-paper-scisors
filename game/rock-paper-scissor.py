# import random module
import random

playing = True

choices = {
    "1": "The Rock",
    "2": "Paper",
    "3": "Scissor"
}
while playing:
    print("Enter choice \n 1.The Rock \n 2. Paper \n 3. Scissor \n")
    choice = int(input("Your turn: "))
    while choice > 3 or choice < 1:
        choice = int(input("Enter number between 1 to 3"))
    your_choice = choices.get(str(choice))
    print("Your choice is: " + your_choice)
    random_comp_turn = random.randint(1, 3)

    while choice == random_comp_turn:
        random_comp_turn = random.randint(1, 3)

    system_turn = choices.get(str(random_comp_turn))

    print("Computer choice is: " + system_turn)

    if ((your_choice == choices.get("1") and system_turn == choices.get("2")) or
            (your_choice == choices.get("2") and system_turn == choices.get("1"))):
        print(choices.get("2"), ' Win')
    elif ((your_choice == choices.get("1") and system_turn == choices.get("3")) or
          (your_choice == choices.get("3") and system_turn == choices.get("1"))):
        print(choices.get("1"), ' Win')
    else:
        print(choices.get("3"), ' Win')

    play_next = input("Do you want to play ... y/n?")
    if play_next == 'y' or play_next == 'Y' or play_next == 'yes' or play_next == 'Yes':
        continue
    else:
        break
