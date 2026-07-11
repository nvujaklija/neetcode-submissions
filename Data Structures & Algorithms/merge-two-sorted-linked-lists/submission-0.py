# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        while list1 or list2:
            if list1 and list2 and list1.val<list2.val:
                tail.next = ListNode(list1.val)
                tail = tail.next
                list1 = list1.next
            elif list2 and list1 and list2.val<list1.val:
                tail.next = ListNode(list2.val)
                tail = tail.next
                list2 = list2.next
            elif list2 and list1 and list2.val == list1.val:
                tail.next = ListNode(list1.val)
                tail = tail.next
                tail.next = ListNode(list2.val)
                tail = tail.next
                list2 = list2.next
                list1 = list1.next
            elif list1 and not list2:
                tail.next = ListNode(list1.val)
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = ListNode(list2.val)
                tail = tail.next
                list2 = list2.next


        return dummy.next
