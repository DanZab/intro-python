class flashcard:
  def __init__(self, front: str, back: str, categories: list):
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
  
  