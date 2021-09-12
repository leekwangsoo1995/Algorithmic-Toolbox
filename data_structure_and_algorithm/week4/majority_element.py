def search(arr, left, right):
    obj = {}
    for i in arr:
        if i not in obj:
            obj[i] = 1
        else:
            obj[i] += 1
    tar = max(obj.values())
    if tar > len(arr)/2:
        return 1
    return 0



n = int(input())
num_list = []
num_list.append(list(map(int,input().split())))
i = search(num_list[0],0,n)
print(i)