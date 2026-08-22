class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sumi = 0
        mul = 1

        num = str(n)

        for digit in num:
            digit = int(digit)
            sumi += digit
            mul *= digit

        ans = sumi + mul

        return n % ans == 0