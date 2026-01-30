import roadster
import matplotlib.pyplot as plt

annadist, annakmh = roadster.load_route('speed_anna.npz')
elsadist, elskmh = roadster.load_route('speed_elsa.npz')

v_anna = roadster.velocity(annadist, 'speed_anna.npz')
v_elsa = roadster.velocity(elsadist, 'speed_elsa.npz')
print(v_anna)
plt.scatter(annadist, annakmh, label='Anna')
plt.scatter(elsadist, elskmh, label='Elsa') 
plt.plot(annadist, v_anna, label='Anna Interpolated')
plt.plot(elsadist, v_elsa, label='Elsa Interpolated')
plt.xlabel('Avstånd (km)', fontsize=18)
plt.ylabel('Hastighet (km/h)', fontsize=18)   
plt.legend()
plt.show()