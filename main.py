 # main.py

from gui import InterfataGUI
import tkinter as tk
from utils import curs_valutar
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfataGUI(root)
    root.mainloop()
   
    print("Curs EUR:", curs_valutar("EUR"))  # Ar trebui să returneze ~4.9
    print("Curs USD:", curs_valutar("USD"))  # Ar trebui să returneze ~4.5