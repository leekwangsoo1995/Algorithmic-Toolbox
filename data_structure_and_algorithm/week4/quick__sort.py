def binary_search(keys,query):
    length = len(keys)
    left = 0
    right = length - 1
    while left <= right:
        mid_index: int = (left + right) // 2
        mid_value: int = keys[mid_index]

        if query < mid_value:
            right = mid_index - 1
            continue
        if query > mid_value:
            left = mid_index + 1
            continue

        return str(mid_index)

    return "-1"



n = int(input())
num_list = []
num_list.append(list(map(int,input().split())))
num_list[0].sort()
#print(num_list[0])
data = ""
for i in range(n):
    if i > 0:
        data += " "
    data += str(num_list[0][i])

print (data)
 
