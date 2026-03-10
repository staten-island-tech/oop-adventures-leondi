import tkinter as tk
import time
class clicker:
    def __init__(click, points, mult, auto):
        click.points = points
        click.mult = mult
        click.auto = auto
    def click(click, points, mult):
        points.
class window:
    def __init__(self, root, text, button):
        self.root = root
        self.text = text
        self.button = button
    def createwindow(self, root, text, button, buymenu):
        root = tk.Tk()
        root.geometry("800x800")
        root.title("stupid ahh clicker game")
        root.resizable(False, False)
        root.grid_columnconfigure(0, weight=1)
        
root.mainloop()