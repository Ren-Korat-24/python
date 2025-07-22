l=[1,2,3,4]


try:
    print(l[6])
except:
    print("Out of Index values in list")
else:
    print("List have already with 3 indexes..")
finally:
    print("code executions..!")