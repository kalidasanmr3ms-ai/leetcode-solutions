class Solution:
    def swapPairs(self, head):
        # if list is empty or has only one node, nothing to swap
        if head == None:
            return head
        if head.next == None:
            return head
        
        # make a dummy node that points to head
        # this makes it easier to handle swapping the very first pair
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        current = head
        
        while current != None and current.next != None:
            first = current
            second = current.next
            
            # do the actual swap
            first.next = second.next
            second.next = first
            prev.next = second
            
            # move prev and current forward for the next pair
            prev = first
            current = first.next
        
        return dummy.next
