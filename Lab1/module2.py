import tkinter as tk
from tkinter import Toplevel, Scale, Button, Label, HORIZONTAL

def run_work2(parent, callback_on_submit):
    dialog = Toplevel(parent)
    dialog.title("Робота 2 - Выбір числа")
    dialog.geometry("300x140")
    dialog.grab_set()

    Label(dialog, text="Оберіть число (1-100):").pack(pady=5)
    
    # Горизонтальний повзунок від 1 до 100
    scale = Scale(dialog, from_=1, to=100, orient=HORIZONTAL, length=200)
    scale.set(1)
    scale.pack(pady=5)

    def _on_ok():
        value = scale.get()
        callback_on_submit(value)
        dialog.destroy()

    def _on_cancel():
        dialog.destroy()

    btn_frame = tk.Frame(dialog)
    btn_frame.pack(pady=5)

    Button(btn_frame, text="Так", width=10, command=_on_ok).pack(side=tk.LEFT, padx=5)
    Button(btn_frame, text="Відміна", width=10, command=_on_cancel).pack(side=tk.LEFT, padx=5)