import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk

f = open('Exp5.txt', 'r')
MassM_eta2 = []
x1 = []
nam = f.readline()
MassM_eta2_1 = list(map(float, nam.split()))
nam = f.readline()
MassM_eta2_2 = list(map(float, nam.split()))
for i in range(1, 11, 1):
    i = i/100
    x1.append(i)

fig, (ax1, ax2) = plt.subplots(2)
ax1.scatter(x1, MassM_eta2_1)
ax1.set_xlabel("a2")
ax1.set_ylabel("M(eta2)", rotation=0, labelpad=20)
x2 = []
for i in range(5, 55, 5):
    i = i/10
    x2.append(i)
ax2.scatter(x2, MassM_eta2_2)
ax2.set_xlabel("a2")
ax2.set_ylabel("M(eta2)", rotation=0, labelpad=20)
plt.show()

w = Tk()
w.geometry("800x600")
x1.insert(0, 'a2')
tree1 = ttk.Treeview(columns=x1, show="headings")
tree1.pack(fill=BOTH,  expand=1)
for i in x1:
    tree1.heading(i, text=i)
    tree1.column(i, width=1)
MassM_eta2_1.insert(0, 'M(eta2)')
table1 = [MassM_eta2_1]
for i in table1:
    tree1.insert("", END, values=i)
x2.insert(0, 'a2')
tree2 = ttk.Treeview(columns=x2, show="headings")
tree2.pack(fill=BOTH,  expand=1)
for i in x2:
    tree2.heading(i, text=i)
    tree2.column(i, width=1)
MassM_eta2_2.insert(0, 'M(eta2)')
table2 = [MassM_eta2_2]
for i in table2:
    tree2.insert("", END, values=i)
w.mainloop()