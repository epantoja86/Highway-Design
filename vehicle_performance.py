"""Ff + Fr = ma + Ra + Rrlf + Rrlr + Rg

```python"""
def calculate_equation(Ff, Fr, m, a, Ra, Rrlf, Rrlr, Rg):
    """
    Calculate the equation: Ff + Fr = ma + Ra + Rrlf + Rrlr + Rg
    
    Parameters:
    Ff (float): Force front
    Fr (float): Force rear
    m (float): Mass
    a (float): Acceleration
    Ra (float): Aerodynamic resistance
    Rrlf (float): Rolling resistance front
    Rrlr (float): Rolling resistance rear
    Rg (float): Gravitational resistance
    
    Returns:
    tuple: (left_side, right_side, is_balanced)
    """
    left_side = Ff + Fr
    right_side = m * a + Ra + Rrlf + Rrlr + Rg
    
    return left_side, right_side, abs(left_side - right_side) < 1e-10

def main():
    print("Equation Calculator: Ff + Fr = ma + Ra + Rrlf + Rrlr + Rg")
    print("-------------------------------------------------------")
    
    # Get user inputs for all variables
    try:
        Ff = float(input("Enter value for Ff (Force front): "))
        Fr = float(input("Enter value for Fr (Force rear): "))
        m = float(input("Enter value for m (Mass): "))
        a = float(input("Enter value for a (Acceleration): "))
        Ra = float(input("Enter value for Ra (Aerodynamic resistance): "))
        Rrlf = float(input("Enter value for Rrlf (Rolling resistance front): "))
        Rrlr = float(input("Enter value for Rrlr (Rolling resistance rear): "))
        Rg = float(input("Enter value for Rg (Gravitational resistance): "))
        
        # Calculate and display results
        left_side, right_side, is_balanced = calculate_equation(Ff, Fr, m, a, Ra, Rrlf, Rrlr, Rg)
        
        print("\nResults:")
        print(f"Left side (Ff + Fr) = {left_side}")
        print(f"Right side (ma + Ra + Rrlf + Rrlr + Rg) = {right_side}")
        print(f"Difference = {left_side - right_side}")
        
        if is_balanced:
            print("The equation is balanced.")
        else:
            print("The equation is not balanced.")
        
    except ValueError:
        print("Error: Please enter valid numerical values for all variables.")

if __name__ == "__main__":
    main()
"""

This script:
1. Defines a function to calculate both sides of the equation
2. Takes user input for all variables (Ff, Fr, m, a, Ra, Rrlf, Rrlr, Rg)
3. Calculates the left side (Ff + Fr) and right side (ma + Ra + Rrlf + Rrlr + Rg)
4. Displays the results and indicates whether the equation is balanced

To use the script, simply run it and enter the values for each variable when prompted. The script will then calculate both sides of the equation and show you the results.​​​​​​​​​​​​​​​​
"""
