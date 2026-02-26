""" 
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float: # type: ignore
        # Merge the two sorted arrays
        merged = []
        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2): # type: ignore
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        # If there are remaining elements in nums1
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        
        # If there are remaining elements in nums2
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1
        
        # Calculate the median
        n = len(merged)
        if n % 2 == 1:
            return float(merged[n // 2])  # Odd length, return the middle element
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0  # Even length, return the average of the two middle elements