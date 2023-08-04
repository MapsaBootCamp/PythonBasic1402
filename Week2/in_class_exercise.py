import math
from typing import List
# Problem 1: function(decimal_num) ==> return binary_num


def dec_to_bin_positive(decimal_num):
    if decimal_num < 0:
        raise ValueError("adad mosbat bashad")
    if decimal_num < 1:
        return decimal_num

    result = ""
    while decimal_num >= 1:
        baghimandeh = decimal_num % 2
        result = str(baghimandeh) + result
        decimal_num //= 2
    return result


def find_largest_power_2(input_num):
    max_pow = 0
    while input_num >= 2 ** (max_pow + 1):
        max_pow += 1
    return max_pow


def find_largest_power_2_behtar(input_num):
    return int(math.log2(input_num))


def decimal_to_bin_ravesh_bikhod(decimal_num):
    max_pow = find_largest_power_2(decimal_num)
    len_bin = max_pow + 1
    result = ""
    for i in range(len_bin):
        if (decimal_num >= 2 ** max_pow):
            result += "1"
            decimal_num -= 2 ** max_pow
            max_pow -= 1
        else:
            result += "0"
            max_pow -= 1
    return result


# print(dec_to_bin_positive(256))
# print(decimal_to_bin_ravesh_bikhod(256))
# print(bin(256))


# Problem 2:


str1 = "heart"
str2 = "earth"


def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)


print(is_anagram(str1, str2))


# Problem 3 ===> bubble sort

def bubble_sort(unsorted_arr: List) -> List:
    result = unsorted_arr
    for i in range(len(unsorted_arr) - 1):  # har ejra
        for j in range(len(unsorted_arr) - i - 1):  # amaliat dar har ejra
            if (unsorted_arr[j] > unsorted_arr[j+1]):
                unsorted_arr[j], unsorted_arr[j +
                                              1] = unsorted_arr[j+1], unsorted_arr[j]
    return result


unsorted_arr = [2, 12, 8, 21, 3]
print(bubble_sort(unsorted_arr))


# Problem 4 ===> factoriel


# ravesh 1

def fact_v_1(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


# ravesh 2 ===> recursive function

def fact_v_recursive(n):
    if n == 1:
        return 1
    return n * fact_v_recursive(n - 1)


print(fact_v_recursive(5))


# Problem 5 ===> factoriel

def fibo(n, cache={1: 1, 2: 1}):
    if n <= 2:
        return 1
    elif n in cache:
        return cache[n]
    else:
        cache[n] = fibo(n-1) + fibo(n-2)
        return cache[n]


# optimize ===> solution2: cache, solution1: bottom up approach
def fibo_v2(n):
    a, b = 1, 1
    for i in range(1, n):
        a, b = b, a + b
    return a


print(fibo(500))
