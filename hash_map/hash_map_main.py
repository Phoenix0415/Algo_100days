from array_hash_map import ArrayHashMap, Pair

def main():
    print("initialize a hash map (or hash table)")
    hmap: ArrayHashMap = ArrayHashMap()
    print("")
    
    print("add key-value pairs (key, value) into the hash map one by one using put() method, then print the hash map")
    hmap.put(12836, "Lily")
    hmap.put(15937, "Tom")
    hmap.put(16750, "Jack")
    hmap.put(13276, "Rose")
    hmap.put(10583, "Jerry")
    hmap.print()
    print("")
    
    print("search the value by key")
    name: str = hmap.get(15937)
    print("searched value by key 15937:",name)
    print("")
    
    print("get all key-value pairs")
    pairs: list[Pair] = hmap.entry_set()
    for pair in pairs:
        print(pair.key, "->", pair.val)
    print("")
    
    print("get all keys")
    keys: list[int] = hmap.key_set()
    for key in keys:
        print(key)
    print("")
    
    print("get all values")
    values: list[str] = hmap.value_set()
    for value in values:
        print(value)
    print("")
    
    print("delete the key-value pair (10583:Jerry) by key")
    hmap.remove(10583)
    print("after deleting the key-value pair:")
    hmap.print()
    
if __name__ == "__main__":
    main()
    
    
    