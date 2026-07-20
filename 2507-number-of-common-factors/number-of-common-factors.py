class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        var = a
        count = 1
        i = 2
        if a>b:
            var = b
        while i <= var:
            if a%i == 0 and b%i == 0:
                count+=1
            i+=1
        return count