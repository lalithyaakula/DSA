class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums=list(tokens)
        while len(nums)>1:
            for i in range(len(nums)):
                t=nums[i]
                if t in {'+','-','*','/'}:
                    a=int(nums[i-2])
                    b=int(nums[i-1])
                    val=0
                    if t=='+':
                        val=a+b
                    elif t=='-':
                        val=a-b
                    elif t=='*':
                        val=a*b
                    else:
                        val=int(a/b)
                    nums[i-2]=str(val)
                    nums.pop(i)
                    nums.pop(i-1)
                    break
        return int(nums[0])




