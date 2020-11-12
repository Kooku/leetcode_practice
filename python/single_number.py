class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Link to problem: https://leetcode.com/problems/single-number

        We can utilize extra memory (list or hashmap) to figure out the single number.
        This will result O(n) runtime with O(n) space complexity

        Optimal solution is to use the bit manipulation, XOR.
        By nature, performing XOR to the same bits results `0` (or canceling),
        so we can XOR all the numbers in the array and
        the resultant will be the single number
        """

        number = 0
        for num in nums:
            number ^= num
        return number
