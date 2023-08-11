def counte(_iterable):
    '''
        input: ["A", "AB", 1, True, "AB", 1, 1]
        return: { "A": 1, "AB": 2, 1: 3, True:1}

    '''
    result = {}
    for elm in _iterable:
        if isinstance(elm, bool):
            elm = str(elm)
        if elm in result:
            result[elm] += 1  # result[elm] = result[elm] + 1
        else:
            result[elm] = 1
    return result


if __name__ == "__main__":
    print(counte(["A", "AB", 1, True, "AB", 1, 1]))