from typing import List



# 6785 ====> 6 * 1000, 1 * 500, 1 * 200, 1 * 50, 1 * 20, 1* 10, 1*5
poolKhoord = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000] # ===> Greedy

def find_coin_devision(poolDorosht: int,poolKhoord: List[int]):
    _poolKhoord = sorted(poolKhoord, reverse=True)
    result = {}
    for sekeh in _poolKhoord:
        tedad_sekeh = poolDorosht // sekeh
        if tedad_sekeh: 
            result[sekeh] = tedad_sekeh
        poolDorosht -= sekeh * tedad_sekeh
    return result

print(find_coin_devision(6785, poolKhoord))