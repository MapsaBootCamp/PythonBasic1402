# from lib.csv import read_csv

# print(read_csv("iris.csv"))


# Q1 ====> given list that each element has 2 repeatation [2, 2, 3, 3, -1, -1, 12, 4, 4]


def find_single(_iterable):
    print(_iterable)
    if len(_iterable) == 1:
        return _iterable[0]
    
    nesfesh = len(_iterable) // 2
    vasati = _iterable[nesfesh]
    if vasati != _iterable[nesfesh + 1] and vasati != _iterable[nesfesh -1]:
        return vasati
    elif nesfesh % 2 != 0:
        if vasati == _iterable[nesfesh + 1]:
            return find_single(_iterable[:nesfesh])
        else:
            return find_single(_iterable[nesfesh + 1:])
    else:    
        if vasati == _iterable[nesfesh + 1]:
            return find_single(_iterable[nesfesh:])
        else:
            return find_single(_iterable[:nesfesh+1])
        
    

if __name__ == "__main__":
    print(find_single([22, 22, 31, 31, 2, 2, 3, 3, 4, 43, 43, -1, -1, 7, 7, 13, 13, 32,32, 0, 0]))

