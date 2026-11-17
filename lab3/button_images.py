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

    return icons