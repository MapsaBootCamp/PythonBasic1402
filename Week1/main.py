print('''
                    WELCOME!

''')

# users = ["ahmad", "mammad", "kobra", "kamran", "juan", "jina"]
# username = input("lotfan username ro bezan: ")   # invoke(call)

# x = False

# if username in users:
#     age = int(input("senet ro begu: "))  # casting str to int
#     if age >= 18:
#         print("YES")
#     # elif age >= 15 and age < 18:
#     elif 15 <= age < 18:
#         print("nesfe nime YES")
#     else:
#         print("NO")

# Alireza
# flag = False
# for user in users:  # پیمایش روی ایتربل ها irerables
#     if user == username:  # indentation ====> بتوانیم بلاک برای فور. ایف و توابع و کلاس تعریف کنیم
#         flag = True
#         break  # break ===> mipare birun, continue ===> edame mide

# if flag:
#     print("YES")
# else:
#     print("NO")

# Mahboubeh  (ru mokh!)
# for user in users:
#     if user == username:
#         print("YES")
#         break
# else:
#     print("NO")

# Sama ===> is chist? baraye check karadan barabari ===>  == or is ===> is alave bar meghdar address ra ham check mikonad
# my_list1 = ["Parsa"]
# my_list2 = ["Parsa"]
# print(my_list1 == my_list2)
# print(my_list1 is my_list2)


users = ["ahmad", "mammad", "kobra", "kamran", "juan", "jina"]


# dictionary ====> key, value
# users = {
#     "usernames": ["Kamran", "Ghasem"],
#     "ages": [23, 43],
#     "password": ["1234", "fdase"]
# }

amir = "Amir"

sample_dict = {
    2: "A",
    2.3: "Gholam",
    "name": "Ali",
    True: "B",
    # [2, 3]: "c",  # ERROR
    "name": "Reza",
    # {2, 3}: "H",  # ERROR
    # {"name": "n"}: "C" # ERROR
    (3, 2): "HARCHI",

}

print(sample_dict.get("nadare", "Default"))

for key, val in sample_dict.items():
    print("key ", key)
    print("val ", val)

# Sama Question: chejuri mitunim list ra sort konim?

products = ["lebas", "machine", "mobile",
            "aebgljewbtflewjhnfleflje", "lebas", "1Sama", "2Same"]
# products.sort()
# print(sorted(products))
# print(products.sort())

# Soal Mentor: chejuri mitunim begim be sort ke bar che asasi sort kone?
# products.sort(reverse=True)


def sort_by_len(input_str):
    return len(input_str)


# ====> anonymous function(function ye bar masraf)
# def harchi(x, y):
#     return "Salam " + x

# print((lambda x, y: "Salam " + x + " Salam " + y)("H", "Sama"))


# def sort_by_second_char(input_str):
#     return input_str[1]

# Alireza.S Q: chikar konim ke ghabeliat che characteri dynamic beshe? Mentor answer ==> higher order function ===> functioni ke function return kone(closure)


def dynamic_sort_by_second_char(char_num):
    def sort_by_second_char(input_str):
        return input_str[char_num]
    return sort_by_second_char


# har eleman list ro midahad be my_fun va khorujie function ro barmigardune ke baraye moghayese elemanha az haman khoruji estefade mikoneh!
products.sort(key=lambda x: len(x))
print(products)


# set

# products = ["lebas", "machine", "mobile", "lebas"]
# print(set(products))

# for elm in {3, 5, 2, 5, 5, 1}:
#     print(elm)

exit(0)

'''
    users ===> har element ===> (username, age, pass)
'''

users = [("Kamran", 23, "1234"), ("Ghasem", 32, "ergrg")]


# immutable, mutable
# string ===> immutable

name1 = "jina"
name2 = "jina"
print(name1 is name2)

# tuple ===> immutable

name_tuple1 = ("jina",)
name_tuple2 = ("jina",)
print(name_tuple1 is name_tuple2)

# my_tuple = (12, 32, "Amir")
# my_tuple = (43,)

# for indx, elm in enumerate(my_tuple):
#     if indx == 2:
#         print(elm)
#         elm = 54
# print(my_tuple)
