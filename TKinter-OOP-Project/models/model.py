INTENSITY_MAP = {
    "Low": 2,
    "Medium": 4,
    "High": 7,
    "Signature": 8,  
    "Finisher": 10    
    }

class Wrestler:
  def __init__(self, wrestler_id=None, wrestler_name="", wrestler_popularity=0):
    self.wrestler_id = wrestler_id
    self.wrestler_name = wrestler_name
    self.wrestler_popularity = int(wrestler_popularity)
  
  def __str__(self):
    return f"{self.wrestler_name}, Popularity: {self.wrestler_popularity}"

class Move:
  def __init__(self, move_id=None, move_name="", move_level=""):
    self.move_id = move_id
    self.move_name = move_name
    self.move_level = move_level

  def __str__(self):
    return f"{self.move_name}, Move Level: {self.move_level}"
  
  @property
  def excitement_value(self):
    return INTENSITY_MAP.get(self.move_level, 1)

class Signature(Move):
  def __init__(self, move_id, move_name, move_level, move_owner_id=""):
    super().__init__(move_id, move_name, move_level)
    self.move_owner_id = move_owner_id

class Finisher(Signature):
  def __init__(self, move_id, move_name, move_level, move_owner_id):
    super().__init__(move_id, move_name, move_owner_id)
    self.move_level = "Finisher"

class Match:
  def __init__(self, wrestler_a, wrestler_b):
      self.wrestler_a = wrestler_a
      self.wrestler_b = wrestler_b
      self.script = [] 
      self.final_rating = 0.0
      self.logs = []