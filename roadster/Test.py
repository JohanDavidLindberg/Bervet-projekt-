import numpy as np
import roadster
'''a = np.zeros(4, dtype=np.int_)
print(a)
a[1] = 2
print(a)
b= [0,0,0,0,0,0,0]
print(b)
c = np.array([0,0,0,0,0,0,0])
print(c)

print(c[-1])
c -= 2
print(c)'''
'''time = 0
n = 430
print('Kör')

while time < 0.95 or time > 0.9666667:
    n += 1
    distance, speed = roadster.load_route('speed_elsa.npz')
    time = roadster.time_to_destination(distance[-1], 'speed_elsa.npz', n)
    minuter = time*60
    print(f'Loop {n}')
print(f'n = {n} and time = {time}, vilket är {minuter} minuter')'''

print(roadster.total_consumption(65, 'speed_anna.npz', 10000))
