a = [25, 2, 3, 57, 38, 41]
# s = ''.join(str(x) for x in a)
#
# dict = {}
#
# for item in sorted(s):
#     if item in dict:
#         dict[item] += 1
#     else:
#         dict[item] = 1
#
# print(sorted(dict[]))

s = ''.join(str(x) for x in a)
print(s)
digits = [0] * 10
print(",,,,,")
print(digits)
for item in s:
    digits[int(item)] += 1
    print(digits)
print(digits)
max_count = max(digits)

digits = [i for i in range(10) if digits[i] == max_count]
digits.sort()

print(digits)
