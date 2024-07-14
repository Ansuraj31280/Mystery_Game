import time
import random

# Helper function to print text slowly for a dramatic effect
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

# Function to introduce the game and set the stage
def intro():
    print_slow("Welcome to the Mystery Solving Game!\n")
    print_slow("You find yourself in a deserted mansion late at night.")
    print_slow("Your mission is to solve the mystery of the missing artifact hidden within.\n")
    print_slow("You step inside the mansion and the door slams shut behind you...\n")

# Function to explore different rooms and interact with clues
def explore_mansion():
    print_slow("You are in the foyer of the mansion.")
    print_slow("There are three doors in front of you: 'left', 'middle', and 'right'.\n")
    choice = input("Which door do you want to enter? ").lower()

    if choice == 'left':
        print_slow("You enter the library.")
        library()
    elif choice == 'middle':
        print_slow("You enter the dining hall.")
        dining_hall()
    elif choice == 'right':
        print_slow("You enter the conservatory.")
        conservatory()
    else:
        print_slow("Invalid choice. The mansion overwhelms you and you get lost.")
        game_over()

# Function for exploring the library and finding clues
def library():
    print_slow("You find yourself surrounded by dusty old books and shelves.")
    print_slow("There is a desk with a locked drawer and a bookshelf with a suspiciously empty spot.\n")
    choice = input("What do you investigate? 'desk', 'bookshelf', or 'leave'? ").lower()

    if choice == 'desk':
        print_slow("You examine the desk and find a key hidden under a stack of papers.")
        print_slow("You unlock the drawer and find a torn note with a riddle:\n")
        print_slow("I shine bright among the stars,")
        print_slow("My shape is a sign of luck afar,")
        print_slow("The triangle points to the sky,")
        print_slow("Yet the circle sees the world pass by.\n")
        puzzle()
    elif choice == 'bookshelf':
        print_slow("You investigate the empty spot and find a hidden switch.")
        print_slow("The bookshelf slides aside, revealing a secret passage!")
        secret_passage()
    elif choice == 'leave':
        print_slow("You decide to leave the library.")
        explore_mansion()
    else:
        print_slow("Invalid choice. The mystery deepens as you struggle to focus.")
        game_over()

# Function for solving a puzzle with cryptic symbols
def puzzle():
    print_slow("You need to arrange these symbols in the correct order to reveal a clue.\n")
    print_slow("Think creatively and out of the box to solve the puzzle!\n")

    # Example of a simple puzzle solution (can be more complex)
    correct_order = ["★", "♦", "△", "⊙"]
    user_order = []

    while user_order != correct_order:
        print_slow("Arrange the symbols: ")
        user_order = input().strip().split()

        if user_order == correct_order:
            print_slow("Congratulations! You solved the puzzle and revealed a hidden compartment.")
            print_slow("Inside, you discover a map leading to the artifact's location!")
            victory()
        else:
            print_slow("Incorrect order. Think creatively and try again.")

# Function for exploring the dining hall and interacting with characters
def dining_hall():
    print_slow("You enter the grand dining hall with a long table and dim lighting.")
    print_slow("There is a butler polishing silverware and a portrait with suspicious eyes.\n")
    choice = input("What do you investigate? 'butler', 'portrait', or 'leave'? ").lower()

    if choice == 'butler':
        print_slow("You approach the butler and ask about the mansion's history.")
        print_slow("He gives you a cryptic message about the master's secrets.")
        explore_mansion()
    elif choice == 'portrait':
        print_slow("You examine the portrait and notice the eyes seem to follow you.")
        print_slow("Behind the portrait, you find a safe with a numeric lock.")
        numeric_lock()
    elif choice == 'leave':
        print_slow("You decide to leave the dining hall.")
        explore_mansion()
    else:
        print_slow("Invalid choice. The mysterious atmosphere clouds your judgment.")
        game_over()

# Function for solving a numeric lock puzzle
def numeric_lock():
    print_slow("You need to guess the correct numeric code to open the safe.")
    print_slow("You have 3 attempts to enter the correct 4-digit code.\n")

    # Example of a numeric lock solution (can be more complex)
    code = random.randint(1000, 9999)
    attempts = 3

    while attempts > 0:
        guess = input("Enter your guess: ")
        if guess.isdigit() and len(guess) == 4:
            if int(guess) == code:
                print_slow("Congratulations! You unlocked the safe and found a key.")
                print_slow("The key unlocks a chest with valuable information!")
                victory()
                break
            else:
                print_slow("Incorrect code. Try again.")
                attempts -= 1
                print(f"Attempts left: {attempts}")
        else:
            print_slow("Invalid input. Enter a 4-digit number.")

    if attempts == 0:
        print_slow(f"You failed to open the safe. The mystery remains unsolved.")
        game_over()

# Function for exploring the conservatory and encountering a trap
def conservatory():
    print_slow("You step into the conservatory filled with exotic plants and statues.")
    print_slow("Suddenly, the door locks behind you and the room starts filling with gas!\n")
    print_slow("You need to find a way out before it's too late!\n")

    # Example of a trap escape solution (can be more complex)
    print_slow("Think creatively and out of the box to escape the trap!\n")
    choice = input("What do you do? 'inspect plants', 'check statues', or 'try windows'? ").lower()

    if choice == 'inspect plants':
        print_slow("You find a ventilation duct hidden behind the plants.")
        print_slow("You crawl through and escape the conservatory!")
        explore_mansion()
    elif choice == 'check statues':
        print_slow("You investigate the statues but find no escape route.")
        print_slow("The gas overwhelms you, and you collapse.")
        game_over()
    elif choice == 'try windows':
        print_slow("You attempt to break the windows, but they are reinforced.")
        print_slow("The gas fills the room, and you lose consciousness.")
        game_over()
    else:
        print_slow("Invalid choice. Panic clouds your judgment.")
        game_over()

# Function for the secret passage leading to victory
def secret_passage():
    print_slow("You enter a secret passage that twists and turns underground.")
    print_slow("You find yourself in a hidden chamber filled with ancient artifacts.\n")
    print_slow("Among the artifacts, you discover the missing artifact!\n")
    victory()

# Function for the victory scenario
def victory():
    print_slow("Congratulations! You have successfully solved the mystery and found the artifact!")
    print_slow("Thank you for playing!")

# Function for the game over scenario
def game_over():
    print_slow("Game over. Would you like to play again? 'yes' or 'no'? ")
    choice = input().lower()
    if choice == 'yes':
        play_game()
    else:
        print_slow("Thank you for playing!")

# Main function to start the game
def play_game():
    intro()
    explore_mansion()

# Entry point of the program
if __name__ == "__main__":
    play_game()
