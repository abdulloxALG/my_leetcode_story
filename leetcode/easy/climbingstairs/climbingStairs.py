class Solution:
    def climbStairs(self, n):
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one


# ==========================
# Test qilish
# ==========================

solution = Solution()

n = 5
result = solution.climbStairs(n)

print("n =", n)
print("Natija:", result)