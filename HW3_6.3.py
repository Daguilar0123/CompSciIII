"""
Problem 6.3:
Implement the recursive approach to raising a number to a power,
as described in the “Raising a Number to a Power” section near the end
of this chapter. Write the recursive power() function. For extra utility,
make use of this transformation to handle negative integer exponents:
    x^y = 1 / x^(-y) when y < 0

Test your function on several combinations including positive and
negative integers and the special cases where the exponent is 0 and 1
(x^0 = 1 and x^1 = x).
"""

def power(x, y):
    """
    Recursive power() per Problem 6.3:

    - Special cases:
        * exponent == 0  → return 1          # “x^0 = 1”
        * exponent == 1  → return x          # “x^1 = x”
    - Negative exponent:
        * y < 0 → use 1 / x^(-y)             # “x^y = 1 / x^-y when y < 0”
    - Recursive (y > 1):
        * x^y = x * x^(y-1)
    """
    # ---- Base cases ----
    if y == 0:
        # “x^0 = 1”
        return 1
    if y == 1:
        # “x^1 = x”
        return x

    # ---- Handle negative integer exponents ----
    if y < 0:
        # “x^y = 1 / x^-y when y < 0”
        return 1 / power(x, -y)

    # ---- Recursive step for positive y > 1 ----
    # “x^y = x * x^(y-1)”
    return x * power(x, y - 1)


# ---------------- Demo / Output ----------------
if __name__ == "__main__":
    # Positive exponent tests
    print("power(2, 0)   # special case x^0=1  →", power(2, 0))
    print("power(5, 1)   # special case x^1=x  →", power(5, 1))
    print("power(3, 3)   # 3^3 = 27            →", power(3, 3))

    # Larger positive exponent
    print("power(2, 10)  # 2^10 = 1024         →", power(2, 10))

    # Negative exponent tests
    print("power(2, -1)  # 2^-1 = 1/2          →", power(2, -1))
    print("power(5, -3)  # 5^-3 = 1/125        →", power(5, -3))

    # Mixed sign
    print("power(-2, 3)  # (-2)^3 = -8         →", power(-2, 3))
    print("power(-2, 4)  # (-2)^4 = 16         →", power(-2, 4))