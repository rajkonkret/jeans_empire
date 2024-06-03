import tkinter as tk
from tkinter import simpledialog
from db import save_project, get_all_projects


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
        self.update_project_list()

    def show_main_menu(self):
        self.pack_forget()
        self.master.show_main_menu()

    def add_project(self):
        name = simpledialog.askstring("Nazwa Projektu", "Podaj nazwę projektu:")
        if name:
            budget = simpledialog.askfloat("Budżet", "Podaj budżet projektu:")
            if budget:
                start_date = simpledialog.askstring("Data Rozpoczęcia", "Podaj datę rozpoczęcia (YYYY-MM-DD):")
                if start_date:
                    end_date = simpledialog.askstring("Data Zakończenia", "Podaj datę zakończenia (YYYY-MM-DD):")
                    if end_date:
                        description = simpledialog.askstring("Opis", "Podaj opis projektu:")
                        if description:
                            save_project(name, budget, start_date, end_date, description)
                            self.update_project_list()

    def update_project_list(self):
        self.project_list.delete(0, tk.END)
        projects = get_all_projects()
        for project in projects:
            self.project_list.insert(tk.END, f"{project[1]} - Budżet: {project[2]}, {project[3]} - {project[4]}")
