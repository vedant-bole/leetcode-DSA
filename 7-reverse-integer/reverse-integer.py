class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        l = list(x)
        l2 = []

        for i in range(len(l) - 1, -1, -1):
            if l[i] != '-' and l[i] != '+':
                l2.append(l[i])

        if l[0] == '-':
            l2.insert(0, '-')
        elif l[0] == '+':
            l2.insert(0, '+')

        x = ''.join(l2)
        x = int(x)

        if x < -2**31 or x > 2**31 - 1:
            return 0

        return x
