import numpy as np
import roadster
'''a = np.zeros(4, dtype=np.int_)
print(a)
b = roadster.total_consumption(23.7, "speed_elsa.npz",1000000)
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
'''distance, speed = roadster.load_route('speed_anna.npz')
print(roadster.time_to_destination(distance[-1], 'speed_anna.npz', 10000))
print(roadster.total_consumption(distance[-1], 'speed_anna.npz', 10000))
c = 0
n = 400
while c < 11925 or c > 11926:
    n += 1
    c = roadster.total_consumption(distance[-1], 'speed_anna.npz', n)
    print(f'Loop nr {n}')
print(f'C is {c} and n = {n}')'''
for i in np.logspace(0, 5):
        print(i)