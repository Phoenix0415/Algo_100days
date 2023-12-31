import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import ListNode, list_to_linked_list


def hashing_search_array(hmap: dict[int, int], target: int) -> int:
    """hashing search (array)"""
    # the key of the hash map is the element, and the value is the index
    # if the key does not exist in the hash map, return -1
    return hmap.get(target, -1)


def hashing_search_linkedlist(
    hmap: dict[int, ListNode], target: int
) -> ListNode | None:
    """hashing search (linked list)"""
    # the key of the hash map is the node value, and the value is the node
    # if the key does not exist in the hash map, return None
    return hmap.get(target, None)


"""Driver Code"""
if __name__ == "__main__":
    target = 3

    # hashing search (array)
    nums = [1, 5, 3, 2, 4, 7, 5, 9, 10, 8]
    # initialize the hash map
    map0 = dict[int, int]()
    for i in range(len(nums)):
        map0[nums[i]] = i  # key: element, value: index
    index: int = hashing_search_array(map0, target)
    print("the index of target element 3 is:", index)   

    # hashing search (linked list)
    head: ListNode = list_to_linked_list(nums)
    # initialize the hash map
    map1 = dict[int, ListNode]()
    while head:
        map1[head.val] = head  # key: node value, value: node
        head = head.next
    node: ListNode = hashing_search_linkedlist(map1, target)
    print("the corresponding node of target element 3 is:", node)