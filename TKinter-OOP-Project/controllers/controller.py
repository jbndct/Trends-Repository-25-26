from services.service import WrestlerService

class WrestlerController:
  def __init__(self, view):
    self.view = view
    self.service = WrestlerService()

  def on_add_wrestler(self):
    name = self.view.get_name()
    age = self.view.get_age()
    self.service.add_wrestler(name, age)
    self.view.show_message("Wrestler added!")

  def on_load_wrestler(self):
    wrestlers = self.service.list_wrestlers()
    self.view.display_wrestlers(wrestlers)

