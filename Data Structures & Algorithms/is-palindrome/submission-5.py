class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_array = [c.lower() for c in s if           c.isalnum()]

        left = 0
        right = len(char_array) - 1

        while left < right:
            if char_array[left] != char_array[right]:
                return False
            left += 1
            right -= 1
          
        return True
        