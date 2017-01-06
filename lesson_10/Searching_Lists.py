values = []
values.append([1, 2, 3, 4])
values.append([5, 6, 7, 8])
values.append([9, 10, 11, 12])
values.append([13, 14, 15, 16])

print(values)
#print(values[2][3])

print("Using range...")
for i in range(0, len(values)):
    output = ""
    for j in range(0, len(values[i])):
        output += str(values[i][j]) + "\t"
    print(output, "\n")

print("Using enhanced loop...")
for value in values:
    output = ""
    for num in value:
        output += str(num) + "\t"
    print(output)


print("\nSearch the list...")
count = 0
for value in values:
    for number in value:
        count += number

print("The sum of the values in the list is equal to ", count)
        
