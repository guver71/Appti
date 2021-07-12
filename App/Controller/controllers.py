import tkinter as tK
from Model.models import Model
from View.views import View

class Controller():
    def __init__(self):
        self.root = tK.Tk()
        self.model = Model()
        self.view = View(self.root, self)
        self.root.title("Ejemplo MVC")
        
    def btnHandler(self, event):
        self.action()
        
    def action(self):
        self.view.viewPanel.entry.insert({}, self.model.saludar())


        