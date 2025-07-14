list1 = [1, 2, 3, 4, "Hello", 80]
list2 = [1, 2, 5, 3, "Strings", 90]

uncommon = []

#list1
for i in list1:
    if i not in list2:
        uncommon.append(i)

#list2
for j in list2:
    if j not in list1:
        uncommon.append(j)

print("Uncommon elements between the two lists:", uncommon)
