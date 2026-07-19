class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        div = 0
        n = num
        while n > 0:
            div = n%10
            n = n//10
            if num%div == 0:
                count +=1
        return count

        