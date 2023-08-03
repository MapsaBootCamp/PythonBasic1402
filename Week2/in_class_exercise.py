import math

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


print(dec_to_bin_positive(256))
print(decimal_to_bin_ravesh_bikhod(256))
print(bin(256))
