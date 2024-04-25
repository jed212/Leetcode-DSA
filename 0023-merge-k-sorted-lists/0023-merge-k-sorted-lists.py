# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = result = ListNode()
        if not lists:
            return None
        
        def mergeSorted(li1, li2):
            dummy = ListNode()
            cur = dummy
            
            while li1 and li2:
                if li1.val < li2.val:
                    cur.next = li1
                    li1 = li1.next
                else:
                    cur.next = li2
                    li2 = li2.next
                cur = cur.next
                
            cur.next = li1 or li2
            return dummy.next
                
        def mergeSort(lists):
            if len(lists) <= 1:
                return lists[0]
            
            mid = len(lists) // 2
            l1 = mergeSort(lists[:mid])
            l2 = mergeSort(lists[mid:])
            
            return mergeSorted(l1, l2)
        return mergeSort(lists)