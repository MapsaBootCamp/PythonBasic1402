
##### Functions ===> arguments

def my_fun(ejbari, *args, name="A", **kwargs):  # packing list ===> harchi delemun mikhad argoman bedahim
    print("ejbari", ejbari)
    print("name", name)
    print("args", args, sep=",")
    print("kwargs", kwargs)

def my_fun2(ejbari1, ejbari2, name="A", age=20, soal=""):  # packing list ===> harchi delemun mikhad argoman bedahim
    print("ejbari1", ejbari1)
    print("ejbari2", ejbari2)
    print("name", name)
    print("age", age)

edris_question = {
    "soal": "kojaha khube unpack konim",
    "name": "Khojasteh",
    "age": 12
}
my_list = [1, 2]
# my_fun(1, Mehrnoush = 2, name="A")
# my_fun2(*my_list, **edris_question) # ===> my_fun(1, soal="kojaha khube unpack konim", name="Khojaste")


##### comprehension
list_comprehension = (f"{line} \n" for line in my_list if line != "Shadi")
# print(type(list_comprehension))
# for elm in list_comprehension:
#     print(elm, end=" ")



###### work with FILE

# f = open("note.txt", "r+")

# # print(f.writable())

# # print(f.write("harchi"))

# # f.writelines(["A", "S"])

# # print(f.readable())

# # print(f.read(5))
# # data = f.readline()
# # while data:
# #     print(data)
# #     data = f.readline()


# #### join vs split

# # header = "NAME, AGE, PASSWORD"
# # print(header.split(", "))
# # print(", ".join(header.split(", ")))

# my_string = "    salam    "
# # print(my_string.strip())
# name = "Ashkan1234"
# # print(name[:-1])   # Ashkan123

# # for line in f.readlines():
# #     print(line[:-1])   #### string ordable, [:-1] ===> ta yeki munde be akhar

# # TODO: rahe behtari peida konid
# def my_readline(f):
#     cursor = f.tell()
#     text_in_file = f.read()
#     arr = text_in_file.split("\n")
#     f.seek(len(arr[0]) + cursor + 1)
#     return arr[0]

# print(my_readline(f))
# print(my_readline(f))
# print(my_readline(f))
# print(f.tell())


# # f.seek(13)
# # my_readline(f)

# f.close()


# context manager

f = open("note.txt", "r+")

with open("note.txt", "r+") as f:
    print(f.read())

from collections import defaultdict


def default():
    return "DEFAULT"

my_dd = defaultdict(default)
my_dd["name"] = "ASHKAN"
print(my_dd["name"])
