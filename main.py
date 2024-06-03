import tkinter as tk
from screens.main_menu import MainMenu
from db import init_db


class JeansEmpireApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jeans Empire")
        self.geometry("800x600")
        init_db()
        self.show_main_menu()

    def show_main_menu(self):
        main_menu = MainMenu(self)
        main_menu.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = JeansEmpireApp()
    app.mainloop()
