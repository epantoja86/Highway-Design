"""python"""
W = 8.9 * 1000 #N
rho = 1.0567 #kg/m^3
Cd = 0.4
Af = 1.86 #m^3
F = 1134 #N
V = 31.28 #m/s

def rolling_resistance():
    return (0.01 * ( 1 + V / 44.73) * W)

def aero_resistance():
    return rho/2 * Cd * Af * V * V

def max_grade():
    return (F - aero_resistance() - rolling_resistance())/W

print(f"\nThe max grade achievable whilst maintaining speed ({round(V*3.6,2)}km/h) is : {round(max_grade()*100,2)}%")