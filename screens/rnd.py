import tkinter as tk


class RnDScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Badania i Rozwój", font=("Helvetica", 24)).pack(pady=20)
        tk.Button(self, text="Wróć do Menu Głównego", command=self.show_main_menu).pack(pady=10)
        tk.Label(self, text="Projekty B+R", font=("Helvetica", 18)).pack(pady=10)
        tk.Button(self, text="Dodaj Projekt", command=self.add_project).pack(pady=10)
        self.project_list = tk.Listbox(self)
        self.project_list.pack(pady=10)

    def show_main_menu(self):
        self.pack_forget()
        self.master.show_main_menu()

    def add_project(self):
        pass  # Implementacja dodawania projektu
