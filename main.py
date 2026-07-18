import sys

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
  menu_choice = input("Please make a selection using a number above: ")

  while menu_choice not in menu_keys:
    menu_choice = input("Invalid selection ({menu_choice}), please make a selection using a number above:")

  return menu_choice

selection = menu_navigation(menu_items)

match selection:
  case "1":
    # Count how many flashcards are available
    # If 0, prompt to manage
    # Else, choice between study all or categories
    print()
  case "2":
    # Load Manage Card menu
    print()
  case "3":
    # Load Manage Categories menu
    print()
  case "X":
    # End the program
    sys.exit()
