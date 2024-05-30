import tkinter as tk

def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        area = 2 * (a*b + b*c + a*c)
        result_label.config(text=f"Площадь поверхности: {area:.2f} кв. см", fg="green")
    except ValueError:
        result_label.config(text="Пожалуйста, введите числовые значения для всех сторон.", fg="red")

def clear():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Площадь поверхности параллелепипеда")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Введите длины сторон параллелепипеда (в см):").grid(row=0, columnspan=2, pady=5)

tk.Label(frame, text="Длина (см):").grid(row=1, column=0, sticky="e", pady=5)
entry_a = tk.Entry(frame)
entry_a.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Ширина (см):").grid(row=2, column=0, sticky="e", pady=5)
entry_b = tk.Entry(frame)
entry_b.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Высота (см):").grid(row=3, column=0, sticky="e", pady=5)
entry_c = tk.Entry(frame)
entry_c.grid(row=3, column=1, pady=5)

tk.Button(frame, text="Выполнить", command=calculate).grid(row=4, column=0, pady=10, padx=5)
tk.Button(frame, text="Очистить", command=clear).grid(row=4, column=1, pady=10, padx=5)

result_label = tk.Label(frame, text="")
result_label.grid(row=5, columnspan=2, pady=5)

root.mainloop()
