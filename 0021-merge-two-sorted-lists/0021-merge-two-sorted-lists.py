class Solution:
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		flag = ListNode()
		p, q, current = list1, list2, flag
		while p and q:
			if p.val < q.val:
				current.next = p
				p = p.next
			else:
				current.next = q
				q = q.next
			current = current.next
		current.next = p if p else q

		return flag.next