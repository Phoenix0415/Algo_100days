import linked_list

class LinkedListStack:
    """implement stack with linked list"""

    def __init__(self):
        """constructor"""
        self._peek: ListNode | None = None
        self._size: int = 0

    def size(self) -> int:
        """get the size of the stack"""
        return self._size

    def is_empty(self) -> bool:
        """whether the stack is empty"""
        return not self._peek

    def push(self, val: int):
        """push element into the stack"""
        node = ListNode(val)
        node.next = self._peek
        self._peek = node
        self._size += 1

    def pop(self) -> int:
        """pop element out of the stack"""
        num = self.peek()
        self._peek = self._peek.next
        self._size -= 1
        return num

    def peek(self) -> int:
        """get the element on the top"""
        if self.is_empty():
            raise IndexError("the stack is empty")
        return self._peek.val

    def to_list(self) -> list[int]:
        """convert the stack to list"""
        arr = []
        node = self._peek
        while node:
            arr.append(node.val)
            node = node.next
        arr.reverse()
        return arr