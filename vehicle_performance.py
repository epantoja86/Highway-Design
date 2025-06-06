import numpy as np

def solve_cubic(a, b, c, d):
    """
    Solves a cubic equation of the form ax³ + bx² + cx + d = 0
    
    Parameters:
    a, b, c, d: coefficients of the cubic equation
    
    Returns:
    Array of roots (solutions) to the equation
    """
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
    return np.roots([a, b, c, d])

# Example: solve x³ - 6x² + 11x - 6 = 0
roots = solve_cubic(1, -6, 11, -6)
print("Roots:", roots)