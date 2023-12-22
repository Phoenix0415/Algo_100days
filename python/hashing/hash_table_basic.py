# initialize a hash table (or hash map)
htable: dict = {}

# add
# add a key-value pair (key, value) into the hash table
htable[12836] = "Lily"
htable[15937] = "Tom"
htable[16750] = "Jack"
htable[13276] = "Rose"
htable[10583] = "Jerry"
print("added 5 key-value pairs:",htable)

# search
# search the value by key
name: str = htable[15937]
print("searched value by key 15937:",name)

# delete
# delete the key-value pair by key
htable.pop(10583)
print("deleted key-value pair by key 10583:",htable)
print("")

# traverse in three ways
# traverse the key-value pair
print("traverse the key-value pair:")
for key, value in htable.items():
    print(key, "->", value)
print("")
# traverse the key
print("traverse the key:")
for key in htable.keys():
    print(key)
print("")
# traverse the value
print("traverse the value:")
for value in htable.values():
    print(value)