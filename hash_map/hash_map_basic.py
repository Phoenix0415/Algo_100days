# initialize a hash map (or hash table)
hmap: dict = {}

# add
# add a key-value pair (key, value) into the hash map
hmap[12836] = "Lily"
hmap[15937] = "Tom"
hmap[16750] = "Jack"
hmap[13276] = "Rose"
hmap[10583] = "Jerry"
print("added 5 key-value pairs:",hmap)

# search
# search the value by key
name: str = hmap[15937]
print("searched value by key 15937:",name)

# delete
# delete the key-value pair by key
hmap.pop(10583)
print("deleted key-value pair by key 10583:",hmap)
print("")

# traverse in three ways
# traverse the key-value pair
print("traverse the key-value pair:")
for key, value in hmap.items():
    print(key, "->", value)
print("")
# traverse the key
print("traverse the key:")
for key in hmap.keys():
    print(key)
print("")
# traverse the value
print("traverse the value:")
for value in hmap.values():
    print(value)