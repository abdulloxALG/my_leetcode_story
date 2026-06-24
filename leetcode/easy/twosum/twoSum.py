from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for ikkinchi in range(i + 1, len(nums)):
            if nums[i] + nums[ikkinchi] == target:
                return [i, ikkinchi]

nums = [2, 7, 11, 15]
target = 9

result = twoSum(nums, target)
print(result)