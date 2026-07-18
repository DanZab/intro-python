import sys
import os

# Support colors in terminal
os.system("color")
# Define ANSI color codes
colors = {
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "RESET": "\033[0m"
}

# Define Menu items here
# Use dictionary to use keys for easy navigation
# Defining these globally to be accessible from multiple functions
menu_items = {
  "1":"1 - Study",
  "2":"2 - Manage Cards (Create/Edit/Delete)",
  "3":"3 - Manage Categories",
  "X":"Exit"
}

def menu_navigation(menu_items):

  # Display menu and prompt
  for item in menu_items:
    print(menu_items[item])

  # Menu prompt with check for valid selection
  menu_keys = menu_items.keys()
  menu_choice = input("Please make a selection using a number above: ").upper()

  while menu_choice not in menu_keys:
    menu_choice = input(f"Invalid selection ({colors["YELLOW"]}{menu_choice}{colors["RESET"]}), please make a selection using a number above:").upper()

  return menu_choice

selection = menu_navigation(menu_items)

match selection:
  case "1":
    # Count how many flashcards are available
    # If 0, prompt to manage
    # Else, choice between study all or categories
    print(f"You chose {colors["RED"]}1{colors["RESET"]}")
  case "2":
    # Load Manage Card menu
    print("You chose 2")
  case "3":
    # Load Manage Categories menu
    print("You chose 3")
  case "X":
    # End the program
    sys.exit()
