from Potok import potokSimulator

f = open('Exp2.txt', 'w')
a = 100; b = 4100; h = 100
MassM_tau = []
MassM_ksi = []
MassM_eta1 = []
MassM_eta2 = []
for q in range(a, b, h):
    MassTau = []
    MassKsi = []
    MassEta1 = []
    MassEta2 = []
    Tm = q
    for r in range(100):
        T = 0.1
        A = potokSimulator(q, T, 1.5, 0.9, 1.1, 0.2, 0.3, 0.7, 0.4, 0.6)
        MassIntervS = A[0]
        MassInitial = A[1]
        MassObserved = []
        for i in range(len(MassInitial)):
            if MassInitial[i][1] == 'O':
                MassObserved.append(MassInitial[i])
        tau = 0
        M_tau = 0
        xi = 0
        xj = 0
        if len(MassObserved) > 1:
            for i in range(1, len(MassObserved)):
                xi = MassObserved[i-1]
                xj = MassObserved[i]
                #print('tau', (xj[0]-xi[0]))
                tau = tau + (xj[0]-xi[0])
            tau = tau/(len(MassObserved)-1)
        else:
            tau = 0
            print(' Имитационная модель содержит только одно событие')
        MassTau.append(tau)
        MassIntervNotObs = []  # периоды ненаблюдения
        ksi = 0
        M_ksi = 0
        x = 0
        x = MassInitial[0][0]
        for i in range(1, len(MassInitial)):
            if MassInitial[i][0] - MassInitial[i - 1][0] > T:
                if x == MassInitial[i - 1][0]:
                    MassIntervNotObs.append(T)
                    x = MassInitial[i][0]
                else:
                    MassIntervNotObs.append(((MassInitial[i - 1][0] - x)+T))
                    x = MassInitial[i][0]
        if len(MassIntervNotObs) != 0:
            for i in range(len(MassIntervNotObs)):
                ksi = ksi + MassIntervNotObs[i]
            ksi = ksi/(len(MassIntervNotObs))
        else:
            ksi = 0
            print(' Имитационная модель не имеет периодов ненаблюдения')
        MassKsi.append(ksi)
        eta1 = 0
        eta2 = 0
        M_eta1 = 0
        M_eta2 = 0
        count_eta1 = 0
        count_eta2 = 0
        for i in range(len(MassIntervS)):
            if MassIntervS[i][1] == 1:
                eta1 = eta1 + MassIntervS[i][0]
                count_eta1 = count_eta1 + 1
            else:
                eta2 = eta2 + MassIntervS[i][0]
                count_eta2 = count_eta2 + 1
        if count_eta1 != 0:
            eta1 = eta1/(count_eta1)
        else:
            eta1 = 0
            print(' Иммитационная модель не содержит 1-го состояния')
        if count_eta2 != 0:
            eta2 = eta2/(count_eta2)
        else:
            eta2 = 0
            print(' Иммитационная модель не содержит 2-го состояния')
        MassEta1.append(eta1)
        MassEta2.append(eta2)
    print(Tm)
    print(MassTau)
    print(MassKsi)
    print(MassEta1)
    print(MassEta2)
    if len(MassTau) != 0:
        for i in range(len(MassTau)):
            M_tau = M_tau + MassTau[i]
        M_tau = (M_tau/(len(MassTau)))
    else:
        M_tau = 0
    MassM_tau.append(round(M_tau, 4))
    if len(MassKsi) != 0:
        for i in range(len(MassKsi)):
            M_ksi = M_ksi + MassKsi[i]
        M_ksi = (M_ksi/(len(MassKsi)))
    else:
        M_ksi = 0
    MassM_ksi.append(round(M_ksi, 6))
    if len(MassEta1) != 0:
        for i in range(len(MassEta1)):
            M_eta1 = (M_eta1 + MassEta1[i])
        M_eta1 = (M_eta1/(len(MassEta1)))
    else:
        M_eta1 = 0
    MassM_eta1.append(round(M_eta1, 4))
    if len(MassEta2) != 0:
        for i in range(len(MassEta2)):
            M_eta2 = (M_eta2 + MassEta2[i])
        M_eta2 = (M_eta2/(len(MassEta2)))
    else:
        M_eta2 = 0
    MassM_eta2.append(round(M_eta2, 4))
for i in range(len(MassM_tau)):
    f.write('%s\t' % MassM_tau[i])
f.write('\n')
for i in range(len(MassM_ksi)):
    f.write('%s ' % MassM_ksi[i])
f.write('\n')
for i in range(len(MassM_eta1)):
    f.write('%s\t' % MassM_eta1[i])
f.write('\n')
for i in range(len(MassM_eta2)):
    f.write('%s\t' % MassM_eta2[i])
f.write('\n')
f.close()


