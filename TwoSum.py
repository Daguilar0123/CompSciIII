from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x]=i
        raise ValueError("No two-sum solution")
    
# Example usage:
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)  # Output: [0, 1]

#Example 2:
# nums = [3, 2, 4]
# target = 6
# solution = Solution()
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(result2)  # Output: [1, 2]
# Example 3:
    nums3 = [3, 1, -3, 8, 3]
    target3 = 11
    result3 = solution.twoSum(nums3, target3)
    print(result3)  # Output: [0, 1]