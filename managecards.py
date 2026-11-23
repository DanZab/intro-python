import core
import os
from cardclasses import Flashcard

def list_flashcards(flashcards):
  # This function displays 10 cards at a time
  showlist = True

  while showlist == True:
    # Clear console
    core.clear_screen()

    cardcount = len(flashcards)
    cardloop = (cardcount // 10)

    print(f"{core.colors['GREEN']}Select a flashcard to update: {core.colors['RESET']}")

    # Becuse range() is zero-based I don't need to add 1
    for loop in range(cardloop + 1):
      print(f"Flashcards {(loop * 10) + 1}-{(loop + 1) * 10} of {cardcount}")

      selection_menu = {"A": "New", "X": "Exit"}
      for i in range(10):
        index = (loop * 10) + i
        if index < cardcount:
          selection_menu[str(index + 1)] = flashcards[index].id
          print(f"{index + 1} - {flashcards[index].id} | {flashcards[index].front}")
      
      print()  # Add a blank line for better readability
      print(f"{core.colors['GREEN']}A{core.colors['RESET']} - Add a new flashcard")
      if index < cardcount - 1:
        print(f"{core.colors['YELLOW']}N{core.colors['RESET']} - Next pagepage")
        
      selection = input(f"Please make a selection using a number above, {core.colors['RED']}X{core.colors['RESET']} to exit: ").upper()
      if selection == "N":
        continue
      else:
        while selection not in selection_menu:
          print(f"You chose {selection}")
          selection = input(f"Invalid selection ({core.colors['YELLOW']}{selection}{core.colors['RESET']}), please make a selection using a number above, {core.colors['GREEN']}N{core.colors['RESET']} for next page, {core.colors['RED']}X{core.colors['RESET']} to exit: ").upper()
        
        match selection:
          case "A":
            print(f"{core.colors['GREEN']}You chose to add a new flashcard{core.colors['RESET']}")
            # Call function to add a new flashcard
            new_card = add_flashcard()
            # Add new card to menu so it shows up
            flashcards.append(new_card)
          case "X":
            showlist = False
          case _:
            print(f"You chose {core.colors['RED']}{selection}{core.colors['RESET']}")
            # show inputs to update card, then pass new values into menu array
            updated_card = modify_flashcard(flashcards[int(selection) - 1])
            flashcards[int(selection) - 1] = updated_card
    

  # Return exits the manage cards screen back to the main menu
  return 

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
    categories = []
    display_flashcard(id, front, back, categories)
    confirm = input(f"Is this correct? (Y/N): ").upper()
    if confirm == "Y":
      with open(f"cards\{id}.txt", "w", encoding="utf-8") as file:
        file.write(f"{front}\n")
        file.write("---\n")
        file.write(f"{back}\n")
        file.write("---\n")
        file.write(";".join(categories))
        file.close()
      confirmed = True

  return Flashcard(id, front, back, categories)

def modify_flashcard(flashcard):
  id = flashcard.id
  front = flashcard.front
  back = flashcard.back
  categories = flashcard.categories

  confirmed = False
  while confirmed == False:
    core.clear_screen()
    print(f"{core.colors['GREEN']}Existing front of card:{core.colors['RESET']}")
    print(front, "\n")
    newfront = core.get_multiline_input(f"{core.colors['GREEN']}Enter the new front of the flashcard (leave blank for no changes):{core.colors['RESET']}")
    if newfront != front and newfront != "":
      front = newfront
    core.clear_screen()
    print(f"{core.colors['GREEN']}Existing back of card:{core.colors['RESET']}")
    print(back, "\n")
    newback = core.get_multiline_input(f"{core.colors['GREEN']}Enter the new back of the flashcard (leave blank for no changes):{core.colors['RESET']}")
    if newback != back and newback != "":
      back = newback
    core.clear_screen()
    categories = []
    display_flashcard(id, front, back, categories)
    confirm = input(f"Is this correct? (Y/N): ").upper()
    if confirm == "Y":
      with open(f"cards\{id}.txt", "w", encoding="utf-8") as file:
        file.write(f"{front}\n")
        file.write("---\n")
        file.write(f"{back}\n")
        file.write("---\n")
        file.write(";".join(categories))
        file.close()
      confirmed = True

  return Flashcard(id, front, back, categories)

  
