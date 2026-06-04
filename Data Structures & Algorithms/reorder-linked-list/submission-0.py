# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        list_of_nodes = []
        while head:
            list_of_nodes.append(head)
            head = head.next
        left_pointer = 0
        right_pointer = len(list_of_nodes) - 1

        while left_pointer < right_pointer:
            list_of_nodes[left_pointer].next = list_of_nodes[right_pointer]
            list_of_nodes[right_pointer].next = list_of_nodes[left_pointer + 1]
            left_pointer += 1
            right_pointer -= 1
        list_of_nodes[left_pointer].next = None
        