nums = [1, 3, 5, 6, 7, 9]
target = 10

# idx = [k if v == target else v > target for k, v in enumerate(nums)]

# idx = [k for k, v in enumerate(nums) if v > target ]
# print(idx)

if target in nums:
    idx = [k for k, v in enumerate(nums) if v == target]
else:
    idx = [k for k, v in enumerate(nums) if v > target]

print(idx[0])
