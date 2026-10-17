import tkinter as tk
import module1
import module2

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Лабораторна робота 1")
        self.root.geometry("400x200")

        # Мітка для відображення результату
        self.result_label = tk.Label(root, text="Результат з'явиться тут", font=("Arial", 12))
        self.result_label.pack(expand=True)

        # Створення головного меню
        menubar = tk.Menu(self.root)
        
        # Додавання пунктів Робота1 та Робота2
        menubar.add_command(label="Робота1", command=self.open_work1)
        menubar.add_command(label="Робота2", command=self.open_work2)

        self.root.config(menu=menubar)

    def update_result(self, value):
        self.result_label.config(text=f"Отриманий результат: {value}")

    def open_work1(self):
        # Виклик функції з окремого модуля module1
        module1.run_work1(self.root, self.update_result)

    def open_work2(self):
        # Виклик функції з окремого модуля module2
        module2.run_work2(self.root, self.update_result)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()