import tkinter as tk

def create_icons():
        
    icons = {}

    # 1. Крапка (жирна точка 4x4 по центру 16x16)
    img_point = tk.PhotoImage(width=16, height=16)
    img_point.put("black", to=(6, 6, 10, 10))
    icons["Крапка"] = img_point

    # 2. Лінія (діагональна червона лінія товщиною 2px)[cite: 1]
    img_line = tk.PhotoImage(width=16, height=16)
    for i in range(2, 14):
        img_line.put("red", to=(i, i, i+2, i+2))
    icons["Лінія"] = img_line

    # 3. Прямокутник (червоний контур товщиною 2px)[cite: 1]
    img_rect = tk.PhotoImage(width=16, height=16)
    img_rect.put("black", to=(2, 3, 14, 5))    # верх
    img_rect.put("black", to=(2, 11, 14, 13))  # низ
    img_rect.put("black", to=(2, 3, 4, 13))    # ліво
    img_rect.put("black", to=(12, 3, 14, 13))  # право
    icons["Прямокутник"] = img_rect

    # 4. Еліпс (червоний овал)[cite: 1]
    img_ellipse = tk.PhotoImage(width=16, height=16)
    # Малюємо контур еліпса за формулою
    for x in range(16):
        for y in range(16):
            # Нормалізовані координати від центру (7.5, 7.5)
            dx = (x - 7.5) / 6.0
            dy = (y - 7.5) / 4.5
            dist = dx*dx + dy*dy
            if 0.65 <= dist <= 1.15:
                img_ellipse.put("black", to=(x, y))
    icons["Еліпс"] = img_ellipse


    img_cube = tk.PhotoImage(width=16, height=16)

    # Задня грань (зміщена вправо-вгору)
    img_cube.put("black", to=(6, 2, 14, 3))
    img_cube.put("black", to=(6, 9, 14, 10))
    img_cube.put("black", to=(6, 2, 7, 10))
    img_cube.put("black", to=(13, 2, 14, 10))

    # Передня грань (зліва-знизу)
    img_cube.put("black", to=(2, 6, 10, 7))
    img_cube.put("black", to=(2, 13, 10, 14))
    img_cube.put("black", to=(2, 6, 3, 14))
    img_cube.put("black", to=(9, 6, 10, 14))

    # Червоні з'єднувальні ребра (як на полотні)
    for step in range(5):
        img_cube.put("red", to=(2 + step, 6 - step, 3 + step, 7 - step))
        img_cube.put("red", to=(9 + step, 6 - step, 10 + step, 7 - step))
        img_cube.put("red", to=(9 + step, 13 - step, 10 + step, 14 - step))
        img_cube.put("red", to=(2 + step, 13 - step, 3 + step, 14 - step))

    icons["Кубік"] = img_cube

    img_segment = tk.PhotoImage(width=16, height=16)
    x0, y0 = 3, 12
    x1, y1 = 12, 3

    steps = max(abs(x1 - x0), abs(y1 - y0))
    for step in range(steps + 1):
        t = step / steps if steps else 0
        px = round(x0 + (x1 - x0) * t)
        py = round(y0 + (y1 - y0) * t)
        img_segment.put("red", to=(px, py, px + 2, py + 2))

    # Кружечки (3x3 з заокругленими кутами) навколо початкової та кінцевої точок
    for vx, vy in ((x0, y0), (x1, y1)):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if abs(dx) == 1 and abs(dy) == 1:
                    continue
                img_segment.put("black", to=(vx + dx, vy + dy))

   

    icons["лінія з кружечками"] = img_segment


    return icons