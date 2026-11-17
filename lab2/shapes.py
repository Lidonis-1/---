class Shape:
    def __init__(self, canvas):
        self.canvas = canvas
        self.shape_id = None
        self.start_x = 0
        self.start_y = 0

    def start_drawing(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def draw(self, event):
        pass

    def stop_drawing(self, event):
        pass

class Point(Shape):
    def start_drawing(self, event):
        super().start_drawing(event)
        r = 2  # радіус крапки (діаметр буде 4 пікселі)
        self.shape_id = self.canvas.create_oval(
            self.start_x - r, self.start_y - r,
            self.start_x + r, self.start_y + r,
            fill='black', outline='black'
        )

class Line(Shape):
    """Клас лінії (простіший базовий графічний елемент)"""
    def start_drawing(self, event):
        super().start_drawing(event)
        # За варіантом: суцільна лінія чорного кольору
        self.shape_id = self.canvas.create_line(
            self.start_x, self.start_y, event.x, event.y,
            fill='black', width=2
        )

    def draw(self, event):
        if self.shape_id:
            self.canvas.coords(self.shape_id, self.start_x, self.start_y, event.x, event.y)


class Rectangle(Shape):
    """Прямокутник (наслідує загальні властивості Shape)"""
    def start_drawing(self, event):
        super().start_drawing(event)
        # За варіантом: ввід по двома кутами, чорний контур без заповнення
        self.shape_id = self.canvas.create_rectangle(
            self.start_x, self.start_y, event.x, event.y,
            outline='black', width=2, fill=''
        )

    def draw(self, event):
        if self.shape_id:
            self.canvas.coords(self.shape_id, self.start_x, self.start_y, event.x, event.y)


class Ellipse(Shape):
    """Еліпс (наслідує Shape, реалізує ввід від центру)"""
    def start_drawing(self, event):
        super().start_drawing(event)
        # За варіантом: ввід від центру, чорний контур із блакитним заповненням
        self.shape_id = self.canvas.create_oval(
            self.start_x, self.start_y, self.start_x, self.start_y,
            outline='black', width=2, fill='lightgreen'
        )

    def draw(self, event):
        if self.shape_id:
            # Обчислення координат для розширення еліпса від центру в усі боки
            dx = abs(event.x - self.start_x)
            dy = abs(event.y - self.start_y)
            
            x1 = self.start_x - dx
            y1 = self.start_y - dy
            x2 = self.start_x + dx
            y2 = self.start_y + dy
            
            self.canvas.coords(self.shape_id, x1, y1, x2, y2)