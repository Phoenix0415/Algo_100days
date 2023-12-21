from array_hash_table import ArrayHashTable, Pair

def main():
    print("initialize a hash table (or hash map)")
    htable: ArrayHashTable = ArrayHashTable()
    print("")
    
    print("add key-value pairs (key, value) into the hash table one by one using put() method, then print the hash table")
    htable.put(12836, "Lily")
    htable.put(15937, "Tom")
    htable.put(16750, "Jack")
    htable.put(13276, "Rose")
    htable.put(10583, "Jerry")
    htable.print()
    print("")
    
    hash_value: int = htable.hash_func(15937)
    print("hash value of 15937:", hash_value)
    hash_value: int = htable.hash_func(10583)
    print("hash value of 10583:", hash_value)
    print("")
    
    print("search the value by key")
    name: str = htable.get(15937)
    print("searched value by key 15937:",name)
    print("")
    
    print("get all key-value pairs")
    pairs: list[Pair] = htable.entry_set()
    for pair in pairs:
        print(pair.key, "->", pair.val)
    print("")
    
    print("get all keys")
    keys: list[int] = htable.key_set()
    for key in keys:
        print(key)
    print("")
    
    print("get all values")
    values: list[str] = htable.value_set()
    for value in values:
        print(value)
    print("")
    
    print("delete the key-value pair (10583:Jerry) by key")
    htable.remove(10583)
    print("after deleting the key-value pair:")
    htable.print()
    
if __name__ == "__main__":
    main()
    
    
    