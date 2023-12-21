class Pair:
    """the class of key-value pair"""

    def __init__(self, key: int, val: str):
        self.key = key
        self.val = val

class ArrayHashMap:
    """hash map implemented by array"""

    def __init__(self):
        """constructor"""
        # initialize an array, which contains 100 buckets
        self.buckets: list[Pair | None] = [None] * 100

    def hash_func(self, key: int) -> int:
        """hash function"""
        index = key % 100
        return index

    def get(self, key: int) -> str:
        """search"""
        index: int = self.hash_func(key)
        pair: Pair = self.buckets[index]
        if pair is None:
            return None
        return pair.val

    def put(self, key: int, val: str):
        """add or update"""
        pair = Pair(key, val)
        index: int = self.hash_func(key)
        self.buckets[index] = pair

    def remove(self, key: int):
        """delete"""
        index: int = self.hash_func(key)
        # set the bucket to None, which means the key-value pair is deleted
        self.buckets[index] = None

    def entry_set(self) -> list[Pair]:
        """get all key-value pairs"""
        result: list[Pair] = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair)
        return result

    def key_set(self) -> list[int]:
        """get all keys"""
        result = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.key)
        return result

    def value_set(self) -> list[str]:
        """get all values"""
        result = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.val)
        return result

    def print(self):
        """print the hash map"""
        for pair in self.buckets:
            if pair is not None:
                print(pair.key, "->", pair.val)