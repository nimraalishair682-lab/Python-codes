#list

list1 = [9,5,6,3,2,8]
print(list1)

list1.append(7)
print(list1)

list1.pop(3)
print(list1)

#tuple

tuple1 = ("w" ,"d" ,"s" ,"y" ,"n")
print(tuple1)

print(type(tuple1))

#set

set1 = {9,2,7,4,5,6,8}
print(set1)
set2 = {9,8,7,6,5,4}
print(set2)

#union

set3 = set1.union(set2)
print(set3)

#intersection

set3 = set1.intersection(set2)
print(set3)

#insubset

set3 = set1.issubset(set2)
print(set3)

#isdisjoint

set3 = set1.isdisjoint(set2)
print(set3)

dict1 = {"name":"Nimra Ali shair",
         "age":21,
         "degree":"BSIT",
         "rollno":133633}
print(dict1)

#update

dict1["name"] = "Haseeba"
print(dict1)

#copy

dict2 = dict1.copy()
print(dict2)

#delete

del dict1["age"]
print(dict1)

#add new item

dict1["address"] = "lahore road"
print(dict1)

#clear dictionary

dict1.clear()
print(dict1)

#palindrom

list9 = [1,2,3,2,1]
if list9 == list9[::-1]:
    print("list is palindrom")
else:
    print("list is not palindrom")