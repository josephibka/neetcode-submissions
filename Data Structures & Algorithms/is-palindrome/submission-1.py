class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_holder = ""
        for char in s:
            if char.isalnum():
                s_holder  += char.lower()
        s = s_holder                

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True