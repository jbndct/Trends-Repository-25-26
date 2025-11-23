import tkinter as tk
from tkinter import messagebox
from controllers.controller import WrestlerController

class MainView(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Wrestler Manager")
    self.geometry("400x300")
    
    tk.Label(self, text="Name").pack()
    self.name_entry = tk.Entry(self)
    self.name_entry.pack()

    tk.Label(self, text="Popularity").pack()
    self.popularity_entry = tk.Entry(self)
    self.popularity_entry.pack()

    tk.Button(self, text = "Add", command=self.add_clicked).pack()
    tk.Button(self, text="Load Wrestlers", command=self.load_clicked).pack()
    
    self.text = tk.Text(self, height=10)
    self.text.pack(fill = "both", expand=True)

    self.controller = WrestlerController(self)

  def get_name(self):
    return self.name_entry.get()
  
  def get_popularity(self):
    return int(self.popularity_entry.get())
  
  def display_wrestlers(self, wrestlers):    
    self.text.delete("1.0", tk.END)

    for wrestler in wrestlers:
      self.text.insert(tk.END, f"{wrestler.id} - {wrestler.name} - {wrestler.popularity}\n")
  
  def show_message(self, msg):
    messagebox.showinfo("Info", msg)
  
  def add_clicked(self):
    self.controller.on_add_wrestler()
  
  def load_clicked(self):
    self.controller.on_load_wrestler()
  



