class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        res = 0
        y = x
        while x > 0:
            res = res * 10 + x % 10
            x = x//10
        if res == y: return True
        return False


        