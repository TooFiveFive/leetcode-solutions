import math
class Solution:
	def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
		nums1.extend(nums2)
		nums1.sort()

		if len(nums1) % 2 == 1:
			return float(nums1[math.floor(len(nums1)/2)])
		else:
			mid = len(nums1)//2
			return float((nums1[mid] + nums1[mid-1])/2)