def two_sum_brute_force(nums: list[int], target: int) -> list[int]:
    """the first approach: brute force"""
    # double loop, time complexity is O(n^2)
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_hash_table(nums: list[int], target: int) -> list[int]:
    """the second approach: hash table"""
    # with a hash table as a complement, the time complexity can be reduced to O(n)
    dic = {}
    # single loop, time complexity is O(n)
    for i in range(len(nums)):
        if target - nums[i] in dic:
            # return the index of the complement and the current index
            return [dic[target - nums[i]], i] 
        dic[nums[i]] = i
    return []


"""Driver Code"""
if __name__ == "__main__":
    # ======= Test Case =======
    nums = [2, 7, 11, 15]
    target = 13

    # ====== Driver Code ======
    # approach 1
    res: list[int] = two_sum_brute_force(nums, target)
    print("approach 1 res =", res) # [0, 2]
    # approach 2
    res: list[int] = two_sum_hash_table(nums, target)
    print("approach 2 res =", res)  # [0, 2]