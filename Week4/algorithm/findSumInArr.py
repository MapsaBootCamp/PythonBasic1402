def find_sum_in_arr(arr, searchItem):
    min = 0
    max = len(arr) - 1

    while min <= max:
        if searchItem == arr[min] + arr[max]:
            return (min, max), (arr[min], arr[max])
        elif searchItem > arr[min] + arr[max]:
            min += 1
        else: max -= 1
    return -1

sample_arr = [2, 3, 8, 21, 32, 46, 53]
searchItem = 57
print(find_sum_in_arr(sample_arr, searchItem))