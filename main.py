from fractions import Fraction

def simplify_equation(x1, y1, gradient):
    # Slope-intercept form: y = mx + c
    c = y1 - gradient * x1
    
    # Simplify slope and intercept (e.g., 0.5 → 1/2, -0 → 0)
    m_frac = Fraction(gradient).limit_denominator()
    c_frac = Fraction(c).limit_denominator()
    
    # Build slope-intercept equation (handle signs neatly)
    slope_intercept = []
    slope_intercept.append(f"y = {m_frac}x" if m_frac != 1 else "y = x")
    
    if c_frac != 0:
        if c_frac > 0:
            slope_intercept.append(f" + {c_frac}")
        else:
            slope_intercept.append(f" - {-c_frac}")
    slope_intercept_eq = "".join(slope_intercept)
    
    # Standard form: Ax + By = C (convert from y = mx + c → mx - y = -c)
    A = m_frac.numerator
    B = -m_frac.denominator
    C = -c_frac.numerator * m_frac.denominator
    
    # Simplify fractions (e.g., 2x - 4y = 8 → x - 2y = 4)
    gcd_val = gcd(gcd(abs(A), abs(B)), abs(C))
    A_simplified = A // gcd_val
    B_simplified = B // gcd_val
    C_simplified = C // gcd_val
    
    # Ensure A ≥ 0
    if A_simplified < 0:
        A_simplified *= -1
        B_simplified *= -1
        C_simplified *= -1
    
    # Build standard form equation
    standard_eq_parts = []
    if A_simplified != 0:
        standard_eq_parts.append(f"{A_simplified}x" if A_simplified != 1 else "x")
    if B_simplified != 0:
        if B_simplified > 0:
            standard_eq_parts.append(f" + {B_simplified}y" if B_simplified != 1 else " + y")
        else:
            standard_eq_parts.append(f" - {-B_simplified}y" if B_simplified != -1 else " - y")
    standard_eq_parts.append(f" = {C_simplified}")
    standard_eq = "".join(standard_eq_parts).replace("+ -", "- ")
    
    return slope_intercept_eq, standard_eq

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
gradient = float(input("Enter the gradient (m): "))

slope_intercept, standard = simplify_equation(x1, y1, gradient)

print("\nEquation of the line:")
print(f"Slope-intercept form: {slope_intercept}")
print(f"Standard form: {standard}")
