import time
import random 

def print_pause(prompt):
    print(prompt)
    time.sleep(2)

def introduction_message():
    print_pause("You find yourself standing in an open field"
                 "filled with grass and yellow wildflowers."
                )
    print_pause("Rumor has it that a dragon is somewhere around here"
                "and has been terrifying the nearby village."
                )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) dagger.")

def prompt_message1():
    print()
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?\n please enter 1 or 2")

def fight_runPrompt():
    print_pause("Would you like to (1) fight or (2) run away?")

def entering_house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a dragon.")
    print_pause("Eep! This is the dragon's house!")
    print_pause("The dragon attacks you!")
    print_pause("You feel a bit under-prepared for this, what with only having a tiny dagger.")

def entering_cave():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger and take the sword with you.")
    print_pause("You walk back out to the field.")
    print()
    user_choice1()

def user_choice1():
    prompt_message1()
    choice= input()
    if choice== "1":
        entering_house()
        user_choice2()
    elif choice== "2":
        entering_cave()
    else:
        print("Wrong choice please check and re-enter ")
        prompt_message1()
        user_choice1()

def loss_fight ():
    print_pause("You do your best...")
    print_pause("but your dagger is no match for the gorgon.")
    print_pause("You have been defeated!")
    print_pause("")
    play_again()

def win_fight():
    print_pause("As the pirate moves to attack, you unsheath your new sword.")
    print_pause("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
    print_pause("But the pirate takes one look at your shiny new toy and runs away!")
    print_pause("You have rid the town of the pirate. You are victorious!")
    print()
    play_again()

def random_odds():
    choose= random.randint(1,2)
    if choose== 1:
        loss_fight()

    else:
        win_fight()

def run_away():
    print_pause("You run back into the field.")
    print_pause(" Luckily, you don't seem to have been followed.")
    print()
    user_choice1()
    
def user_choice2():
    fight_runPrompt()
    choice1= input()
    if choice1== "1":
        random_odds()
    elif choice1== "2":
        run_away()    
    else:
        print("Wrong choice please check and re-enter ")
        user_choice2()

def play_again():
    again= input(" Want to play again? enter Y/N ").lower()
    if again != "n":
        print("excellent !! restarting the game")
        introduction_message()
        user_choice1()

    else:
        print_pause("Thank you for playing see you next time!!")

def adventure_game():
    introduction_message()
    user_choice1()



adventure_game()
