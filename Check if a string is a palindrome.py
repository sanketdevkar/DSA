# Function to recursively check if a string is a palindrome
def f(i, n, s):
    # BASE CASE: If the left pointer reaches or passes the midpoint, 
    # all character pairs have matched successfully.
    if i >= n // 2:
        return True 

    # RECURSIVE CONDITION: Compare the character from the start s[i] 
    # with its matching character from the end s[n - i - 1]
    if s[i] != s[n - i - 1]:
        return False # Characters don't match -> Not a palindrome
    
    # RECURSIVE STEP: Move to the next pair of characters (i + 1)
    return f(i + 1, n, s)


# Driver code
String = input("Enter a string To check it is palindrome or not :")
n = len(String)

# Call the function with initial index 0 and print the result
print(f(0, n, String))


"""1. General Rules for Recursion
Base Case is Required: Always define a base case (e.g., if i >= n // 2: return True) at the top of your function to prevent infinite recursive loops (RecursionError).

Pass the Result Back: Always use the return keyword when making recursive calls (e.g., return f(i + 1, ...)). Omitting return causes the function to return None instead of the inner result.

Progress Towards Base Case: Ensure state variables change on every recursive call (e.g., i + 1) so the algorithm eventually hits the base condition.

2. Two-Pointer Palindrome Logic
Symmetric Index Formula: To compare elements from opposite ends of a sequence of length n:

Left element: s[i]

Right element: s[n - i - 1]

Optimization: You only need to loop or recurse up to n // 2 (the midpoint). Beyond that, you are re-checking pairs you have already compared.

3. Complexity Quick Reference
Time Complexity: O(n)

The function makes at most n/2 checks, which simplifies to linear time O(n).

Space Complexity: O(n)

Because recursion uses the function call stack, n/2 active stack frames exist in memory at the maximum depth.

Iterative Alternative (Loop): An iterative while loop implementation achieves O(n) time complexity but reduces space complexity to O(1) by avoiding call-stack overhead."""
