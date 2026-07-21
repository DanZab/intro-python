import os

# Define ANSI color codes
colors = {
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "RESET": "\033[0m"
}

def clear_screen():
    # 'nt' means Windows, otherwise it's likely Mac or Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def get_multiline_input(prompt):
    # Allows user to input multiple lines of text until they press ENTER on a new line
    print(prompt)
    print(f"Press {colors['YELLOW']}ENTER{colors['RESET']} on a new line to finish.")
    
    lines = []
    while True:
        line = input()
        if not line:  
            break
        lines.append(line)
    return "\n".join(lines)

def onLoad():
  # Load all the flashcards and categories from files
  card_dir = "./cards"
  flashcards = os.listdir(card_dir)

  print(f"Found {len(flashcards)} flashcards")

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
