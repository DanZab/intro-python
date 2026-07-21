import core
import os

def list_flashcards(flashcards):
  # Clear console
  core.clear_screen()

  print(f"{core.colors['GREEN']}Select a flashcard to update: {core.colors['RESET']}")
  # This function displays 10 cards at a time
  cardcount = len(flashcards)
  cardloop = (cardcount // 10)

  # Becuse range() is zero-based I don't need to add 1
  for loop in range(cardloop + 1):
    print(f"Flashcards {loop * 10} of {cardcount}")

    selection_menu = {}
    for i in range(10):
      index = (loop * 10) + i
      if index < cardcount:
        selection_menu[str(index)] = f"{index + 1} - {flashcards[index].id} | {flashcards[index].front}"
        print(selection_menu[str(index)])
    
    print()  # Add a blank line for better readability
    print(f"{core.colors['GREEN']}A{core.colors['RESET']} - Add a new flashcard")
    if index < cardcount - 1:
      print(f"{core.colors['YELLOW']}N{core.colors['RESET']} - Next pagepage")
      
    selection = input(f"Please make a selection using a number above, {core.colors['RED']}X{core.colors['RESET']} to exit: ").upper()
    if selection == "N":
      continue
    elif selection == "X":
      break
    else:
      while selection not in selection_menu:
        selection = input(f"Invalid selection ({core.colors['YELLOW']}{selection}{core.colors['RESET']}), please make a selection using a number above, {core.colors['GREEN']}N{core.colors['RESET']} for next page, {core.colors['RED']}X{core.colors['RESET']} to exit: ").upper()
      
      match selection:
        case "A":
          print(f"{core.colors['GREEN']}You chose to add a new flashcard{core.colors['RESET']}")
          # Call function to add a new flashcard
          add_flashcard()
        case _:
          print(f"You chose {core.colors['RED']}{selection}{core.colors['RESET']}")
          # Return exits the manage cards screen back to the main menu
          modify_flashcard(flashcards[int(selection)])

    # Return exits the manage cards screen back to the main menu
    return flashcards[int(selection)]

def get_id():
  # Generate an ID by taking next available number
  # Gets list of files, sorts it alphabetically, takes the last one and adds 1
  card_dir = "./cards"
  flashcards = os.listdir(card_dir)
  flashcards.sort()
  last_id = flashcards[-1].replace(".txt", "")
  new_id_number = int(last_id) + 1
  new_id = f"{new_id_number:04d}"  # Format as 4-digit number with leading zeros

  return new_id

def display_flashcard(id, front, back, categories):
  categories_str = ", ".join(categories) if categories else "No categories assigned"
  print(f"{core.colors['YELLOW']}{id}{core.colors['RESET']}")
  print(f"Categories: {core.colors['GREEN']}{categories_str}{core.colors['RESET']}")
  print("--------------------")
  print(f"{core.colors['BLUE']}   CARD FRONT:{core.colors['RESET']}")
  print(f"{front}")
  print("--------------------")
  print(f"{core.colors['BLUE']}   CARD BACK:{core.colors['RESET']}")
  print(f"{back}")

def add_flashcard():
  id = get_id()
  confirmed = False
  while confirmed == False:
    core.clear_screen()
    front = core.get_multiline_input(f"{core.colors['GREEN']}Enter the front of the flashcard:{core.colors['RESET']}")
    core.clear_screen()
    back = core.get_multiline_input(f"{core.colors['GREEN']}Enter the back of the flashcard:{core.colors['RESET']}")
    core.clear_screen()
    display_flashcard(id, front, back, [])
    confirm = input(f"Is this correct? (Y/N): ").upper()
    if confirm == "Y":
      confirmed = True
