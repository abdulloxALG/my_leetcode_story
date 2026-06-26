def removeDuplicates(nums):
    l = 1

    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1

    return l


# Test
nums = [1, 1, 2, 2, 3, 4, 4, 5]

k = removeDuplicates(nums)

print("k =", k)
print("Yangi massiv:", nums[:k])
print("To'liq massiv:", nums)