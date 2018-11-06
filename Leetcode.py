# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    @staticmethod
    def two_sum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num = {}
        for i in range(len(nums)):
            num1 = nums[i]
            num2 = target - num1
            if num2 in num:
                return [num[num2], i]
            else:
                num[num1] = i
        raise RuntimeError("no two sum solution")

    @staticmethod
    def add_two_numbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            l1 = ListNode(0)
        if l2 is None:
            l2 = ListNode(0)
        num = l1.val + l2.val
        node = ListNode(num % 10)
        if num >= 10:
            n = num / 10
            ne = l1.next
            if ne is None:
                l1.next = ListNode(n)
            else:
                ne.val = ne.val + n

        node.next = Solution.add_two_numbers(l1.next, l2.next)
        return node

    @staticmethod
    def length_of_longest_substring(s):
        """
        :type s: str
        :rtype: int
        """


two_sum = Solution.two_sum([2, 3, 7, 9], 9)
print(two_sum)

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
add_two_num = Solution.add_two_numbers(l1, l2)
while add_two_num is not None:
    print(add_two_num.val)
    add_two_num = add_two_num.next
