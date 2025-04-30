import math

def lcm_and_gcd(a, b):
    gcd = math.gcd(a, b)
    lcm = abs(a * b) // gcd
    return lcm, gcd