import random

print("🎲 Welcome to the Dice Roll Game!")
print("................................")

def main_function():
    main = True
    while main:
        users_choice = input("Do you want to play this game? (yes/no): ").strip().lower()

        if users_choice == "yes":
            random_choice = random.randint(1, 6)
            print(f"You rolled a {random_choice} 🎯\n")
        elif users_choice == "no":
            print("Thanks for playing! Goodbye! 👋")
            main = False
        else:
            print("Please type 'yes' or 'no'.\n")

main_function()
