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
