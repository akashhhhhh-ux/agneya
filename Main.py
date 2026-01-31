class Solution:
    def moveZeroes(self, nums):
        index = 0   # Position to place the next non-zero element

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1

        # Fill the remaining positions with 0
        for i in range(index, len(nums)):
            nums[i] = 0
