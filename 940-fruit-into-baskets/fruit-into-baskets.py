class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq={}
        left=0
        maxi=0
        for r in range(0,len(fruits)):
          freq[fruits[r]]=freq.get(fruits[r],0)+1
          while len(freq)>2:
            freq[fruits[left]]-=1
            if freq[fruits[left]]==0:
                del freq[fruits[left]]
            left+=1
          maxi=max(maxi,r-left+1)
        return maxi
        
         