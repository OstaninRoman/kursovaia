from tkinter import *
import random

def ran1(idum):
    iff = 0
    r = []
    rm1 = 3.8580247e-6
    rm2 = 7.4373773e-6
    m1 = 259200
    ia1 = 7141
    ic1 = 54773
    m2 = 134456
    ia2 = 8121
    ic2 = 28411
    m3 = 243000
    ia3 = 4561
    ic3 = 51349
    j = 0
    ret = 0
    if(idum<0 or iff==0):
        iff = 1
        if(idum<0): idum = -idum
        ix1 = (ic1 - idum) % m1
        ix1 = (ia1 * ix1 + ic1) % m1
        ix2 = ix1 % m2
        ix1 = (ia1 * ix1 + ic1) % m1
        ix3 = ix1 % m3
        for j in range(0, 98):
            ix1 = (ia1 * ix1 + ic1) % m1
            ix2 = (ia2 * ix2 + ic2) % m2
            r.append(((ix1 + ix2 * rm2) * rm1))
        idum = 1
    ix1 = (ia1 * ix1 + ic1) % m1
    ix2 = (ia2 * ix2 + ic2) % m2
    ix3 = (ia3 * ix3 + ic3) % m3
    j = int((97 * ix3) / m3)
    if(j<0):j = 0
    else:
        if(j>96): j=96
    ret = r[j]
    r[j] = (ix1 + ix2 * rm2) * rm1
    return ret

Wind = Tk()
c = Canvas(Wind, height=200, width=300)

c.pack()
c.create_arc(100, 140, 200, 180)
c.create_arc(0, 140, 100, 180)
c.create_text(100, 130, text='t')
c.mainloop()

Tm = 50
T = 1
P11 = 0.3
P12 = 0.7
P21 = 0.4
P22 = 0.6
L = 0
l1 = 2
l2 = 0.5
a1 = 0.7
Lj = [l1, a1]
ji = 0
a2 = 0.2
t = 0
td1 = 0
td2 = 0
MassInitial = []
MassMiss = []
MassObservedS1 = []
MassObservedS2 = []
Hi1 = 1
Hi2 = 2
h = 600
w = 1200
kt = 20
x = random.random()
if (x >= 0.5):
    L = l1
else:
    L = l2
i = 0
while (Tm > t):
    if (L == l1):
        x1 = random.random()
        x2 = random.random()
        xj = [x1, x2]
        if (xj[0] > xj[1]):
            j = 1
            ji = 2
        else:
            j = 0
            ji = 1
        T1 = t
        ty = -(1 / xj[j]) * math.log(1 - xj[j])
        t = t + ty
        if (Tm < t): break

        T1 = T1 + ty
        if (T1 > td1):
            Hi1 = 1
            td1 = T1
            td1 = td1 + T
            TempList = [round(t, 4), ji]
            MassObservedS1.append(TempList)

        else:
            Hi1 = Hi1 + 1
            td1 = T1
            td1 = td1 + T
            MassMiss.append(round(t, 4))
        x = random.random()
        if (j == 1):
            if (x > P21):
                L = l2
                td2 = td1
                Hi2 = Hi1
            else:
                L = l1
    else:
        if (L == l2):
            x = random.random()
            T2 = t
            ty = -(1 / a2) * (math.log(1 - x))
            t = t + ty
            while (L == l2):
                x = random.random()
                tys = -(1 / l2) * (math.log(1 - x))
                T2 = T2 + tys
                if (Tm < T2): break
                if (t > T2):
                    if (T2 > td2):
                        Hi2 = 1
                        td2 = T2
                        td2 = td2 + T
                        MassObservedS2.append(round(T2, 4))
                        MassInitial
                    else:
                        Hi2 = Hi2 + 1
                        td2 = T2
                        td2 = td2 + T
                        MassMiss.append(round(T2, 4))
                else:
                    L = l1
                    td1 = td2
                    Hi1 = Hi2

