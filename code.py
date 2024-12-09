import tkinter as tk
from tkinter import messagebox

class InsuranceCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Страховой калькулятор")
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.root, text="Стоимость имущества (₽):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.property_value_entry = tk.Entry(self.root)
        self.property_value_entry.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(self.root, text="Тип имущества:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.property_type = tk.StringVar(value="Недвижимость")
        tk.OptionMenu(self.root, self.property_type, "Недвижимость", "Транспорт", "Оборудование").grid(row=1, column=1, padx=10, pady=10)
        tk.Label(self.root, text="Уровень покрытия:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.coverage_level = tk.StringVar(value="Базовый")
        tk.OptionMenu(self.root, self.coverage_level, "Базовый", "Расширенный", "Премиум").grid(row=2, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Рассчитать стоимость", command=self.calculate_insurance).grid(row=3, column=0, columnspan=2, pady=10)
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12, "bold"))
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)
    def calculate_insurance(self):
        try:
            property_value = float(self.property_value_entry.get())
            property_type = self.property_type.get()
            coverage_level = self.coverage_level.get()
            base_rate = 0.01  
            if property_type == "Транспорт":
                base_rate += 0.005  
            elif property_type == "Оборудование":
                base_rate += 0.007  
            if coverage_level == "Расширенный":
                base_rate *= 1.2  
            elif coverage_level == "Премиум":
                base_rate *= 1.5
            insurance_cost = property_value * base_rate
            self.result_label.config(text=f"Стоимость страховки: {insurance_cost:.2f} ₽")
        except ValueError:
            messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректную стоимость имущества.")

root = tk.Tk()
app = InsuranceCalculator(root)
root.mainloop()