#278. First Bad Version

# versions = 1,2,3,4,5

# ,6,7,8,9,10 .... n
bad = 2

left = 1
right = 5
result = 1

def isBadVersion(version):
    if version >=2:
        return True
    else:
        return False

while left <= right:
    mid = (left + right)// 2
    if isBadVersion(mid) == False:
        left = mid + 1
    else:
        right = mid -1
        result = mid

print(result)


