import tkinter as tk
import shapes

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")

        # Словник з посиланнями на класи фігур
        self.shape_classes = {
            'Крапка': shapes.Point,
            'Лінія': shapes.Line,
            'Прямокутник': shapes.Rectangle,
            'Еліпс': shapes.Ellipse
        }
        
        # Поточний вибраний клас та назва (без StringVar)
        self.current_shape_name = "Прямокутник"
        self.current_class = self.shape_classes[self.current_shape_name]
        self.root.title(f"lab3 - {self.current_shape_name}")

        # 2. Меню інструментів (toolbar) та кнопки
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED, bg="#e0e0e0")
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_point = tk.Button(toolbar, text=" · ", font=("Arial", 12), command=lambda: self.set_tool("Крапка"))
        btn_point.pack(side=tk.LEFT, padx=2, pady=2)

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
        self.N = 109
        self.pcshape = [] 
        self.shape_count = 0

        # Події миші
        self.canvas.bind("<Button-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_holding)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        # Меню зверху
        menubar = tk.Menu(self.root)
        menubar.add_command(label='Файл', command=lambda: print("Файл was opened"))

        objects_menu = tk.Menu(menubar, tearoff=0)
        # Використовуємо add_command замість add_radiobutton, щоб прибрати позначки
        for name in self.shape_classes.keys():
            objects_menu.add_command(
                label=name, 
                command=lambda n=name: self.set_tool(n)
            )

        menubar.add_cascade(label="Об'єкти", menu=objects_menu)
        menubar.add_command(label='Довідка', command=lambda: print("Довідка was opened"))
        self.root.config(menu=menubar)

    def set_tool(self, shape_name):
        """Встановлює активний клас фігури та оновлює заголовок вікна"""
        self.current_shape_name = shape_name
        self.current_class = self.shape_classes[shape_name]
        self.root.title(f"lab3 - {shape_name}")
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
            if self.shape_count <= self.N:
                self.pcshape.append(self.current_shape_obj)
                self.shape_count += 1
                print(f"Фігуру збережено в масив. Загалом об'єктів: {self.shape_count}")
            self.current_shape_obj = None


if __name__ == "__main__":
    root = tk.Tk()
    window = MainWindow(root)
    root.mainloop()