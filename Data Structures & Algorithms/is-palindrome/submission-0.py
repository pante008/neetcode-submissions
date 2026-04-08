class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean=""
        for i in s:
            if i.isalnum():
                
                clean+=i.lower()

        if clean==clean[::-1]:
            return True
        else:
            return False
        