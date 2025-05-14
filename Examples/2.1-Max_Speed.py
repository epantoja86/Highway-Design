'''python'''

import numpy as np

W = 11.1 * 1000 #N
rho = 1.2256 #kg/m^3
Cd = 0.38
Af = 1.86 #m^3
Pavail = 37.3 * 1000 #W

def aero_resistance():
    return rho/2 * Cd * Af

def rolling_resistance():
    return (0.01 * W / 44.73 , 0.01 * W)

def max_speed():
    """
    Returns max speed achievable with available power to overcome rolling and aero resistance
    
    Achieved by Solveing a cubic equation of the form ax³ + bx² + cx + d = 0
    
    Parameters:
    a, b, c, d: coefficients of the cubic equation
    a : Aero Resistance (N)
    b & c : Rolling Resistance (N)
    d : Available Power (W)
    
    Returns:
    Array of roots (solutions) to the equation
    """
    a = aero_resistance()
    b,c = rolling_resistance()
    d = -Pavail

    # Handle the case where a is 0 (making it a quadratic equation)
    if a == 0:
        # Handle quadratic equation: bx² + cx + d = 0
        if b == 0:
            # Handle linear equation: cx + d = 0
            if c == 0:
                return "Not an equation" if d == 0 else "No solution"
            return [-d / c]
        # Quadratic formula: (-c ± sqrt(c² - 4bd)) / (2b)
        discriminant = c**2 - 4*b*d
        if discriminant < 0:
            return "No real solutions"
        elif discriminant == 0:
            return [-c / (2*b)]
        else:
            return [(-c + np.sqrt(discriminant)) / (2*b), 
                    (-c - np.sqrt(discriminant)) / (2*b)]
    
    # For cubic equation, use numpy's polynomial roots solver
    Vm = np.roots([a, b, c, d]) * 3.6
    V = [root.real for root in Vm if np.isclose(root.imag, 0)]
    return round(abs(V[0]),2)
print(f"\nThe max speed achievable with available power ({Pavail/1000}kW) is : {max_speed()} km/h")