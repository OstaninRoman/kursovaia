from Potok import potokSimulator
from tkinter import *
from tkinter import ttk

A = potokSimulator(10, 0.5, 1.1, 0.5, 0.7, 0.8, 0.4, 0.6, 0.6, 0.4)
MassInitial = A[1]
MassObserved = []
for i in range(len(MassInitial)):
    if MassInitial[i][1] == 'O':
        MassObserved.append(round(MassInitial[i][0], 4))
    else:
        MassObserved.append(' ')
row1 = []
for i in range(len(MassInitial)):
    row1.append(round(MassInitial[i][0], 4))

w = Tk()
w.geometry("800x200")
columns = ['ti']
for i in range(len(MassInitial)):
    columns.append('t%s' %i)
tree = ttk.Treeview(columns=columns, show="headings")
tree.pack(fill=BOTH, side=BOTTOM,  expand=1)
for i in columns:
    tree.heading(i, text=i)
    tree.column(i, width=1)
row1.insert(0, 't исх.п.')
MassObserved.insert(0, 't набл.п.')
table = [row1, MassObserved]
for i in table:
    tree.insert("", END, values=i)
w.mainloop()
