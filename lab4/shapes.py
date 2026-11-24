
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
    def start_drawing(self, event):
        super().start_drawing(event)
        # За варіантом: суцільна лінія чорного кольору
        self.shape_id = self.canvas.create_line(
            self.start_x, self.start_y, event.x, event.y,
            fill='red', width=2
        )

    def draw(self, event):
        if self.shape_id:
            self.canvas.coords(self.shape_id, self.start_x, self.start_y, event.x, event.y)


class Rectangle(Shape):
    def start_drawing(self, event):
        super().start_drawing(event)
        self.shape_id = self.canvas.create_rectangle(
            self.start_x, self.start_y, event.x, event.y,
            outline='black', width=2, fill=''
        )

    def draw(self, event):
        if self.shape_id:
            dx = abs(event.x - self.start_x)
            dy = abs(event.y - self.start_y)
            
            x1 = self.start_x - dx
            y1 = self.start_y - dy
            x2 = self.start_x + dx
            y2 = self.start_y + dy
            self.canvas.coords(self.shape_id, x1, y1, x2, y2)


class Cube(Rectangle, Line):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.rect_ids = []   # [front_id, back_id]
        self.edge_ids = []   # 4 з'єднувальні лінії між гранями

    def get_coords(self, event):
        # Протилежні кути передньої грані: від точки старту до курсора
        fx1, fy1 = self.start_x, self.start_y
        fx2, fy2 = event.x, event.y

        # Зміщення задньої грані вглиб пропорційно розміру фігури
        dx = event.x - self.start_x
        dy = event.y - self.start_y
        offset_x = int(dx * 0.35)
        offset_y = int(dy * 0.35)

        bx1, by1 = fx1 + offset_x, fy1 - abs(offset_y)
        bx2, by2 = fx2 + offset_x, fy2 - abs(offset_y)

        front = (fx1, fy1, fx2, fy2)
        back = (bx1, by1, bx2, by2)

        # 4 ребра між відповідними кутами передньої та задньої граней
        edges = [
            (fx1, fy1, bx1, by1),
            (fx2, fy1, bx2, by1),
            (fx2, fy2, bx2, by2),
            (fx1, fy2, bx1, by2),
        ]
        return front, back, edges

    def start_drawing(self, event):
        Shape.start_drawing(self, event)
        self.rect_ids.clear()
        self.edge_ids.clear()

        front, back, edges = self.get_coords(event)

        # Створюємо передню та задню грані через Rectangle
        for coords in (front, back):
            Rectangle.start_drawing(self, event)
            self.canvas.coords(self.shape_id, *coords)
            self.rect_ids.append(self.shape_id)

        # Створюємо 4 ребра жорсткості/каркасу через Line
        for coords in edges:
            Line.start_drawing(self, event)
            self.canvas.coords(self.shape_id, *coords)
            self.edge_ids.append(self.shape_id)

    def draw(self, event):
        if not self.rect_ids:
            return

        front, back, edges = self.get_coords(event)

        for rect_id, coords in zip(self.rect_ids, (front, back)):
            self.canvas.coords(rect_id, *coords)

        for edge_id, coords in zip(self.edge_ids, edges):
            self.canvas.coords(edge_id, *coords)

class Ellipse(Shape):
    def start_drawing(self, event):
        super().start_drawing(event)
        # За варіантом: ввід від центру, чорний контур із блакитним заповненням
        self.shape_id = self.canvas.create_oval(
            self.start_x, self.start_y, self.start_x, self.start_y,
            outline='black', width=2, fill='lightblue'
        )

    def draw(self, event):
        if self.shape_id:
            self.canvas.coords(self.shape_id, self.start_x, self.start_y, event.x, event.y)


class Line_elips(Line, Ellipse):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.line_id = None
        self.start_oval_id = None
        self.end_oval_id = None
        self.circle_r = 6  # радіус кружечків на кінцях лінії

    def _circle_coords(self, cx, cy):
        r = self.circle_r
        return cx - r, cy - r, cx + r, cy + r

    def start_drawing(self, event):
        Shape.start_drawing(self, event)

        # Створюємо лінію через логіку Line
        Line.start_drawing(self, event)
        self.line_id = self.shape_id

        # Створюємо кружечки на початку та в кінці через логіку Ellipse
        Ellipse.start_drawing(self, event)
        self.start_oval_id = self.shape_id
        self.canvas.coords(self.start_oval_id, *self._circle_coords(self.start_x, self.start_y))

        Ellipse.start_drawing(self, event)
        self.end_oval_id = self.shape_id
        self.canvas.coords(self.end_oval_id, *self._circle_coords(event.x, event.y))

        # Повертаємо line_id як основний shape_id лінії
        self.shape_id = self.line_id

    def draw(self, event):
        if self.line_id:
            self.canvas.coords(self.line_id, self.start_x, self.start_y, event.x, event.y)
        if self.start_oval_id:
            self.canvas.coords(self.start_oval_id, *self._circle_coords(self.start_x, self.start_y))
        if self.end_oval_id:
            self.canvas.coords(self.end_oval_id, *self._circle_coords(event.x, event.y))
