#### map, filter, reduce, zip


# map
sample_arr = [2, 3, 6, 7, 21]


# print(list(map(lambda x: 2*x, sample_arr)))

# filter
users = ["m4apsa", "gholam12", "dragon42", "ghamardaraghrab"]
# print(*filter(lambda x: x % 2 == 0, sample_arr))

# Q1: in user array list, find users that their username consist number!

# TODO: change code to use RegEx
def is_string_include_number(_str):
    result = False
    # num_range = list(map(lambda x: str(x), range(10)))
    for _char in _str:
        # if _char in num_range:
        #     result = True
        #     break
        if _char.isdecimal():
            result = True
            break
    return result


# print(*filter(is_string_include_number, users))


# reduce
from functools import reduce

def test_reduce(x, y):
    print(x, y)
    return x + y

# print(reduce(test_reduce, [2, 4, 5, 8, 12], 0))
# print(sum([2, 4, 5, 8, 12]))

# create map using reduce
def my_map(_fun, arr):
    return reduce(lambda x, y: [*x, _fun(y)], arr, [])

# print(sample_arr)
# print(my_map(lambda x: 2 *x, sample_arr))


# create filter using reduce
def my_filter(_fun, arr):
    return reduce(lambda x, y:  [*x, y] if _fun(y) else x, arr,  [])

# print(my_filter(is_string_include_number, users))



# zip 
age = [12, 51, 14, 32]
_users = ["A", "B", "C", "D"]
active = [True, False, True]

for elm in zip(age, _users, active):
    print(elm)