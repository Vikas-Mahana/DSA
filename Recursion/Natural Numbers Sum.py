"""
Sum of Natural Numbers
Input : n = 3
Output : 6
Explanation : The sum of first 3 natural numbers is 1+2+3 = 6.
"""

def sum(n):
    # base condition
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)