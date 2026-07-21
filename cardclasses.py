class Category:
  def __init__(self, category:str, cardlist=""):
    self.category = category
    self.filename = f"{category}.txt"
    
    # Create the file to save the category information
    with open(f"./cats/{self.filename}", "w") as file:
      cardliststring = ";".join(cardlist)
      file.write(cardliststring)

  # List the flashcards assigned to this category
  def get_cards(self):
    # Create the file to save the category information
    with open(f"./cats/{self.filename}", "r") as file:
      cards = file.read().split(";")

      if len(cards) > 0:
        return cards
      else:
        return []

  # Assign a card to the category
  def assign_card(self, flashcard):
    cards = self.get_cards()

    if flashcard.id not in cards:    
      # Adds the id of the card to the file list
      with open(f"./cats/{self.filename}", "a") as file:
        file.write(f"{flashcard.id};")
    else:
      print(f"Card already assigned to {self.category}")

  # Remove/Unassign card to category
  def remove_cards(self, flashcard):
    cards = self.get_cards()

    if flashcard.id in cards:
      # Remove card from list and then create string to write to file
      cards.remove(flashcard.id)
      cardstring = ";".join(cards)
      
      # Overwrite the file with list
      with open(f"./cats/{self.filename}", "w") as file:
        file.write(cardstring)

class Flashcard:
  def __init__(self, id: str, front: str, back: str, categories: list):
    self.id = id
    self.front = front
    self.back = back
    self.categories = categories
    
    # Need to generate unique id per card
    # self.id = 
  
  def get_front(self):
    return self.front
  
  def set_front(self, front):
    if len(front) > 0:
      self.front = front

  def get_back(self):
    return self.back
  
  def set_back(self, back):
    if len(back) > 0:
      self.back = back

  def check_category(self, category):
    if category in self.categories:
      return True
    else:
      return False
    
  def add_category(self, category):
    if category not in self.categories:
      self.categories.append(category)

  def remove_category(self, category):
    if category in self.categories:
      self.categories.remove(category)

  def get_categories(self, categories):
    return self.categories
