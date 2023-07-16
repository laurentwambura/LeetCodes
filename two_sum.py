def two_sum(nums, target):
    for num_index,num in enumerate(nums):
        val = target - num
        try:
            val_index = nums.index(val)
            return [num_index,val_index]
        except ValueError:
            continue

print(two_sum(nums = [3,2,4], target = 6))
