import tkinter as tk
from screens.production import ProductionScreen
from screens.sales import SalesScreen
from screens.marketing import MarketingScreen
from screens.rnd import RnDScreen


class MainMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Jeans Empire", font=("Helvetica", 24)).pack(pady=20)
        tk.Button(self, text="Zarządzanie Produkcją", command=self.show_production).pack(pady=10)
        tk.Button(self, text="Zarządzanie Sprzedażą", command=self.show_sales).pack(pady=10)
        tk.Button(self, text="Marketing", command=self.show_marketing).pack(pady=10)
        tk.Button(self, text="Badania i Rozwój", command=self.show_rnd).pack(pady=10)

    def show_production(self):
        self.pack_forget()
        production_screen = ProductionScreen(self.master)
        production_screen.pack(fill="both", expand=True)

    def show_sales(self):
        self.pack_forget()
        sales_screen = SalesScreen(self.master)
        sales_screen.pack(fill="both", expand=True)

    def show_marketing(self):
        self.pack_forget()
        marketing_screen = MarketingScreen(self.master)
        marketing_screen.pack(fill="both", expand=True)

    def show_rnd(self):
        self.pack_forget()
        rnd_screen = RnDScreen(self.master)
        rnd_screen.pack(fill="both", expand=True)
