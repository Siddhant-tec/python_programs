n = int(input(""))
dictionary = {}
my_list = []
for value in range(n):
    keys, values = input().split()
    dictionary[keys] = values

print(dictionary)

for j in range(n):
    name = str(input())
    if name in dictionary.keys():
        print(name + '=' + dictionary[name])
    else:
        print("Not found")

#############################3
n = int(input())
i = 0
book = dict()  # Declare a dictionary
while (i < n):
    name, number = input().split()  # Split input for name,number
    book[name] = number  # Append key,value pair in dictionary
    i += 1
while True:  # Run infinitely
    try:
        # Trick - If there is no more input stop the program
        query = input()
    except:
        break
    val = book.get(query, 0)  # Returns 0 is name not in dictionary
    if val != 0:
        print(query + "=" + book[query])
    else:
        print("Not found")
