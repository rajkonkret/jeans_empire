import tkinter as tk
from db import get_all_values


class ProductionScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Zarządzanie Produkcją", font=("Helvetica", 24)).pack(pady=20)
        tk.Button(self, text="Wróć do Menu Głównego", command=self.show_main_menu).pack(pady=10)
        tk.Label(self, text="Bieżąca Produkcja", font=("Helvetica", 18)).pack(pady=10)
        self.production_list = tk.Listbox(self)
        self.production_list.pack(pady=10)
        self.update_production_list()

    def show_main_menu(self):
        self.pack_forget()
        self.master.show_main_menu()

    def update_production_list(self):
        values = get_all_values()
        for item in values:
            self.production_list.insert(tk.END, f"{item[1]} - {item[2]}")
