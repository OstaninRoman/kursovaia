from Potok import potokSimulator


f = open('Exp4.txt', 'w')
# вероятности перехода из 1-го состояния во 2-е увеличены
a = 5
b = 55
h = 5
MassM_eta1 = []
for q in range(a, b, h):
    MassEta1 = []
    l1 = q/10
    for r in range(100):
        A = potokSimulator(3000, 0.1, l1, 0.2, 1.1, 0.2, 0.3, 0.7, 0.3, 0.7)
        MassIntervS = A[0]
        eta1 = 0
        M_eta1 = 0
        count_eta1 = 0
        for i in range(len(MassIntervS)):
            if MassIntervS[i][1] == 1:
                eta1 = eta1 + MassIntervS[i][0]
                count_eta1 = count_eta1 + 1
        if count_eta1 != 0:
            eta1 = eta1/(count_eta1)
        else:
            eta1 = 0
            print(' Иммитационная модель не содержит 1-го состояния')
        MassEta1.append(eta1)
    print(l1)
    print(MassEta1)
    if len(MassEta1) != 0:
        for i in range(len(MassEta1)):
            M_eta1 = (M_eta1 + MassEta1[i])
        M_eta1 = (M_eta1/(len(MassEta1)))
    else:
        M_eta1 = 0
    MassM_eta1.append(round(M_eta1, 4))
for i in range(len(MassM_eta1)):
    f.write('%s\t' % MassM_eta1[i])
f.write('\n')


#вероятности остаться в 1-м состоянии увеличены
MassM_eta1 = []
for q in range(a, b, h):
    MassEta1 = []
    l1 = q/10
    for r in range(100):
        A = potokSimulator(3000, 0.1, l1, 0.2, 1.1, 0.2, 0.7, 0.3, 0.7, 0.3)
        MassIntervS = A[0]
        eta1 = 0
        M_eta1 = 0
        count_eta1 = 0
        for i in range(len(MassIntervS)):
            if MassIntervS[i][1] == 1:
                eta1 = eta1 + MassIntervS[i][0]
                count_eta1 = count_eta1 + 1
        if count_eta1 != 0:
            eta1 = eta1/(count_eta1)
        else:
            eta1 = 0
            print(' Иммитационная модель не содержит 1-го состояния')
        MassEta1.append(eta1)
    print(l1)
    print(MassEta1)
    if len(MassEta1) != 0:
        for i in range(len(MassEta1)):
            M_eta1 = (M_eta1 + MassEta1[i])
        M_eta1 = (M_eta1/(len(MassEta1)))
    else:
        M_eta1 = 0
    MassM_eta1.append(round(M_eta1, 4))
for i in range(len(MassM_eta1)):
    f.write('%s\t' % MassM_eta1[i])
f.write('\n')

f.close()


