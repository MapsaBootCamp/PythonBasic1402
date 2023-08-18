from typing import List, Tuple
# [(2, 10), (4, 3)]  ==> [(w, v)], capacity

# density = v_i / w_i

weight_val = [(2, 8), (4, 3), (5, 2), (3, 10)]
capacity = 10


def fractional_knapsack(weight_val: List[Tuple[float, float]], capacity: float):

    sorted_weight_val = sorted(weight_val, key=lambda x: x[1] / x[0], reverse=True)

    result = {}
    optimum_val = 0

    for elm in sorted_weight_val:
        weight, val = elm
        if capacity >= weight:
            fraction = 1
            result[elm] = fraction
            capacity -= fraction * weight
            optimum_val += fraction * val
        else:
            fraction = capacity / weight
            result[elm] = fraction
            optimum_val += fraction * val
            break
    return result


print(fractional_knapsack(weight_val, capacity))