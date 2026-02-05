import numpy as np
from scipy import interpolate

def load_route(route):
    """ 
    Get speed data from route .npz-file. Example usage:

      distance_km, speed_kmph = load_route('speed_anna.npz')
    
    The route file should contain two arrays, distance_km and 
    speed_kmph, of equal length with position (in km) and speed 
    (in km/h) along route. Those two arrays are returned by this 
    convenience function.
    """
    # Read data from npz file
    if not route.endswith('.npz'):
        route = f'{route}.npz' 
    data = np.load(route)
    distance_km = data['distance_km']
    speed_kmph = data['speed_kmph']    
    return distance_km, speed_kmph

def save_route(route, distance_km, speed_kmph):
    """ 
    Write speed data to route file. Example usage:

      save_route('speed_olof.npz', distance_km, speed_kmph)
    
    Parameters have same meaning as for load_route
    """ 
    np.savez(route, distance_km=distance_km, speed_kmph=speed_kmph)

### PART 1A ###
def consumption(v):
    a1,a2,a3,a4 = 546.8, 50.31, 0.2584, 0.008210

    return a1/v + a2 +a3*v +a4*v**2
    

### PART 1B ###
def velocity(x, route):
    # ALREADY IMPLEMENTED!
    """
    Interpolates data in given route file, and evaluates the function
    in x
    """
    # Load data
    distance_km, speed_kmph = load_route(route)
    # Check input ok?
    assert np.all(x>=0), 'x must be non-negative'
    assert np.all(x<=distance_km[-1]), 'x must be smaller than route length'
    # Interpolate
    v = interpolate.pchip_interpolate(distance_km, speed_kmph,x)
    return v

### PART 2A ###
def time_to_destination(x, route, n):
    # x avstånd längs rutt
    # route rutt
    # n antal delintervall
    h = x/n
    pos = np.linspace(0,x,n+1)
    tid = 1 / velocity(pos,route)
    tid[0], tid[-1] = tid[0]/2, tid[-1]/2 

    return np.sum(tid)*h

### PART 2B ###
def total_consumption(x, route, n):
    h=x/n
    pos = np.linspace(0,x,n+1)
    hastighet = velocity(pos, route)
    consump = consumption(hastighet)
    consump[0], consump[-1] = consump[0]/2, consump[-1]/2
    return np.sum(consump)*h

    

### PART 3A ###
def distance(T, route): #fungerar inte över 0.5, helt ärligt tycker inte att den bör fungera alls, för
    #tycker att det ska vara ttd*vel, men då fungerar det inte, är så jälva förvirrad.
    tolerans = 10
    n = 100000
    distance_km, speed_kmp = load_route(route)
    assert np.all(T<=time_to_destination(distance_km[-1], route, n)), 'T must be smaller than total time to destination'
    x= T/time_to_destination(distance_km[-1], route, n)*distance_km[-1] #gissning är snittet
    while tolerans > 10**-4: #kör bara tills liten tollerans.
        vel = velocity(x, route)
        ttd = time_to_destination(x, route, n)
        x -= ttd/vel
        tolerans = abs(ttd - T)
        print(x)
        #print(tolerans)
    return x

    
    
        
    return



### PART 3B ###
def reach(C, route):
    # REMOVE THE FOLLOWING LINE AND WRITE YOUR SOLUTION
    raise NotImplementedError('reach not implemented yet!')
