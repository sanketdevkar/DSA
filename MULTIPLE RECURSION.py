"""
====================================================================
HEADER: MULTIPLE RECURSION IN PYTHON (FIBONACCI EXAMPLE)
====================================================================

WHAT IS MULTIPLE RECURSION?
- A recursive function is considered to have "multiple recursion" when 
  it calls itself MORE THAN ONCE within a single execution path.
- In this example, 'fibonacci()' calls itself twice:
  'fibonacci(n - 1)' and 'fibonacci(n - 2)'.

KEY NOTES & TAKEAWAYS:
1. Base Cases:
   - Always define stopping conditions (n <= 0 and n == 1) to prevent 
     infinite recursion and stack overflow errors.
2. Branching Execution (Recursion Tree):
   - Each call spawns two additional calls, creating a binary tree 
     of execution frames.
3. Redundant Calculations:
   - Standard multiple recursion re-computes the same values repeatedly.
     (e.g., fibonacci(3) is calculated multiple times when finding fibonacci(5)).
   - Can be optimized using Memoization / Dynamic Programming.

COMPLEXITY ANALYSIS:
- Time Complexity: O(2^n)
  - Exponential time due to the doubling of function calls at each level.
- Space Complexity: O(n)
  - Linear space required for the call stack corresponding to the height 
    of the recursion tree.
====================================================================
"""


def fibonacci(n):
    # BASE CASES
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # MULTIPLE RECURSION CALLS
    return fibonacci(n - 1) + fibonacci(n - 2)


# Test the function
n = int(input("Enter Number: "))
print(fibonacci(n))
