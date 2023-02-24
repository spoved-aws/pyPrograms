a = [25, 2, 3, 57, 38, 41]

s = ''.join(str(x) for x in a)

#print(sorted(s))

dict = {}
for item in s:
    if item in dict:
        dict[item] += 1
    else:
        dict[item] = 1

to_calculate_max_list = []

for keys in dict:
    to_calculate_max_list.append(dict[keys])
# print(to_calculate_max_list)
# print(dict)

max_digit = max(to_calculate_max_list)
final_list = []
for keys in dict:
    if dict[keys] == max_digit:
        final_list.append(keys)

print(sorted(final_list))


