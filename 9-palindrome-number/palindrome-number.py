class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l = list(x)
        l2 = []
        
        for i in range(len(l)):
            l2.append(l[-(i+1)])
        
        x2 = ''.join(l2)
        
        if x == x2:
            return True
        else:
            return False
        