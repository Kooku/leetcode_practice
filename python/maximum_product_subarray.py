class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Problem link: https://leetcode.com/problems/maximum-product-subarray/

        Brute force solution: O(n^2) Nested for loops trying all possible combinations

        Optimal solution: O(n)
        Keep a running minimum, maximum product and the max throughout the iteration.

        For the cases where we would have a new max from a positive * positive, we have cur_max
        For the cases where we would have a new max from a negative * negative, we have cur_min
        Once we have a new max, we track the value by using total_max and return the total_max in the end.
        """ 
        cur_max = cur_min = total_max = nums[0]

        for num in nums[1:]
            # We use temp variables here. If we use cur_max instead of temp_max, we would have incorrect values for temp_min when calculating line 21.
            temp_max = max(num, num * cur_max, num * cur_min)
            temp_min = min(num, num * cur_max, num * cur_min)
            cur_max = temp_max
            cur_min = temp_min
            total_max = max(total_max, cur_max)

        return total_max
