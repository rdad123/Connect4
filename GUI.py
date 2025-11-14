"""
    Program - Connect 4
    Name - Robbie D A Dickson
    Student ID - 2935586
    Advanced Programming with Python Assignment
"""
import tkinter as tk
from tkinter import ttk


class GUI:

    def __init__(self, master):
        self.master = master
        self.master.title("Connect 4")
        self.master.geometry("850x680")
        self.master.resizable(False, False)
        self.master.grid_columnconfigure(0, weight=1)
        self._create_MainMenu()

    def _create_MainMenu(self):
        self.main_label = ttk.Label(
            self.master,
            text="Connect 4",
            font=('Inter', 14, 'bold'),
            foreground='#333333'
        )
        self.main_label.grid(row=0, column=0, pady=(30, 20), sticky="n")

        button_frame = ttk.Frame(self.master)
        button_frame.grid(row=1, column=0, pady=10)

        PVP = ttk.Button(
            button_frame,
            text="2 Player",
        )
        PVP.pack(side=tk.LEFT, padx=15, ipadx=10, ipady=5)

        PVE = ttk.Button(
            button_frame,
            text="VS AI",
        )
        PVE.pack(side=tk.LEFT, padx=15, ipadx=10, ipady=5)



