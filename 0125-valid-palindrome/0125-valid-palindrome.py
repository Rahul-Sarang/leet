class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = ""

        for ch in s:
            if ch.isalnum():
                str1 += ch.lower()

        return str1 == str1[::-1]