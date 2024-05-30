from Potok import potokSimulator

f = open('Exp5.txt', 'w')
a = 1
b = 11
h = 1
MassM_eta2 = []
for q in range(a, b, h):
    MassEta2 = []
    a2 = q/100
    for r in range(100):
        A = potokSimulator(3000, 0.1, 1.5, 0.2, 1.1, a2, 0.4, 0.6, 0.6, 0.4)
        MassIntervS = A[0]
        eta2 = 0
        M_eta2 = 0
        count_eta2 = 0
        for i in range(len(MassIntervS)):
            if MassIntervS[i][1] == 2:
                eta2 = eta2 + MassIntervS[i][0]
                count_eta2 = count_eta2 + 1
        if count_eta2 != 0:
            eta2 = eta2/(count_eta2)
        else:
            eta2 = 0
            print(' Иммитационная модель не содержит 2-го состояния')
        MassEta2.append(eta2)
    print(a2)
    print(MassEta2)
    if len(MassEta2) != 0:
        for i in range(len(MassEta2)):
            M_eta2 = (M_eta2 + MassEta2[i])
        M_eta2 = (M_eta2/(len(MassEta2)))
    else:
        M_eta2 = 0
    MassM_eta2.append(round(M_eta2, 4))
for i in range(len(MassM_eta2)):
    f.write('%s\t' % MassM_eta2[i])
f.write('\n')

a = 5
b = 55
h = 5
MassM_eta2 = []
for q in range(a, b, h):
    MassEta2 = []
    a2 = q/10
    for r in range(100):
        A = potokSimulator(3000, 0.1, 1.5, 0.2, 1.1, a2, 0.4, 0.6, 0.6, 0.4)
        MassIntervS = A[0]
        eta2 = 0
        M_eta2 = 0
        count_eta2 = 0
        for i in range(len(MassIntervS)):
            if MassIntervS[i][1] == 2:
                eta2 = eta2 + MassIntervS[i][0]
                count_eta2 = count_eta2 + 1
        if count_eta2 != 0:
            eta2 = eta2/(count_eta2)
        else:
            eta2 = 0
            print(' Иммитационная модель не содержит 2-го состояния')
        MassEta2.append(eta2)
    print(a2)
    print(MassEta2)
    if len(MassEta2) != 0:
        for i in range(len(MassEta2)):
            M_eta2 = (M_eta2 + MassEta2[i])
        M_eta2 = (M_eta2/(len(MassEta2)))
    else:
        M_eta2 = 0
    MassM_eta2.append(round(M_eta2, 4))
for i in range(len(MassM_eta2)):
    f.write('%s\t' % MassM_eta2[i])
f.write('\n')
f.close()


