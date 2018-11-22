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
        if len(s) == 0:
            return 0
        last_dict = {}
        start = 0
        max_length = 0
        for index in range(len(s)):
            c = s[index]
            length = index - start + 1
            if c in last_dict:
                i = last_dict[c]
                if i >= start:
                    start = i + 1
                    length = length - 1
            max_length = max(max_length, length)
            last_dict[c] = index
        return max_length

    @staticmethod
    def find_median_sorted_arrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m > n:
            m,n,nums1,nums2 = n,m,nums2,nums1
        if n == 0:
            return None
        for i in range(m + 1):
            j = (m + n + 1)//2 - i
            left2 = None
            left1 = None
            right2 = None
            right1 = None
            if i - 1 >= 0:
                left1 = nums1[i - 1]
                left2 = left1
            if i < m:
                right1 = nums1[i]
                right2 = right1
            if j - 1 >= 0:
                left2 = nums2[j - 1]
                if left1 is None: left1 = left2
            if j < n:
                right2 = nums2[j]
                if right1 is None: right1 = right2
            if right1 is None and right2 is None: 
                right1 = left1
                right2 = left2
            if left2 <= right1 and left1 <= right2:
                if (m + n) % 2 == 1: return max(left1, left2)
                else: return (max(left1, left2) + min(right1, right2))/2

    @staticmethod
    def longestPalindrome(s):
        for i in range(len(s)):
            c = s[i]
            m,n = i
            
        return 0

s = [1, 2, 5]
print(Solution.longestPalindrome(s))