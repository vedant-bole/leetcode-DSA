class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        num = 0
        new = 0
        palandrom = False
        if x >= 0:
            num = n%10
            n = n//10
            while n >0:
                new = n%10
                num= (num*10)+new
                n = n//10
            if num == x:
                palandrom = True
        return palandrom