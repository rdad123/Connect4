"""
    Program - Connect 4
    Name - Robbie D A Dickson
    Student ID - 2935586
    Advanced Programming with Python Assignment
"""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from Game import Game

BOARD_ROWS = 6
BOARD_COLS = 7
TILE_SIZE = 80

class GUI:

    def __init__(self, master):
        self.master = master
        self.master.title("Connect 4")
        self.master.geometry("850x680")
        self.master.resizable(True, True)

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

        self.game = Game()
        self.log_area = None
        self.game_mode = ""

        self.board_canvas = None
        self.drop_buttons = []

        self.images = {}
        self._load_tile_images()

        self._create_MainMenu()

    def _load_tile_images(self):
        try:
            blank_pil = Image.open("blank.png")
            red_pil = Image.open("redtile.png")
            blue_pil = Image.open("bluetile.png")

            self.images['⬛'] = ImageTk.PhotoImage(blank_pil)
            self.images['🔴'] = ImageTk.PhotoImage(red_pil)
            self.images['🔵'] = ImageTk.PhotoImage(blue_pil)

            self._pil_images = {
                '⬛': blank_pil,
                '🔴': red_pil,
                '🔵': blue_pil
            }

        except FileNotFoundError as e:
            tk.messagebox.showerror("Image Error", f"Missing image file: {e.filename}\nPlease ensure 'blank.png', 'redtile.png', and 'bluetile.png' are in the same directory as the script.")
            self.master.destroy()
        except Exception as e:
            tk.messagebox.showerror("Image Error", f"Failed to load images: {e}")
            self.master.destroy()

    def _clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        self.drop_buttons.clear()

    def _create_MainMenu(self):
        self._clear_window()

        self.game.reset_game()

        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_rowconfigure(1, weight=0)
        self.master.grid_rowconfigure(2, weight=1)

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
            command=lambda: self._create_GameView("2 Player", 0)
        )
        PVP.pack(side=tk.LEFT, padx=15, ipadx=10, ipady=5)

        PVE = ttk.Button(
            button_frame,
            text="VS AI",
            command=self._create_DifficultySelect
        )
        PVE.pack(side=tk.LEFT, padx=15, ipadx=10, ipady=5)

    def _create_DifficultySelect(self):
        """Creates a screen for selecting the AI difficulty."""
        self._clear_window()

        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_rowconfigure(1, weight=0)
        self.master.grid_rowconfigure(2, weight=1)

        ttk.Label(
            self.master,
            text="Select AI Difficulty",
            font=('Inter', 20, 'bold'),
            foreground='#333333'
        ).grid(row=0, column=0, pady=(150, 30), sticky="s")

        button_frame = ttk.Frame(self.master)
        button_frame.grid(row=1, column=0, pady=10, sticky="n")

        ttk.Button(
            button_frame,
            text="Easy (Random)",
            command=lambda: self._create_GameView("VS AI (Easy)", 1)
        ).pack(side=tk.LEFT, padx=15, ipadx=10, ipady=5)

        ttk.Button(
            button_frame,
            text="Medium",
            command=lambda: self._create_GameView("VS AI (Medium)", 2)
        ).pack(side=tk.LEFT, padx=15, ipadx=10, ipady=5)

        ttk.Button(
            button_frame,
            text="Hard",
            command=lambda: self._create_GameView("VS AI (Hard)", 3)
        ).pack(side=tk.LEFT, padx=15, ipadx=10, ipady=5)

        ttk.Button(
            self.master,
            text="< Back",
            command=self._create_MainMenu
        ).grid(row=2, column=0, pady=(50, 10), sticky="n")

    def _create_GameView(self, game_mode, difficulty):
        self._clear_window()
        self.game_mode = game_mode

        self.game.reset_game(difficulty)

        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=0)
        self.master.grid_rowconfigure(3, weight=4)

        top_button_frame = ttk.Frame(self.master)
        top_button_frame.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="ne")

        back_button = ttk.Button(
            top_button_frame,
            text="< Back to Menu",
            command=self._create_MainMenu
        )
        back_button.pack(padx=0, pady=0)

        log_frame = ttk.Frame(self.master)
        log_frame.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="nsew")
        log_frame.grid_columnconfigure(0, weight=1)
        log_frame.grid_rowconfigure(1, weight=1)

        player_token = self.game.get_current_player_token()
        log_label = ttk.Label(log_frame, text=f"Connect 4 - Mode: {game_mode}", font=('Inter', 12, 'bold'))
        log_label.grid(row=0, column=0, sticky="w")

        self.log_area = tk.Text(log_frame, height=5, font=('Consolas', 10), relief=tk.SUNKEN, wrap=tk.WORD, state=tk.DISABLED)
        self.log_area.grid(row=1, column=0, sticky="nsew", pady=(5, 0))

        scrollbar = ttk.Scrollbar(log_frame, command=self.log_area.yview)
        scrollbar.grid(row=1, column=1, sticky='nse')
        self.log_area['yscrollcommand'] = scrollbar.set

        buttons_container = ttk.Frame(self.master)
        buttons_container.grid(row=2, column=0, pady=10, sticky="n")

        for i in range(BOARD_COLS):
            col_num = i
            btn = ttk.Button(
                buttons_container,
                text=f"Drop {col_num + 1}",
                width=10,
                command=lambda c=col_num: self.on_column_select(c)
            )
            btn.pack(side=tk.LEFT, padx=5)
            self.drop_buttons.append(btn)

        self.board_canvas = tk.Canvas(
            self.master,
            bg="#004792",
            highlightthickness=0
        )
        self.board_canvas.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="nsew")

        self.board_canvas.bind("<Configure>", self._on_canvas_resize)

        self.master.update_idletasks()
        self._update_board_display()

        self._toggle_controls(True)
        self.log_message(f"Game started in {game_mode} mode.\nPlayer {self.game.current_player_num} {self.game.get_current_player_token()}'s turn. Select a column to drop a piece.")

        if difficulty > 0 and self.game.current_player_num == 2:
            self._handle_ai_turn()

    def _toggle_controls(self, enable):
        state = 'normal' if enable else 'disabled'
        for btn in self.drop_buttons:
            btn.config(state=state)

    def log_message(self, message):
        self.log_area.config(state=tk.NORMAL)
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)
        self.log_area.config(state=tk.DISABLED)

    def _on_canvas_resize(self, event):
        if event.width == 0 or event.height == 0:
            return
        self._update_board_display()

    def _update_board_display(self):
        if not self.board_canvas or not self.images:
            return

        canvas_width = self.board_canvas.winfo_width()
        canvas_height = self.board_canvas.winfo_height()

        if canvas_width == 0 or canvas_height == 0:
            return

        self.board_canvas.delete("all")

        tile_width = canvas_width // BOARD_COLS
        tile_height = canvas_height // BOARD_ROWS
        actual_tile_size = min(tile_width, tile_height)

        start_x = (canvas_width - actual_tile_size * BOARD_COLS) / 2
        start_y = (canvas_height - actual_tile_size * BOARD_ROWS) / 2

        current_board = self.game.get_board_state()

        resized_images = {}
        for key, pil_img in self._pil_images.items():
            if actual_tile_size <= 0: return

            resized_pil = pil_img.resize((actual_tile_size, actual_tile_size), Image.LANCZOS)
            resized_images[key] = ImageTk.PhotoImage(resized_pil)

        self.images = resized_images

        for r in range(BOARD_ROWS):
            for c in range(BOARD_COLS):
                token_type = current_board[r][c]
                image_to_draw = self.images.get(token_type)

                if image_to_draw:
                    x1 = int(start_x + c * actual_tile_size)
                    y1 = int(start_y + r * actual_tile_size)

                    self.board_canvas.create_image(x1, y1, anchor=tk.NW, image=image_to_draw)


    def _handle_game_end(self):
        winner = "Player 1 🔴" if self.game.get_winner() == 1 else "Player 2 🔵"
        self.log_message(f"\n*** GAME OVER! {winner} WINS! ***")
        self._toggle_controls(False)

    def _handle_ai_turn(self):
        self._toggle_controls(False)
        self.log_message("AI is thinking...")

        self.master.after(500, self._execute_ai_move)

    def _execute_ai_move(self):
        ai_move_col = self.game.AI_Move()

        if ai_move_col != -1:
            self._update_board_display()
            self.log_message(f"> AI {self.game.board_manager.PLAYER2_TOKEN} dropped piece in Column {ai_move_col + 1}.")

            if self.game.get_winner():
                self._handle_game_end()
            else:
                self._toggle_controls(True)
                next_player_token = self.game.get_current_player_token()
                self.log_message(f"> It is now Player {self.game.current_player_num} {next_player_token}'s turn.")
        else:
            self.log_message("AI failed to make a move or board is full.")
            self._toggle_controls(True)


    def on_column_select(self, column_index):
        if not self.game.is_in_progress():
            self.log_message("\n*** Game is over! Go back to menu to start a new game. ***")
            return

        if self.game.DIFFICULTY != 0 and self.game.current_player_num != 1:
            self.log_message("> It is the AI's turn! Please wait.")
            return

        mover_num = self.game.current_player_num
        mover_token = self.game.get_current_player_token()

        move_successful = self.game.make_move(column_index)

        if move_successful:
            self.log_message(f"> Player {mover_num} {mover_token} dropped piece in Column {column_index + 1}.")
            self._update_board_display()

            if self.game.get_winner():
                self._handle_game_end()
            elif self.game.DIFFICULTY != 0:
                self._handle_ai_turn()
            else:
                next_player_token = self.game.get_current_player_token()
                self.log_message(f"> It is now Player {self.game.current_player_num} {next_player_token}'s turn.")

        else:
            self.log_message(f"> Column {column_index + 1} is full! Try another column.")
