def special_add(num1):
    if num1:
        return (num1 + 2) + special_add(num1 - 1)
    else:
        return num1 - 1


def extraordinary_add(num2):
    if num2:
        return special_add(num2) + extraordinary_add(num2 - 1)
    else:
        return -1


print(extraordinary_add(4))
