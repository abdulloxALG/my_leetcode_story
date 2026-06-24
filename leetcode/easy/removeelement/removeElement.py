from typing import List

def removeElement(nums: List[int], val: int) -> int:
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

# Test qilish:
nums = [3, 2, 2, 3]
val = 3

k = removeElement(nums, val)

print("k =", k)
print("yangilangan massiv =", nums[:k])