# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        list_node_len = 0
        node = head
        while node:
            list_node_len += 1
            node = node.next

        node = head
        head = self.reverse_(node, k, list_node_len)
        return head

    def reverse_(self, head, k, rest_len):
        if k > rest_len:
            return head

        node = head
        next_node = node.next
        count = k - 1
        while count:
            tmp = next_node.next
            if count == 1:
                head.next = self.reverse_(tmp, k, rest_len - k)
                next_node.next = node
                node = next_node
            else:
                next_node.next = node
                node = next_node
                next_node = tmp
            count -= 1
        return node


if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)
    test = Solution()
    res = test.reverseKGroup(root, 2)
    print(res.val)
    print(res.next.val)
    print(res.next.next.val)
    print(res.next.next.next.val)
    print(res.next.next.next.next.val)