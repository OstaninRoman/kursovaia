from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Числовые значения")
root.geometry("250x200")

# определяем данные для отображения
characteristic = [("M(tau)"), ("Bob"), ("Sam")]

# определяем столбцы
columns = ("name", "age", "email")

tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, expand=1)

# определяем заголовки
tree.heading("name", text="Имя")
tree.heading("age", text="Возраст")
tree.heading("email", text="Email")

# добавляем данные
for  in people:
    tree.insert("", END, values=person)

root.mainloop()