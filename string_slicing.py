def StringSlicing():
    my_string = input("")
    str1 = []
    str2 = []
    for j in range(0, len(my_string)):
        if j % 2 == 0:
            str1.append(my_string[j])
        elif j % 2 != 0:
            str2.append(my_string[j])
    print("".join(str1), "" + "".join(str2))


inp = int(input(""))
i = 0
for i in range(0, inp):
    StringSlicing()
