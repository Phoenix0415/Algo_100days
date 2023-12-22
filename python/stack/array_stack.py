class ArrayStack:
    """implement stack with array"""

    def __init__(self):
        """constructor"""
        self._stack: list[int] = []

    def size(self) -> int:
        """get the size of the stack"""
        return len(self._stack)

    def is_empty(self) -> bool:
        """whether the stack is empty"""
        return self._stack == []

    def push(self, item: int):
        """push element into the stack"""
        self._stack.append(item)

    def pop(self) -> int:
        """pop element out of the stack"""
        if self.is_empty():
            raise IndexError("the stack is empty")
        return self._stack.pop()

    def peek(self) -> int:
        """get the element on the top"""
        if self.is_empty():
            raise IndexError("the stack is empty")
        return self._stack[-1]

    def to_list(self) -> list[int]:
        """convert the stack to list"""
        return self._stack
