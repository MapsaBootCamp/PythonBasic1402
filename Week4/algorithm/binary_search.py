def binary_search_recursive(arr: list,searchItem, min=0, max=None):
    if max == None:
        max = len(arr) - 1
    mid = (min + max) // 2

    if min > max:
        return -1
    if searchItem == arr[mid]:
        return mid
    elif searchItem > arr[mid]:
        return binary_search_recursive(arr, searchItem, min = mid + 1, max = max)
    else:
        return binary_search_recursive(arr, searchItem, min=min, max=mid - 1)
     
def binary_search_iterative(arr, searchItem):
    min = 0
    max = len(arr) - 1

    while min <= max:
        mid = (max + min) // 2
        if searchItem == arr[mid]:
            return mid
        elif searchItem > arr[mid]:
            min = mid + 1
        else: 
            max = mid - 1
    return -1


sample_arr = [3, 4, 12, 28, 42, 61, 73]
search_item= 103
print("search_item", search_item)
print(binary_search_recursive(sample_arr, search_item))
print(binary_search_iterative(sample_arr, search_item))