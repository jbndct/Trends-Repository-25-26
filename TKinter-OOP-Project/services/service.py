from models.model import Wrestler
from repositories.repo import WrestlerRepository 

class WrestlerService:
  def __init__(self):
    self.repo = WrestlerRepository()

  def add_wrestler(self, name, age):
    if not name:
      raise ValueError("Name cannot be empty.")
    
    if age <=0:
      raise ValueError("Age must be a positive integer.")
    
    wrestler = Wrestler(name=name, age=age)
    self.repo.create(wrestler)
  
  def list_wrestlers(self):
    return self.repo.get_all()
  
  
  