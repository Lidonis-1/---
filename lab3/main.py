import tkinter as tk
import shapes

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("lab3")
        self.root.geometry("800x600")

        # 1. СПОЧАТКУ створюємо StringVar, оскільки кнопки до нього звертаються!
        self.selected_object = tk.StringVar(value="Прямокутник")

        # Словник з посиланнями на класи фігур
        self.shape_classes = {
            'Лінія': shapes.Line,
            'Прямокутник': shapes.Rectangle,
            'Еліпс': shapes.Ellipse
        }
        
        # Поточний вибраний клас
        self.current_class = self.shape_classes["Прямокутник"]

        # 2. Меню інструментів (toolbar) та кнопки
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED, bg="#e0e0e0")
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_line = tk.Button(toolbar, text=" — ", font=("Arial", 12), command=lambda: self.set_tool("Лінія"))
        btn_line.pack(side=tk.LEFT, padx=2, pady=2)

        btn_rect = tk.Button(toolbar, text=" ▭ ", font=("Arial", 12), command=lambda: self.set_tool("Прямокутник"))
        btn_rect.pack(side=tk.LEFT, padx=2, pady=2)

        btn_circle = tk.Button(toolbar, text=" ○ ", font=("Arial", 12), command=lambda: self.set_tool("Еліпс"))
        btn_circle.pack(side=tk.LEFT, padx=2, pady=2)

        # 3. Canvas та інші елементи
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.current_shape_obj = None
        self.N = 108
        self.pcshape = [None] * self.N
        self.shape_count = 0

        # Події миші
        self.canvas.bind("<Button-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_holding)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        # Меню зверху
        menubar = tk.Menu(self.root)
        menubar.add_command(label='Файл', command=lambda: print("Файл was opened"))

        objects_menu = tk.Menu(menubar, tearoff=0)
        for name in self.shape_classes.keys():
            objects_menu.add_radiobutton(
                label=name, 
                variable=self.selected_object, 
                value=name,
                command=self.change_tool_class
            )

        menubar.add_cascade(label="Об'єкти", menu=objects_menu)
        menubar.add_command(label='Довідка', command=lambda: print("Довідка was opened"))
        self.root.config(menu=menubar)

    # МЕТОДИ КЛАСУ ПОВИННІ БУТИ НА РІВНІ __init__, а не всередині нього!
    def set_tool(self, shape_name):
        """Встановлює значення StringVar та оновлює активний клас"""
        self.selected_object.set(shape_name)
        self.change_tool_class()

    def change_tool_class(self):
        shape_name = self.selected_object.get()
        self.current_class = self.shape_classes[shape_name]
        print(f"Змінено активний клас на: {shape_name} ({self.current_class.__name__})")

    def on_button_press(self, event):
        if self.shape_count >= 108:
            print("забагато об'єктів")
            return
        self.current_shape_obj = self.current_class(self.canvas)
        self.current_shape_obj.start_drawing(event)

    def on_holding(self, event):
        if self.current_shape_obj:
            self.current_shape_obj.draw(event)

    def on_release(self, event):
        if self.current_shape_obj:
            if self.shape_count < self.N:
                self.pcshape[self.shape_count] = self.current_shape_obj
                self.shape_count += 1
                print(f"Фігуру збережено в масив. Загалом об'єктів: {self.shape_count}")
            self.current_shape_obj = None


if __name__ == "__main__":
    root = tk.Tk()
    window = MainWindow(root)
    root.mainloop()