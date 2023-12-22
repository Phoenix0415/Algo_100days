class Pair:
    """the class of key-value pair"""

    def __init__(self, key: int, val: str):
        self.key = key
        self.val = val

class HashTableChaining:
    """hash table (or hash map) implemented by chaining"""

    def __init__(self):
        """constructor"""
        self.size = 0  # the number of key-value pairs
        self.capacity = 4  # the capacity of hash table
        self.load_thres = 2.0 / 3.0  # the load factor threshold for extending
        self.extend_ratio = 2  # the extend ratio
        self.buckets = [[] for _ in range(self.capacity)]  # the buckets

    def hash_func(self, key: int) -> int:
        """hash function"""
        return key % self.capacity

    def load_factor(self) -> float:
        """load factor"""
        return self.size / self.capacity

    def get(self, key: int) -> str | None:
        """search"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # traverse the bucket, if the key is found, return the corresponding value
        for pair in bucket:
            if pair.key == key:
                return pair.val
        # if the key is not found, return None
        return None

    def put(self, key: int, val: str):
        """add or update"""
        # when the load factor is greater than the threshold, extend the hash table
        if self.load_factor() > self.load_thres:
            self.extend()
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # traverse the bucket, if the key is found, update the corresponding value
        for pair in bucket:
            if pair.key == key:
                pair.val = val
                return
        # if the key is not found, add the key-value pair to the bucket
        pair = Pair(key, val)
        bucket.append(pair)
        self.size += 1

    def remove(self, key: int):
        """delete"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # traverse the bucket, if the key is found, remove the key-value pair
        for pair in bucket:
            if pair.key == key:
                bucket.remove(pair)
                self.size -= 1
                break

    def extend(self):
        """extend the hash table"""
        # store the old buckets
        buckets = self.buckets
        # initialize a new hash table with extended capacity
        self.capacity *= self.extend_ratio
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        # move the key-value pairs from the old buckets to the new buckets
        for bucket in buckets:
            for pair in bucket:
                self.put(pair.key, pair.val)

    def print(self):
        """print the hash table"""
        for bucket in self.buckets:
            res = []
            for pair in bucket:
                res.append(str(pair.key) + " -> " + pair.val)
            print(res)