import numpy as np
import roadster

a = roadster.time_to_destination(35, "speed_anna.npz",100)
print(a)
b = roadster.total_consumption(23.7, "speed_elsa.npz",1000000)
print(b)