import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import ListNode, list_to_linked_list


def linear_search_array(nums: list[int], target: int) -> int:
    """linear search (array)"""
    # traverse the array
    for i in range(len(nums)):
        if nums[i] == target:  # found the target element, return its index
            return i
    return -1  # if the target element does not exist in the array, return -1   


def linear_search_linkedlist(head: ListNode, target: int) -> ListNode | None:
    """linear search (linked list)"""
    # traverse the linked list
    while head:
        if head.val == target:  # found the target node, return it
            return head
        head = head.next
    return None  # the target node does not exist in the linked list, return None


"""Driver Code"""
if __name__ == "__main__":
    target = 3

    # linear search on array
    nums = [1, 5, 3, 2, 4, 7, 5, 9, 10, 8]
    index: int = linear_search_array(nums, target)
    print("the index of target element 3 is", index)

    # linear search on linked list
    head: ListNode = list_to_linked_list(nums)
    node: ListNode | None = linear_search_linkedlist(head, target)
    print("the corresponding node of target element 3 is", node)