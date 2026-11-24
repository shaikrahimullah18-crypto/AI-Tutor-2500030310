n = int(input("Enter number of entries:"))
data = {}

for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

print(data)