import tkinter as tk
from tkinter import Toplevel, Entry, Button, Label

def run_work1(parent, callback_on_submit):
    # Створення діалогового вікна (Toplevel)
    dialog = Toplevel(parent)
    dialog.title("Робота 1 - Ввід тексту")
    dialog.geometry("300x120")
    dialog.grab_set()  # Модальне вікно

    Label(dialog, text="Введіть текст:").pack(pady=5)
    entry = Entry(dialog, width=30)
    entry.pack(pady=5)

    # Приватна (callback) функція обробки [Так]
    def _on_ok():
        text = entry.get()
        callback_on_submit(text)  # Передаємо результат у головне вікно
        dialog.destroy()           # Автоматично закриваємо вікно

    # Приватна (callback) функція обробки [Відміна]
    def _on_cancel():
        dialog.destroy()

    btn_frame = tk.Frame(dialog)
    btn_frame.pack(pady=5)

    Button(btn_frame, text="Так", width=10, command=_on_ok).pack(side=tk.LEFT, padx=5)
    Button(btn_frame, text="Відміна", width=10, command=_on_cancel).pack(side=tk.LEFT, padx=5)