import sys
import os
from cardclasses import Flashcard, Category
import managecards
import core

#import managecards.py

# Support colors in terminal
os.system("color")

# Define Menu items here
# Use dictionary to use keys for easy navigation
# Defining these globally to be accessible from multiple functions
menu_items = {
  "1":"1 - Study",
  "2":"2 - Manage Cards (Create/Edit/Delete)",
  "3":"3 - Manage Categories",
  "X":"X - Exit"
}

def loadCards(card_dir):
  card_array = []
  for file in os.listdir(card_dir):
    path = os.path.join(card_dir, file)
    with open(path, "r") as card_contents:
      id = file.replace(".txt", "")
      card_content = card_contents.read().split("---")
      front = card_content[0].strip("\n")
      back = card_content[1].strip("\n")
      categories = card_content[2].strip("\n").split(";")
      categories = [cat for cat in categories if cat]  # Remove empty strings
      print(f"Card content: {id} |{front} | {back} | {categories}")

      card_array.append(Flashcard(id, front, back, categories))

  return card_array


def onLoad():
  # Load all the flashcards and categories from files
  card_dir = "./cards"
  flashcards = os.listdir(card_dir)

  print(f"Found {len(flashcards)} flashcards")

  card_array = loadCards(card_dir)

  cat_dir = "./cats"
  cats = os.listdir(cat_dir)

  print(f"Found {len(cats)} categories")

  cat_array = []
  for catfile in os.listdir(cat_dir):
    path = os.path.join(cat_dir, catfile)
    with open(path, "r") as cat_contents:
      category = catfile.replace(".txt", "")
      assigned_cards = cat_contents.read().strip("\n").split(";")
      assigned_cards = [card for card in assigned_cards if card]  # Remove empty strings
      print(f"Category: {category}, Assigned Cards: {assigned_cards}")

      cat_array.append(Category(category, assigned_cards))

  return card_array, cat_array

def menu_navigation(menu_items):
  # Clear console
  core.clear_screen()

  print(f"{core.colors['GREEN']}Welcome to the Flashcard Study Program!{core.colors['RESET']}\n")

  # Display menu and prompt
  for item in menu_items:
    print(menu_items[item])

  print()  # Add a blank line for better readability

  # Menu prompt with check for valid selection
  menu_keys = menu_items.keys()
  menu_choice = input("Please make a selection using a number above: ").upper()

  while menu_choice not in menu_keys:
    menu_choice = input(f"Invalid selection ({core.colors["YELLOW"]}{menu_choice}{core.colors["RESET"]}), please make a selection using a number above:").upper()

  return menu_choice

# Loads all the flashcards and categories
all_flashcards, all_categories = onLoad()

selection = ""
while selection != "X":
  selection = menu_navigation(menu_items)

  match selection:
    case "1":
      # Count how many flashcards are available
      # If 0, prompt to manage
      # Else, choice between study all or categories
      print(f"You chose {core.colors["RED"]}1{core.colors["RESET"]}")
    case "2":
      # Load Manage Card menu
      print("You chose 2")
      managecards.list_flashcards(all_flashcards)
    case "3":
      # Load Manage Categories menu
      print("You chose 3")
    case "X":
      # End the program
      core.clear_screen()
      sys.exit()
