import math
import random
from tkinter import *
import numpy

def CreateP (ti, flag1, flag2, t, td, h, T, RadOval, HighRect, Hi, ColorO, ColorR):
    if(flag1 == 2):
        if(flag2 == 1):
            c.create_line(t+10, h-450, t+10, h-10)
            c.create_text(t + 20, h - 20, text='t%s' % ti)
        else:
            c.create_line(t + 10, h - 450, t + 10, h - 350, dash=(5, 1))
    else:
        if (flag2 == 1):
            c.create_line(t + 10, h - 500, t + 10, h - 10)
            c.create_text(t + 20, h - 20, text='t%s' % ti)
        else:
            c.create_line(t + 10, h - 500, t + 10, h - 350, dash=(5, 1))
    if(ColorO == 'black'):
        c.create_oval(t-RadOval+10, h-(350+RadOval), t+RadOval+10, h-(350-RadOval), fill=ColorO)
    else:
        c.create_oval(t-RadOval+10, h-(10+RadOval), t+RadOval+10, h-(10-RadOval), fill=ColorO)
    c.create_rectangle((td-T)+10, h-(340-HighRect*Hi), td+10, h-(340-(HighRect*Hi-HighRect)), fill=ColorR)
    c.create_rectangle((td-T)+10, h-150, td+10-1, h-(150-HighRect), fill='black', outline='black')




Tm = 50
T = 0.3
P11 = 0.7 #on first r.v. from s1 to s1
P12 = 0.3
P21 = 0.6 #on second r.v. from s1 to s1
P22 = 0.4
L = 0
l1 = 1.5
l2 = 0.6
a1 = 0.8
Lj = [l1, a1]
a2 = 0.7
t = 0
td1 = 0
td2 = 0
MassMiss = []
MassObserved = []
MassInitial = []
Hi1 = 1
Hi2 = 2
h = 600
w = 1200
kt = 30


Window = Tk()
Window.title('Графика')
c = Canvas(Window, height=h, width=w)
c.pack()
c.create_line(5, h-10, w, h-10, arrow=LAST)
c.create_line(5, h-10, 5, 10, arrow=LAST)
c.create_line(5, h-350, w, h-350, arrow=LAST)
c.create_line(5, h-150, w, h-150, arrow=LAST)
c.create_text(20, 20, text='L(t)')
c.create_text(w-10, h-360, text='t')
c.create_text(w-10, h-160, text='t')
c.create_text(w-10, h-20, text='t')
x = numpy.random.rand(1)[0]
if(x >= 0.5): L = l1
else: L = l2
i = 0
while (Tm > t):
    if(L == l1):
        x1 = numpy.random.rand(1)[0]
        x2 = numpy.random.rand(1)[0]
        ty1 = -(1 / Lj[0]) * math.log(1 - x1)
        ty2 = -(1 / Lj[1]) * math.log(1 - x2)
        if ty1 > ty2:
            ty = ty2
            SV = 2
        else:
            ty = ty1
            SV = 1
        t = t + ty
        if(Tm < t):
            if (SV == 1):
                c.create_line((Tm - (ty-(t-Tm))) * kt + 10, h - 500, Tm * kt + 10, h - 500, fill='blue', width=5)
            else:
                c.create_line((Tm - (ty-(t-Tm))) * kt + 10, h - 500, Tm * kt + 10, h - 500, fill='green', width=5)
            break
        else:
            if(SV == 1):
                c.create_line((t-ty)*kt+10, h-500, t*kt+10, h-500, fill='blue', width=5)
            else:
                c.create_line((t - ty) * kt + 10, h - 500, t * kt + 10, h - 500, fill='green', width=5)
        if(t > td1):
            Hi1 = 1
            td1 = t
            td1 = td1 + T
            TempList = [round(t, 4), 1]
            MassObserved.append(TempList)
            MassInitial.append(TempList)
            CreateP(len(MassObserved), 1, 1, t*kt, td1*kt, h, T*kt, 3, 5, Hi1, 'white', 'grey')
            #c.create_text(t*kt, h-20, text='ti')
        else:
            Hi1 = Hi1 + 1
            td1 = t
            td1 = td1 + T
            TempList = [round(t, 4), 1]
            MassMiss.append(round(t, 4))
            MassInitial.append(TempList)
            CreateP(0, 1, 0, t*kt, td1*kt, h, T*kt, 3, 5, Hi1, 'black', 'grey')
        x = numpy.random.rand(1)[0]
        if(SV == 2):
            if(x > P21):
                L = l2
                td2 = td1
                Hi2 = Hi1
                c.create_line(t*kt+10, h-500, t*kt+10, h-450, arrow=LAST)
            else:
                L = l1
        else:
            if(x > P11):
                L = l2
                td2 = td1
                Hi2 = Hi1
                c.create_line(t * kt + 10, h - 500, t * kt + 10, h - 450, arrow=LAST)
            else:
                L = l1
    else:
        if(L == l2):
            x = numpy.random.rand(1)[0]
            T2 = t
            ty = -(1/a2)*(math.log(1-x))
            t = t + ty
            if (Tm < t):
                c.create_line((t - ty) * kt + 10, h - 450, Tm * kt + 10, h - 450)
                t = Tm
            else:
                c.create_line((t - ty) * kt + 10, h - 450, t * kt + 10, h - 450)
                c.create_line(t * kt + 10, h - 500, t * kt + 10, h - 450, arrow=FIRST)
            while(L == l2):
                x = numpy.random.rand(1)[0]
                tys = -(1/l2)*(math.log(1-x))
                T2 = T2 + tys
                if(t > T2):
                    if(T2 > td2):
                        Hi2 = 1
                        td2 = T2
                        td2 = td2 + T
                        TempList = [round(T2, 4), 2]
                        MassObserved.append(TempList)
                        MassInitial.append(TempList)
                        CreateP(len(MassObserved),2, 1, T2*kt, td2*kt, h, T*kt, 3, 5, Hi2, 'white', 'grey')
                    else:
                        Hi2 = Hi2 + 1
                        td2 = T2
                        td2 = td2 + T
                        TempList = [round(T2, 4), 2]
                        MassMiss.append(round(T2, 4))
                        MassInitial.append(TempList)
                        CreateP(0, 2, 0, T2*kt, td2*kt, h, T*kt, 3, 5, Hi2, 'black', 'grey')
                else:
                    L = l1
                    td1 = td2
                    Hi1 = Hi2
print('Observed:', MassObserved)
print('Miss:', MassMiss)

def LabelW(t, a):
    l = LabelFrame(W2, text=t)
    e = Entry(l)
    e.insert(0, a)
    l.pack()
    e.pack()

W2 = Tk()
W2.title('Параметры')
W2.geometry("400x350")
LabelW('Параметр l1:', l1)
LabelW('Параметр a1:', a1)
LabelW('Параметр l2:', l2)
LabelW('Параметр a2:', a2)
LabelW('Параметр T:', T)
LabelW('Вероятность P.1.1:', P11)
LabelW('Вероятность P.1.2:', P12)
LabelW('Вероятность P.2.1:', P21)
LabelW('Вероятность P.2.2:', P22)

Window.mainloop()
W2.mainloop()



