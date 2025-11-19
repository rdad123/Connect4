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
        self.master.resizable(True, True)

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

        self._create_MainMenu()

    def _clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def _create_MainMenu(self):
        self._clear_window()

        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_rowconfigure(1, weight=0)

        self.main_label = ttk.Label(
            self.master,
            text="Connect 4",
            font=('Inter', 24, 'bold'),
            foreground='#333333'
        )
        self.main_label.grid(row=0, column=0, pady=(150, 40), sticky="s")

        button_frame = ttk.Frame(self.master)
        button_frame.grid(row=1, column=0, pady=10, sticky="n")

        PVP = ttk.Button(
            button_frame,
            text="2 Player",
            command=lambda: self._create_GameView("2 Player")
        )
        PVP.pack(side=tk.LEFT, padx=15, ipadx=10, ipady=5)

        PVE = ttk.Button(
            button_frame,
            text="VS AI",
            command=lambda: self._create_GameView("VS AI")
        )
        PVE.pack(side=tk.LEFT, padx=15, ipadx=10, ipady=5)

    def _create_GameView(self, game_mode):
        self._clear_window()

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=0)
        self.master.grid_rowconfigure(2, weight=4)

        log_frame = ttk.Frame(self.master)
        log_frame.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")
        log_frame.grid_columnconfigure(0, weight=1)
        log_frame.grid_rowconfigure(0, weight=1)

        log_label = ttk.Label(log_frame, text=f"Connect 4 - Mode: {game_mode}", font=('Inter', 12, 'bold'))
        log_label.grid(row=0, column=0, sticky="w")

        self.log_area = tk.Text(log_frame, height=5, font=('Consolas', 10), relief=tk.SUNKEN)
        self.log_area.grid(row=1, column=0, sticky="nsew", pady=(5, 0))
        self.log_area.insert("1.0", f"Game started in {game_mode} mode.\nSelect a column to drop a piece.")

        scrollbar = ttk.Scrollbar(log_frame, command=self.log_area.yview)
        scrollbar.grid(row=1, column=1, sticky='nse')
        self.log_area['yscrollcommand'] = scrollbar.set

        buttons_container = ttk.Frame(self.master)
        buttons_container.grid(row=1, column=0, pady=10, sticky="n")

        for i in range(7):
            col_num = i + 1
            btn = ttk.Button(
                buttons_container,
                text=f"Drop {col_num}",
                width=10,
                command=lambda c=col_num: self.on_column_select(c)
            )
            btn.pack(side=tk.LEFT, padx=5)

        self.board_canvas = tk.Canvas(
            self.master,
            bg="#003366",
            relief=tk.SUNKEN
        )
        self.board_canvas.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="nsew")

        back_button = ttk.Button(
            self.master,
            text="< Back to Menu",
            command=self._create_MainMenu
        )
        back_button.grid(row=3, column=0, pady=(0, 10), sticky="s")


    def on_column_select(self, column_number):
        log_message = f"\n> Column {column_number} selected. Placing piece..."
        self.log_area.insert(tk.END, log_message)
        self.log_area.see(tk.END)
