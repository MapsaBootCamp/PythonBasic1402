from typing import Iterable, List

def create_range(_iterable: Iterable[str]) -> List[int]:
    '''
        example: 
            input: ['0-2', '3-3', '8-12']
            output: [0, 1, 2, 3, 8, 9, 10, 11, 12]
    '''
    
    result = []
    for _range in _iterable:
        range_val = _range.split("-")
        result.extend(list(range(int(range_val[0]), int(range_val[1]) + 1)))

        # for i in range(int(range_val[0]), int(range_val[1]) + 1):
        #     result.append(i)
    return result


if __name__ == "__main__":
    print(create_range(['0-2', '3-3', '8-12']))