import roadster
import numpy as np
import matplotlib.pyplot as plt

def konvergensstudie(route, n):
    '''x = roadster.load_route(route)[0][-1]

    steg = np.zeros(8, dtype=np.float32)
    E = np.zeros(8, dtype=np.float32)

    for i in range(8):
        steg[i] = n*2**i
        E[i] = roadster.total_consumption(x, route, n*2**i)
    E -= E[-1]
    print(steg)
    print(E)
    return steg, E

an, aE, = konvergensstudie("speed_anna.npz", 16)
en, eE, = konvergensstudie("speed_elsa.npz", 16)

plt.loglog(an,aE, label = "anna")
plt.loglog(en,eE, label = "elsa")
plt.plot(np.logspace(1, 3, 100), 7e4*np.logspace(1, 3, 100)**-2, label="lutning -2")
plt.legend()
plt.xlabel("n")
plt.ylabel("E")
plt.show()'''
    totalfel = np.array([])
    nvalue = np.array([])
    distance, speed = roadster.load_route(route)
    äkta = roadster.time_to_destination(distance[-1], route, 100000)
    for i in range(12): #sätt inte för högt
        fel = abs(äkta - roadster.time_to_destination(distance[-1], route, n*2**i))
        totalfel = np.append(totalfel, fel)
        nvalue = np.append(nvalue, n*2**i)
    return nvalue, totalfel

n=10

anna_nvalue, anna_totalfel = konvergensstudie('speed_anna.npz', n)
elsa_nvalue, elsa_totalfel = konvergensstudie('speed_elsa.npz', n)

plt.loglog(anna_nvalue, anna_totalfel, label = "anna")
plt.loglog(elsa_nvalue, elsa_totalfel, label = "elsa")
plt.plot(np.logspace(1, 3, 100, base=n), 1e2*np.logspace(1, 3, 100, base=n)**-2, label="lutning -2")
plt.plot(np.logspace(1, 3, 100, base=n), 1e1*np.logspace(1, 3, 100, base=n)**-1, label="lutning -1")
plt.legend()
plt.show()


