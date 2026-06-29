def longestPalindrome(s):
    seen = set()
    res = 0

    for c in s:
        if c in seen:
            seen.remove(c)
            res += 2
        else:
            seen.add(c)

    return res + 1 if seen else res


# Test
s = "abccccdd"
natija = longestPalindrome(s)

print("String:", s)
print("Eng uzun palindrome uzunligi:", natija)