class Pair:
    """the class of key-value pair"""

    def __init__(self, key: int, val: str):
        self.key = key
        self.val = val

class HashTableOpenAddressing:
    """hash table implemented by open addressing"""

    def __init__(self):
        """constructor"""
        self.size = 0  # the number of key-value pairs
        self.capacity = 4  # capacity of hash table
        self.load_thres = 2.0 / 3.0  # the threshold of load factor for extending
        self.extend_ratio = 2  # the extend ratio
        self.buckets: list[Pair | None] = [None] * self.capacity  # the buckets
        self.TOMBSTONE = Pair(-1, "-1")  # the tombstone

    def hash_func(self, key: int) -> int:
        """hash function"""
        return key % self.capacity

    def load_factor(self) -> float:
        """the load factor"""
        return self.size / self.capacity

    def find_bucket(self, key: int) -> int:
        """find the bucket index of the key"""
        index = self.hash_func(key)
        first_tombstone = -1
        # linear probing to find the bucket index
        while self.buckets[index] is not None:
            # if the key is found, return the bucket index
            if self.buckets[index].key == key:
                # if the bucket is a tombstone, move the key-value pair to the first tombstone
                if first_tombstone != -1:
                    self.buckets[first_tombstone] = self.buckets[index]
                    self.buckets[index] = self.TOMBSTONE
                    return first_tombstone  # return the first tombstone index
                return index  # return the bucket index
            # record the first tombstone index
            if first_tombstone == -1 and self.buckets[index] is self.TOMBSTONE:
                first_tombstone = index
            # calculate the next index, and make sure it is in the range of the array
            index = (index + 1) % self.capacity
        # if the key is not found, return the first tombstone index if it exists, otherwise return the bucket index
        return index if first_tombstone == -1 else first_tombstone

    def get(self, key: int) -> str:
        """search"""
        # search the bucket index of the key
        index = self.find_bucket(key)
        # if the key is found, return the corresponding value
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            return self.buckets[index].val
        # if the key is not found, return None
        return None

    def put(self, key: int, val: str):
        """add or update"""
        # when the load factor is greater than the threshold, extend the hash table
        if self.load_factor() > self.load_thres:
            self.extend()
        # search the bucket index of the key
        index = self.find_bucket(key)
        # if the key exists, update the corresponding value
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            self.buckets[index].val = val
            return
        # if the key does not exist, add the key-value pair to the bucket
        self.buckets[index] = Pair(key, val)
        self.size += 1

    def remove(self, key: int):
        """删除操作"""
        # search the bucket index of the key
        index = self.find_bucket(key)
        # if the key-value pair was found, set the bucket to the tombstone
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            self.buckets[index] = self.TOMBSTONE
            self.size -= 1

    def extend(self):
        """extend the hash table"""
        # store the old hash table
        buckets_tmp = self.buckets
        # initialize a new hash table with extended capacity
        self.capacity *= self.extend_ratio
        self.buckets = [None] * self.capacity
        self.size = 0
        # move the key-value pairs from the old hash table to the new hash table
        for pair in buckets_tmp:
            if pair not in [None, self.TOMBSTONE]:
                self.put(pair.key, pair.val)

    def print(self):
        """print the hash table"""
        for pair in self.buckets:
            if pair is None:
                print("None")
            elif pair is self.TOMBSTONE:
                print("TOMBSTONE")
            else:
                print(pair.key, "->", pair.val)