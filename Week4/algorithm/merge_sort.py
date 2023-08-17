def merge_sort(arr: list) -> list:

    if len(arr) < 2:
        return arr
     
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]

    left = merge_sort(left)
    right: list = merge_sort(right)

    ### merge
    arr = []
    while (len(left) > 0) and (len(right) > 0):
        if(left[0] < right[0]):
            arr.append(left.pop(0))
        else:
            arr.append(right.pop(0))
    arr.extend(left)
    arr.extend(right)

    return arr


sample_arr = [3, 4, 12, 1, 27, 2, 18]
print(merge_sort(sample_arr))