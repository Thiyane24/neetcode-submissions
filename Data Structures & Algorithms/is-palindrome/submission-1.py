class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        if s==s[::-1]:
            return True
        else:
            return False

s = "Was it a car or a cat I saw?"
sol=Solution()

print(sol.isPalindrome(s))