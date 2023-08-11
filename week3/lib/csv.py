'''
    name,age,pass  
    "A",21,123
    "V",43,321

'''





def read_csv(path: str, sep=",", head=True):
    result = {}
    with open(path, "r") as f:
        data = f.readline().rstrip() # =>  'name,age,pass' ===> split(sep)
        if head:
            headers = data.split(sep)
            for header in headers:
                result[header] = []
        while row := f.readline().rstrip():
            row_splited = row.split(sep)
            for i, v in enumerate(headers):
                result[v].append(row_splited[i])
    return result


if __name__ == "__main__":
    print(read_csv("sample.csv"))