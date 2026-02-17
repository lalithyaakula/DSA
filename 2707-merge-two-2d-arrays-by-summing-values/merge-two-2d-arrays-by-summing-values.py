class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res=[]
        l,r=0,0
        while l<len(nums1) and r<len(nums2):
           id1,val1=nums1[l]
           id2,val2=nums2[r]
           if id1<id2:
             res.append([id1,val1])
             l+=1
           elif id1>id2:
             res.append([id2,val2])
             r+=1
           else:
             res.append([id1,val1+val2])
             l+=1
             r+=1
        while l<len(nums1):
            res.append(nums1[l])
            l+=1
        while r<len(nums2):
            res.append(nums2[r])
            r+=1
        return res

