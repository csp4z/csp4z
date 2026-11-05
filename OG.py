"""
PROGRAM CREDIT:
Original Algorithm: Countess Ada Lovelace (1843)
Published in: "Notes by the Translator" for Luigi Menabrea's paper on Babbage's Analytical Engine.
Description: The world's first computer algorithm, designed to compute Bernoulli numbers.
"""

from fractions import Fraction
from math import comb

def ada_lovelace_bernoulli(n: int) -> Fraction:
    """
    Computes the n-th Bernoulli number using the recursive 
    derivation logic outlined in Ada Lovelace's Note G (1843).
    """
    if n == 0:
        return Fraction(1, 1)
    
    # Lovelace's formulation effectively solves a recursive system of linear equations
    total_sum = Fraction(0, 1)
    for k in range(n):
        total_sum += comb(n + 1, k) * ada_lovelace_bernoulli(k)
        
    # Isolate the current Bernoulli number
    return Fraction(1, 1) - (total_sum / (n + 1))

# --- Verification Test ---
if __name__ == "__main__":
    print("--- ADA LOVELACE'S ALGORITHM (1843) ---")
    print("Testing even-indexed Bernoulli numbers (Note: Odd indices > 1 are 0):")
    
    for i in [0, 1, 2, 4, 6, 8]:
        print(f"B({i}) = {ada_lovelace_bernoulli(i)}")
