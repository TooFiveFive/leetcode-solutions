class Solution:
	def firstMissingPositive(self, nums: list) -> int:
		n = set(nums)
		i = 1
		while i in n and i <= len(nums):
			i += 1
		return i