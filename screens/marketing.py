import tkinter as tk
from tkinter import simpledialog
from db import save_campaign, get_all_campaigns

class MarketingScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Marketing", font=("Helvetica", 24)).pack(pady=20)
        tk.Button(self, text="Wróć do Menu Głównego", command=self.show_main_menu).pack(pady=10)
        tk.Label(self, text="Kampanie Marketingowe", font=("Helvetica", 18)).pack(pady=10)
        tk.Button(self, text="Dodaj Kampanię", command=self.add_campaign).pack(pady=10)
        self.campaign_list = tk.Listbox(self)
        self.campaign_list.pack(pady=10)
        self.update_campaign_list()

    def show_main_menu(self):
        self.pack_forget()
        self.master.show_main_menu()

    def add_campaign(self):
        name = simpledialog.askstring("Nazwa Kampanii", "Podaj nazwę kampanii:")
        if name:
            budget = simpledialog.askfloat("Budżet", "Podaj budżet kampanii:")
            if budget:
                start_date = simpledialog.askstring("Data Rozpoczęcia", "Podaj datę rozpoczęcia (YYYY-MM-DD):")
                if start_date:
                    end_date = simpledialog.askstring("Data Zakończenia", "Podaj datę zakończenia (YYYY-MM-DD):")
                    if end_date:
                        save_campaign(name, budget, start_date, end_date)
                        self.update_campaign_list()

    def update_campaign_list(self):
        self.campaign_list.delete(0, tk.END)
        campaigns = get_all_campaigns()
        for campaign in campaigns:
            self.campaign_list.insert(tk.END, f"{campaign[1]} - Budżet: {campaign[2]}, {campaign[3]} - {campaign[4]}")
