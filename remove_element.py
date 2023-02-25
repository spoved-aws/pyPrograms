
nums = [0,1,2,2,3,0,4,2]
val = 2
count = 0
length = len(nums)
# for item in nums:
#     y = nums
#     if item == val:
#         nums.remove(item)
#         count += 1
#         print(nums)

while val in nums:
    print("yes")
    nums.remove(val)
    count += 1

print(nums,count)