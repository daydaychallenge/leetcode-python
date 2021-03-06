
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        #### [445. Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/)

        You are given two **non-empty** linked lists representing two  non-negative integers. The most significant digit comes first and each  of their nodes contain a single digit. Add the two numbers and return it as a linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.

        **Follow up:**
         What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

        **Example:**

        ```
        Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 8 -> 0 -> 7
        ```

        Parameters
        ----------
        l1: ListNode
        l2: ListNode

        Returns
        -------
        ListNode

        Examples
        --------

        Notes
        -----

        References
        ---------

        """
        s1, s2 = [], []

        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next

        dummy = ListNode(0)
        carry = 0

        while s1 or s2 or carry:
            if s1:
                carry += s1.pop()
            if s2:
                carry += s2.pop()
            carry, val = divmod(carry, 10)
            dummy.next, dummy.next.next = ListNode(val), dummy.next
        return dummy.next

