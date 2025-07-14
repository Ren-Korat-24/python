data = [1, 2, 3, 4, "Hello", 1, 2, 5, 3, "Strings", 80]
i = 0
while i < len(data):
    j = i + 1
    while j < len(data):
        if data[i] == data[j]:
            print(f"Duplicate found: {data[j]}")
            data.pop(j)  # Remove duplicate
        else:
            j += 1
    i += 1

print("List after removing duplicates:", data)
