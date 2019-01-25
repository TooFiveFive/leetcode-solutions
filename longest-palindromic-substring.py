class Solution:
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		_s = s[::-1]
		pals = []
		for i1,s1 in enumerate(s):
			for i2,s2 in enumerate(_s):
				if s1 == s2:
					ss = s[i1:len(s)-i2]
					_ss = _s[i2:len(s)-i1]
					if ss == _ss:
						pals.append(ss)
						break
		if len(s) > 0:
			return max(pals, key=len)
		else:
			return s