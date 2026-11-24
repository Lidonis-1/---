import tkinter as tk
import button_images
import shapes


class MyEditor:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")

        # Словник з посиланнями на класи фігур
        self.shape_classes = {
            "Крапка": shapes.Point,
            "Лінія": shapes.Line,
            "Прямокутник": shapes.Rectangle,
            "Еліпс": shapes.Ellipse,
            "Кубік": shapes.Cube,
            "лінія з кружечками": shapes.Line_elips,
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
                width=24,
                height=24,
                command=lambda n=name: self.set_tool(n),
            )
            btn.pack(side=tk.LEFT, padx=2, pady=2)
            self.toolbar_buttons[name] = btn


        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

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
        menubar.add_command(label="Файл", command=lambda: print("Файл was opened"))

        objects_menu = tk.Menu(menubar, tearoff=0)
        for name in self.shape_classes.keys():
            objects_menu.add_command(
                label=name,
                command=lambda n=name: self.set_tool(n),
            )

        menubar.add_cascade(label="Об'єкти", menu=objects_menu)
        menubar.add_command(label="Довідка", command=lambda: print("Довідка was opened"))
        self.root.config(menu=menubar)

        self.onNotify()

    def set_tool(self, shape_name):
        self.current_shape_name = shape_name
        self.current_class = self.shape_classes[shape_name]
        print(f"Змінено активний клас на: {shape_name} ({self.current_class.__name__})")
        self.onNotify()

    def onNotify(self):
        self.root.title(f"Lab4 - {self.current_shape_name}")

        for name, btn in self.toolbar_buttons.items():
            if name == self.current_shape_name:
                btn.config(relief=tk.SUNKEN, bg="#c8c8c8")
            else:
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

    def destroy(self):
        """Коректне звільнення ресурсів і посилань перед знищенням об'єкта."""
        if hasattr(self, "canvas") and self.canvas.winfo_exists():
            self.canvas.unbind("<Button-1>")
            self.canvas.unbind("<B1-Motion>")
            self.canvas.unbind("<ButtonRelease-1>")
        self.pcshape.clear()
        self.shape_count = 0
        self.current_shape_obj = None
        self.icons.clear()
        self.toolbar_buttons.clear()
        if hasattr(self, "root") and self.root.winfo_exists():
            self.root.config(menu="")
            self.root.destroy()


MainWindow = MyEditor  # Сумісність, якщо десь імпортується стара назва


def run_editor():
    root = tk.Tk()
    editor = MyEditor(root)  # Динамічне створення об'єкта MyEditor

    def handle_close():
        nonlocal editor
        if editor is not None:
            current = editor
            editor = None
            current.destroy()
            del current

    root.protocol("WM_DELETE_WINDOW", handle_close)
    try:
        root.mainloop()
    finally:
        if editor is not None:
            current = editor
            editor = None
            current.destroy()
            del current


if __name__ == "__main__":
    run_editor()