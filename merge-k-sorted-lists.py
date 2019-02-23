class Solution:
	o = []
	def mergeKLists(self, lists: list) -> ListNode:
		for l in lists:
			self.it(l)
		self.o.sort(reverse=True)
		if len(self.o) > 0:
			return self.ret()
		else:
			return None
	def it(self, l):
		if l != None:
			self.o.append(l.val)
			if l.next != None:
				self.it(l.next)
	def ret(self):
		out = ListNode(self.o.pop())
		if len(self.o) > 0:
			out.next = self.ret()
		return out