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

        if mid_index == 0:
            return str(mid_index)

        while True:
            if keys[mid_index -1] == keys[mid_index]:
                mid_index -= 1
            else:
                return str(mid_index)

    return "-1"



n = int(input())
num_list = []
num_list.append(list(map(int,input().split())))
m = int(input())
num_list.append(list(map(int,input().split())))
#print(num_count)
data = ""
for i in range(m):
    if i > 0:
        data += " "
    data += binary_search(num_list[0],num_list[1][i])

print(data)