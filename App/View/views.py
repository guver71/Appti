import tkinter as tK

class View():
    def __init__(self, master, controller):
        self.controller = controller(master)
        self.frame.pack()
        self.frame = tK.Frame
        self.viewPanel = ViewPanel(master, controller)
        pass

class ViewPanel():
    def __init__(self, root, controller):
        self.controller = controller
        self.framePanel = tK.Frame(root)
        self.framePanel.pack()
        self.label = tK.Label(self, framePanel, text="Resultado: ")
        self.label.pack()
        self.entry = tK.Entry(self, framePanel)
        self.entry.pack()
        self.btn = tK.Button(self, framePanel, text="Welcome")
        self.btn.pack()
        self.btn.bind("<Button>", controller, binHandler)



        
