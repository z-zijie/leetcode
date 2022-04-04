from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = list1, list2
        root = ListNode(0)
        ptr = root
        while ptr1 is not None or ptr2 is not None:
            if ptr1 is None:
                ptr.next = ListNode(ptr2.val)
                ptr2 = ptr2.next
            elif ptr2 is None:
                ptr.next = ListNode(ptr1.val)
                ptr1 = ptr1.next
            elif ptr1.val < ptr2.val:
                ptr.next = ListNode(ptr1.val)
                ptr1 = ptr1.next
            else:
                ptr.next = ListNode(ptr2.val)
                ptr2 = ptr2.next
            ptr = ptr.next
        return root.next


def create_ListNode_from_list(sorted_list: List):
    root = ListNode(0)
    ptr = root
    for num in sorted_list:
        ptr.next = ListNode(num)
        ptr = ptr.next
    return root.next


if __name__ == "__main__":
    print("[21][Merge Two Sorted Lists]")
    main = Solution()
    l1 = create_ListNode_from_list([0])
    l2 = create_ListNode_from_list([])
    merged = main.mergeTwoLists(l1, l2)
    while merged:
        print(merged.val)
        merged = merged.next