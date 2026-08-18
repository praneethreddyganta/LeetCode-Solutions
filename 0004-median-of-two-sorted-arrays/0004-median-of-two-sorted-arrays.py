class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_arr=[]
        i=0
        j=0
        while i<len(nums1) and j <len(nums2):
            if nums1[i]<nums2[j]:
                merged_arr.append(nums1[i])
                i+=1
            elif nums1[i]>nums2[j]:
                merged_arr.append(nums2[j])
                j+=1
            else:
                merged_arr.append(nums1[i])
                merged_arr.append(nums2[j])
                i+=1
                j+=1
        while i<len(nums1):
            merged_arr.append(nums1[i])
            i+=1
        while j<len(nums2):
            merged_arr.append(nums2[j])
            j+=1
        n=len(merged_arr)
        if n%2==0:
            return (merged_arr[n//2]+merged_arr[n//2-1])/2
        else:
            return (merged_arr[n//2])