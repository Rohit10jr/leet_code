'''
69. Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:

Input: x = 4
Output: 2

Example 2:

Input: x = 8
Output: 2

'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        left, right = 1, x  
        ans = 0 # This will store the largest integer whose square is less than or equal to x

        while left <= right:
            mid = left + (right - left) // 2
            # Use mid * mid directly for comparison.
            # Be careful with potential overflow for very large x if Python didn't handle large integers automatically.
            # In other languages (like C++/Java), you might cast mid to a long long before multiplication.
            # Python integers handle arbitrary precision, so overflow is not a typical concern here.
            square = mid * mid

            if square == x:
                return mid  # Found the exact square root
            elif square < x:
                ans = mid  # mid could be the answer, try to find a larger one
                left = mid + 1
            else: # square > x
                right = mid - 1 # mid is too large, search in the left half

        return ans

# Example Usage:
solution = Solution()
print(f"sqrt(4) = {solution.mySqrt(4)}")    # Output: 2
print(f"sqrt(8) = {solution.mySqrt(8)}")    # Output: 2
print(f"sqrt(0) = {solution.mySqrt(0)}")    # Output: 0
print(f"sqrt(1) = {solution.mySqrt(1)}")    # Output: 1
print(f"sqrt(9) = {solution.mySqrt(9)}")    # Output: 3
print(f"sqrt(2147483647) = {solution.mySqrt(2147483647)}") # Max int in 32-bit, output should be 46340