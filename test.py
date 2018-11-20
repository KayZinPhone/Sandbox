name = input("Enter name: ")
while len(name) <= 0:
    print("Your name is blank, enter aganin: ")
    name = input("Enter name: ")

print(name[1:3])
print(name[1:3:2])
for i in range(0, len(name), 2):
    print(name[i])