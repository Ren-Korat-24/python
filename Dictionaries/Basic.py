thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.setdefault("model","year")
print(x)

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# x = ('key1', 'key2', 'key3')
# y = 0

# thisdict1=thisdict.get("Model")
# thisdict = dict.fromkeys(x, y)

# print(thisdict)

# for x,obj in myfamily.items():
#   print(x)
  
#   for y in obj:
#     print(y + ':', obj[y])
    
# print(myfamily["child2"]["name"])
# print(myfamily)


# mydict=thisdict.copy()
# print(mydict)

# for x in thisdict:
  # print(thisdict[x])
  # print(x)

# thisdict.clear()

# del thisdict["model"]

# thisdict.popitem()

# thisdict.pop("model")


# thisdict["Color"]="Red"

# thisdict.update({"year":2001})

# thisdict["year"]=2000
# print(thisdict)

# if "model" in thisdict:
  # print(True)

# x = thisdict.items()

# x = thisdict.values()

# x = thisdict.keys()
# print(x) #before the change
# thisdict["color"] = "white"
# print(x) 

# x = thisdict.keys()

# x=thisdict.get("model")
# x=thisdict["model"]
# print(x)

# print(type(thisdict))

# print(len(thisdict))

# print(thisdict["brand"])

# print(thisdict)