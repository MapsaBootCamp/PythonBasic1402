def find_max(inp_list):
    result = inp_list[0]
    for elm in inp_list:
        if result < elm:
            result = elm
    return result


my_list = [2, 12, -1, 21, 133, -32, 45, 83, 0, 8]
print(find_max(my_list))
