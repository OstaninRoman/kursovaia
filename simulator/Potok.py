import math
import numpy

def potokSimulator(tm, t, L1, L2, A1, A2, p11, p12, p21, p22):
    Tm = tm; T = t
    P11 = p11; P12 = p12; P21 = p21; P22 = p22
    L = 0; l1 = L1; l2 = L2; a1 = A1
    Lj = [l1, a1]
    a2 = A2
    t = 0; td1 = 0; td2 = 0
    MassInitial = []
    TempListIntervS1 = [] # интервалы в 1-м состоянии
    MassIntervS = []  # интервалы в состояниях
    Interv_s1 = 0
    Interv_s2 = 0
    x = numpy.random.rand(1)[0]
    if (x >= 0.5):
        L = l1
    else:
        L = l2
    i = 0
    while (Tm > t):
        if (L == l1):
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
            TempListIntervS1.append([ty, SV])
            if (Tm < t):
                TempListIntervS1[len(TempListIntervS1) - 1][0] = Tm - (t - ty)
                Interv_s1 = 0
                for i in range(len(TempListIntervS1)):
                    Interv_s1 = Interv_s1 + TempListIntervS1[i][0]
                TempList = [Interv_s1, 1, TempListIntervS1]
                MassIntervS.append(TempList)
                TempListIntervS1 = []
                break
            if (t > td1):
                td1 = t
                td1 = td1 + T
                TempList = [t, 'O', 1, SV]
                MassInitial.append(TempList)
            else:
                td1 = t
                td1 = td1 + T
                TempList = [t, 'M', 1, SV]
                MassInitial.append(TempList)
            x = numpy.random.rand(1)[0]
            if (SV == 2):
                if (x > P21):
                    L = l2
                    td2 = td1
                    Interv_s1 = 0
                    for i in range(len(TempListIntervS1)):
                        Interv_s1 = Interv_s1 + TempListIntervS1[i][0]
                    TempList = [Interv_s1, 1, TempListIntervS1]
                    MassIntervS.append(TempList)
                    TempListIntervS1 = []
                else:
                    L = l1
            else:
                if (x > P11):
                    L = l2
                    td2 = td1
                    Interv_s1 = 0
                    for i in range(len(TempListIntervS1)):
                        Interv_s1 = Interv_s1 + TempListIntervS1[i][0]
                    TempList = [Interv_s1, 1, TempListIntervS1]
                    MassIntervS.append(TempList)
                    TempListIntervS1 = []
                else:
                    L = l1
        else:
            if (L == l2):
                x = numpy.random.rand(1)[0]
                T2 = t
                ty = -(1 / a2) * (math.log(1 - x))
                t = t + ty
                if (Tm < t):
                    Interv_s2 = Tm - (t - ty)
                    t = Tm
                    TempList = [Interv_s2, 2]
                    MassIntervS.append(TempList)
                else:
                    Interv_s2 = ty
                    TempList = [Interv_s2, 2]
                    MassIntervS.append(TempList)
                while (L == l2):
                    x = numpy.random.rand(1)
                    tys = -(1 / l2) * (math.log(1 - x))
                    T2 = T2 + tys
                    if (t > T2):
                        if (T2 > td2):
                            td2 = T2
                            td2 = td2 + T
                            TempList = [T2, 'O', 2]
                            MassInitial.append(TempList)
                        else:
                            td2 = T2
                            td2 = td2 + T
                            TempList = [T2, 'M', 2]
                            MassInitial.append(TempList)
                    else:
                        L = l1
                        td1 = td2
    A = [MassIntervS, MassInitial]
    return A

