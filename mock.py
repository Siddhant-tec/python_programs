num = int(input(""))


def check_even():
    if num % 2 == 0:
        return 0
    else:
        return 1


if check_even() == 0 and num in range(2, 5):
    print("Not Weird")
elif check_even() == 0 and num in range(6, 20):
    print("Weird")
elif check_even() == 0 and num > 20:
    print("Not Weird")
else:
    print("Weird")
