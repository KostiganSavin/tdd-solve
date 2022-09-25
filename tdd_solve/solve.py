from math import sqrt, isnan, isinf
from typing import List

def solve(a: float, b: float, c: float, eps = 0.0000001) -> List[float]:
    for param in (a, b, c):
        if isnan(param):
            raise ValueError("params could not be 'NaN'")
        if isinf(param):
            raise ValueError("params could not be Infinity")

    if abs(a) < eps:
        raise ValueError("'a' could not be equals 0")
    result = []
    d = b * b - 4 * a * c
    print(d)
    if d > eps:
        result = [(-b + sqrt(d)) / 2 * a, (-b - sqrt(d)) / 2 * a]
    if abs(d) < eps:
        result =  [-b / 2 * a]
    
    return result
