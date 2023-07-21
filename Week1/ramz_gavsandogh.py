# ramz 4 ragham,

# '1234'  ragham sevom ===> str[2]

# functions
# def name(arguments):
#     block

def salamKardan(name, age, active=True):
    print(active)
    # return "Salam " + name
    return f"Salam {name}", age, active


# print(salamKardan("Ashkan", 23))


def getPositionDigit(num, position):
    try:
        return int(str(num)[position - 1])
    except:
        raise Exception(f"position {position} dar adad {num} vojud nadarad")


# print(getPositionDigit(324565, 7))


# for i in range(1001, 10000, 2):
#     if (int(str(i)[2]) / int(str(i)[0]) == 4) \
#             and (int(str(i)[0]) - int(str(i)[3]) == 1) \
#             and (int(str(i)[1]) - int(str(i)[0]) == 3) \
#             and (int(str(i)[1]) / int(str(i)[0]) == 2.5):
#         print(i)


for i in range(1001, 10000, 2):
    if (getPositionDigit(i, 3) / getPositionDigit(i, 1) == 4) \
            and (getPositionDigit(i, 1) - getPositionDigit(i, 4) == 1) \
            and (getPositionDigit(i, 2) - getPositionDigit(i, 1) == 3) \
            and (getPositionDigit(i, 2) / getPositionDigit(i, 1) == 2.5):
        print(i)
