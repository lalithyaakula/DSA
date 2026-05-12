class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in range(0,len(nums1)):
            found=False
            for j in range(0,len(nums2)):
                if nums1[i]==nums2[j]:
                    for k in range(j+1,len(nums2)):
                        if nums2[k]>nums2[j]:
                            ans.append(nums2[k])
                            found=True
                            break
                    if not found:
                        ans.append(-1)
        return ans