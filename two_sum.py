def two_sum(nums, target):
    for num_index,num in enumerate(nums):
        val = target - num
        try:
            val_index = nums.index(val, num_index + 1)
            return [num_index,val_index]
        except ValueError:
            continue

print(two_sum(nums = [3,3], target = 6))
