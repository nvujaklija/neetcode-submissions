class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        tail = head
        reordered = []
        while tail:
            reordered.append(tail)
            tail = tail.next
        
        curr = head
        for i in range(len(reordered)//2):
            nxt = curr.next
            new = reordered.pop()
            curr.next = new
            new.next = nxt
            curr = nxt
        
        if curr:
            curr.next = None