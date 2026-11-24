import tkinter as tk
import shapes
import button_images
from tkinter import Scale, HORIZONTAL

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
        
        self.current_shape_name = "Прямокутник"
        self.current_class = self.shape_classes[self.current_shape_name]

        # Завантажуємо іконки
        self.icons = button_images.create_icons()

        # 1. Панель інструментів (toolbar)
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED, bg="#e0e0e0")
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.toolbar_buttons = {}
        for name in self.shape_classes.keys():
            btn = tk.Button(
                toolbar, 
                image=self.icons[name], 
                command=lambda n=name: self.set_tool(n)
            )
            btn.pack(side=tk.LEFT, padx=2, pady=2)
            self.toolbar_buttons[name] = btn

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='white')
        

        self.current_shape_obj = None
        self.N = 109
        self.pcshape = [] 
        self.shape_count = 0

        # Події миші
        self.canvas.bind("<Button-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_holding)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        # 3. Верхнє меню (menubar) без позначок активності
        menubar = tk.Menu(self.root)
        menubar.add_command(label='Файл', command=lambda: print("Файл was opened"))

        objects_menu = tk.Menu(menubar, tearoff=0)
        for name in self.shape_classes.keys():
            objects_menu.add_command(
                label=name, 
                command=lambda n=name: self.set_tool(n)
            )

        menubar.add_cascade(label="Об'єкти", menu=objects_menu)
        menubar.add_command(label='Довідка', command=lambda: print("Довідка was opened"))
        self.root.config(menu=menubar)


        self.scale = Scale(self.root, from_=1, to=100, orient=HORIZONTAL)
        self.scale.pack()

        # Викликаємо onNotify при старті, щоб "втиснути" кнопку початкового інструменту
        self.onNotify()

    def set_tool(self, shape_name):
        self.current_shape_name = shape_name
        self.current_class = self.shape_classes[shape_name]
        print(f"Змінено активний клас на: {shape_name} ({self.current_class.__name__})")
        self.onNotify()

    def onNotify(self):
        self.root.title(f"lab3 - {self.current_shape_name}")
        
        for name, btn in self.toolbar_buttons.items():
            if name == self.current_shape_name:
                # Активна кнопка виглядає натиснутою і трохи темнішою
                btn.config(relief=tk.SUNKEN, bg="#c8c8c8")
            else:
                # Неактивні кнопки у звичайному стані
                btn.config(relief=tk.RAISED, bg="#f0f0f0")

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