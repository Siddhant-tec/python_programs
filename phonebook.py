n = int(input("Enter dictionary values:"))
dictionary = {}
for value in range(n):
    keys, values = input().split()
    dictionary[keys] = values
print(dictionary)


def search():
    my_list = []
    while True:
        inp = input()
        if inp == 'done':
            break
        my_list.append(inp)

    for name in my_list:
        if set(my_list).issubset(dictionary.keys()):
            print(name + '=' + dictionary[name])
        else:
            print("Not Found")


search()
