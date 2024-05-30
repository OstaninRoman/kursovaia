from Potok import potokSimulator
from tkinter import *

def potokArt(h, w, kt, a):
    A = potokSimulator(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9])
    MassIntervS = A[0]
    MassInitial = A[1]
    H = h
    W = w
    Kt = kt
    Window = Tk()
    Window.title('Графика')
    left = 30
    right = 10
    down = 20
    up = 10
    line_1 = h*(1/5)
    line_2 = h*(2/5)
    line_3 = h*(3/5)
    line_4 = h*(4/5)
    line_5 = h-20
    c = Canvas(Window, height=H, width=W)
    c.pack(side=BOTTOM)
    c.create_line(left, h-down, left, up, arrow=LAST)
    c.create_line(left, line_1, w, line_1, arrow=LAST)
    c.create_line(left, line_2, w, line_2, arrow=LAST)
    c.create_line(left, line_3, w, line_3, arrow=LAST)
    c.create_line(left, line_4, w, line_4, arrow=LAST)
    c.create_line(left, line_5, w, line_5, arrow=LAST)
    c.create_text(left-15, 20, text='L(t)')
    c.create_text(w-right, line_1+10, text='t')
    c.create_text(w-right, line_2+10, text='t')
    c.create_text(w-right, line_3+10, text='t')
    c.create_text(w-right, line_4+10, text='t')
    c.create_text(w-right, line_5+10, text='t')
    c.create_text(w*(1/2), line_1-10, text='процесс L(t)')
    c.create_text(w*(1/2), line_2-10, text='исходный поток событий')
    c.create_text(w*(1/2), line_3-10, text='формирование периодов ненаблюдения')
    c.create_text(w*(1/2), line_4-10, text='общий период ненаблюдения')
    c.create_text(w*(1/2), line_5-10, text='наблюдаемый поток')
    cx = left
    line_s1 = line_1*(1/4)
    line_s2 = line_1*(3/4)
    for i in range(len(MassIntervS) - 1):
        if MassIntervS[i][1] == 1:
            for j in range(len(MassIntervS[i][2])):
                if MassIntervS[i][2][j][1] == 1:
                    c.create_line(cx, line_s1, cx+MassIntervS[i][2][j][0]*kt, line_s1, fill='blue', width=5)
                else:
                    c.create_line(cx, line_s1, cx+MassIntervS[i][2][j][0]*kt, line_s1, fill='green', width=5)
                cx = cx + MassIntervS[i][2][j][0] * kt
            c.create_line(cx, line_s1, cx, line_s2, arrow=LAST)
        else:
            c.create_line(cx, line_s2, cx+MassIntervS[i][0]*kt, line_s2)
            c.create_line(cx + MassIntervS[i][0]*kt, line_s2, cx + MassIntervS[i][0]*kt, line_s1, arrow=LAST)
            cx = cx + MassIntervS[i][0]*kt
    if MassIntervS[len(MassIntervS)-1][1] == 1:
        for j in range(len(MassIntervS[len(MassIntervS)-1][2])):
            if MassIntervS[len(MassIntervS)-1][2][j][1] == 1:
                c.create_line(cx, line_s1, cx+MassIntervS[len(MassIntervS)-1][2][j][0]*kt, line_s1, fill='blue', width=5)
            else:
                c.create_line(cx, line_s1, cx+MassIntervS[len(MassIntervS)-1][2][j][0]*kt, line_s1, fill='green', width=5)
            cx = cx + MassIntervS[len(MassIntervS)-1][2][j][0] * kt
    else:
        c.create_line(cx, line_s2, cx + MassIntervS[len(MassIntervS) - 1][0]*kt, line_s2)
    Hi = 1
    RadOval = 3
    HiRec = h*(1/120)
    cx = 0
    count_event = 0
    for i in range(len(MassInitial)):
        cx = MassInitial[i][0]
        if MassInitial[i][1] == 'M':
            Hi = Hi + 1
            if MassInitial[i][2] == 1:
                c.create_line(cx*kt+left, line_s1, cx*kt+left, line_2, dash=(5, 1))
                c.create_oval((cx*kt+left-RadOval), line_2-RadOval, (cx*kt+left+RadOval), line_2+RadOval, fill='black')
                c.create_rectangle(cx*kt+left, (line_3+10)+HiRec*Hi, ((cx+a[1])*kt+left), (line_3+10)+HiRec+HiRec*Hi, fill='gray')
                c.create_rectangle(cx*kt+left, (line_4+10)+HiRec, ((cx+a[1])*kt+left), (line_4+10)+HiRec*2, fill='black')
            else:
                c.create_line(cx*kt+left, line_s2, cx*kt+left, line_2, dash=(5, 1))
                c.create_oval((cx*kt+left-RadOval), line_2-RadOval, (cx*kt+left+RadOval), line_2+RadOval, fill='black')
                c.create_rectangle(cx*kt+left, (line_3+10)+HiRec*Hi, ((cx+a[1])*kt+left), (line_3+10)+HiRec+HiRec*Hi, fill='gray')
                c.create_rectangle(cx*kt+left, (line_4+10)+HiRec, ((cx+a[1])*kt+left), (line_4+10)+HiRec*2, fill='black')
        else:
            Hi = 1
            count_event = count_event + 1
            if MassInitial[i][2] == 1:
                c.create_line(cx*kt+left, line_s1, cx*kt+left, line_5)
                c.create_oval((cx*kt+left-RadOval), line_2-RadOval, (cx*kt+left+RadOval), line_2+RadOval, fill='white')
                c.create_oval((cx*kt+left-RadOval), line_5-RadOval, (cx*kt+left+RadOval), line_5+RadOval, fill='white')
                c.create_rectangle(cx*kt+left, (line_3+10)+HiRec, ((cx+a[1])*kt+left), (line_3+10)+HiRec*2, fill='gray')
                c.create_rectangle(cx*kt+left, (line_4+10)+HiRec, ((cx+a[1])*kt+left), (line_4+10)+HiRec*2, fill='black')
                c.create_text(cx*kt+left, h-10, text='t%s' % count_event)
            else:
                c.create_line(cx*kt+left, line_s2, cx*kt+left, line_5)
                c.create_oval((cx*kt+left-RadOval), line_2-RadOval, (cx*kt+left+RadOval), line_2+RadOval, fill='white')
                c.create_oval((cx*kt+left-RadOval), line_5-RadOval, (cx*kt+left+RadOval), line_5+RadOval, fill='white')
                c.create_rectangle(cx*kt+left, (line_3+10)+HiRec, ((cx+a[1])*kt+left), (line_3+10)+HiRec*2, fill='gray')
                c.create_rectangle(cx*kt+left, (line_4+10)+HiRec, ((cx+a[1])*kt+left), (line_4+10)+HiRec*2, fill='black')
                c.create_text(cx*kt+left, h-10, text='t%s' % count_event)
    def LabelW(t, a):
        l = LabelFrame(Window, text=t)
        e = Entry(l)
        e.insert(0, a)
        l.pack(side=LEFT)
        e.pack()

    LabelW('Парам. Tm:', a[0])
    LabelW('Парам. T:', a[1])
    LabelW('Парам. l1:', a[2])
    LabelW('Парам. l2:', a[3])
    LabelW('Парам. a1:', a[4])
    LabelW('Парам. a2:', a[5])
    LabelW('Вер-ть P.1.1:', a[6])
    LabelW('Вер-ть P.1.2:', a[7])
    LabelW('Вер-ть P.2.1:', a[8])
    LabelW('Вер-ть P.2.2:', a[9])
    Window.mainloop()
    return 0

potokArt(550, 1150, 30, [35, 0.5, 1.5, 0.8, 0.8, 0.7, 0.4, 0.6, 0.7, 0.3])

