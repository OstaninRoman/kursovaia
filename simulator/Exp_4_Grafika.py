import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk

f = open('Exp4.txt', 'r')
MassM_eta1 = []
MassM_eta2 = []
x = []
nam = f.readline()
MassM_eta1_1 = list(map(float, nam.split()))
nam = f.readline()
MassM_eta1_2 = list(map(float, nam.split()))

for i in range(5, 55, 5):
    i = i/10
    x.append(i)

fig, (ax1, ax2) = plt.subplots(2)
ax1.scatter(x, MassM_eta1_1)
ax1.set_xlabel("l1")
ax1.set_ylabel("M(eta1)", rotation=0, labelpad=20)

ax2.scatter(x, MassM_eta1_2)
ax2.set_xlabel("l1")
ax2.set_ylabel("M(eta1)", rotation=0, labelpad=20)

plt.show()

w = Tk()
w.geometry("800x600")
x.insert(0, 'l1')
tree1 = ttk.Treeview(columns=x, show="headings")
tree1.pack(fill=BOTH,  expand=1)
for i in x:
    tree1.heading(i, text=i)
    tree1.column(i, width=1)
MassM_eta1_1.insert(0, 'M(eta1)')
table1 = [MassM_eta1_1]
for i in table1:
    tree1.insert("", END, values=i)
tree2 = ttk.Treeview(columns=x, show="headings")
tree2.pack(fill=BOTH,  expand=1)
for i in x:
    tree2.heading(i, text=i)
    tree2.column(i, width=1)
MassM_eta1_2.insert(0, 'M(eta1)')
table2 = [MassM_eta1_2]
for i in table2:
    tree2.insert("", END, values=i)
w.mainloop()