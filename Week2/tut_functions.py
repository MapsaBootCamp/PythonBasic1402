# global scope
global_scope = "AAAAA"
new_var = "Alireza Ziaei"
my_list = [3, 4]


def fun_name(positional_ag, default_arg=None):
    # local scope
    # global new_var #### kasif
    my_list.append(23)
    print(global_scope)
    new_var = "21"
    print(new_var)
    print("X")


fun_name("HARCHI")
print(new_var)
print(my_list)
