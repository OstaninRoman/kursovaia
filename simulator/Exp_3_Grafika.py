import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk

def ax_(a, x, y):
    a.set_xlabel(x)
    a.set_ylabel(y)

f = open('Exp3.txt', 'r')
MassM_tau = []
MassM_ksi = []
MassM_eta1 = []
MassM_eta2 = []
x = []
nam = f.readline()
MassM_tau = list(map(float, nam.split()))
nam = f.readline()
MassM_ksi = list(map(float, nam.split()))
nam = f.readline()
MassM_eta1 = list(map(float, nam.split()))
nam = f.readline()
MassM_eta2 = list(map(float, nam.split()))
print(MassM_tau)
for i in range(1, 16, 1):
    i = i/10
    x.append(i)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.scatter(x, MassM_tau)
ax_(ax1, 'T', 'M(tau)')

ax2.scatter(x, MassM_ksi)
ax_(ax2, 'T', 'M(ksi)')

ax3.scatter(x, MassM_eta1)
y = MassM_eta1[len(MassM_eta1)-1]
ax3.set_ylim(y-0.05, y+0.05)
ax_(ax3, 'T', 'M(eta1)')

ax4.scatter(x, MassM_eta2)
y = MassM_eta2[len(MassM_eta2)-1]
ax4.set_ylim(y-0.5, y+0.5)
ax_(ax4, 'T', 'M(eta2)')
plt.show()

w = Tk()
w.geometry("1200x200")
x.insert(0, 'T')
tree = ttk.Treeview(columns=x, show="headings")
tree.pack(fill=BOTH,  expand=1)
for i in x:
    tree.heading(i, text=i)
    tree.column(i, width=1)
MassM_tau.insert(0, 'M(tau)')
MassM_ksi.insert(0, 'M(ksi)')
MassM_eta1.insert(0, 'M(eta1)')
MassM_eta2.insert(0, 'M(eta2)')
table = [MassM_tau, MassM_ksi, MassM_eta1, MassM_eta2]
for i in table:
    tree.insert("", END, values=i)
w.mainloop()