import tkinter as tk
import shapes

class main_window:
    def __init__(self, root):
        self.root = root
        self.root.geometry('800x600')
        self.root.title('lab2 - Графічний редактор')
        
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.current_shape_obj = None

        self.N = 108
        self.pcshape = [None] * self.N
        self.shape_count = 0

        self.shape_classes = {
            'Крапка': shapes.Point,
            'Лінія': shapes.Line,
            'Прямокутник': shapes.Rectangle,
            'Еліпс': shapes.Ellipse   
        }

        self.selected_object = tk.StringVar(value="Прямокутник")
        
        self.current_class = self.shape_classes["Прямокутник"]

        self.canvas.bind("<Button-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_holding)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        # меню
        menubar = tk.Menu(self.root)
        menubar.add_command(label='Файл', command=lambda: print("Файл was opened"))

        objects_menu = tk.Menu(menubar, tearoff=0)

        # Створюємо пункти меню, які викликають метод зміни класу
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
            # Зберігаємо об'єкт у статичний масив-історію (якщо є вільне місце)
            if self.shape_count <= self.N:
                self.pcshape[self.shape_count] = self.current_shape_obj
                self.shape_count += 1
                print(f"Фігуру збережено в масив. Загалом об'єктів: {self.shape_count}")
            
            self.current_shape_obj = None


if __name__ == "__main__":
    window = tk.Tk()
    app = main_window(window)
    window.mainloop()