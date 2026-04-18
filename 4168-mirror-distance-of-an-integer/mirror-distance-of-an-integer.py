class Solution:
    def mirrorDistance(self, n: int) -> int:
        ori=n
        rev=0
        while n>0:
            last_digit=n%10
            rev=rev*10+last_digit
            n=n//10
        ans=abs(ori-rev)
        return ans