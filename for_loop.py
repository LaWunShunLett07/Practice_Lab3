credit_card="1234-5678-9101112"
# for x in reversed(range(1,12,2)):
#     print(x)
# for x in credit_card:
#     print(x)
# for x in range(1,21):
#     if x==13:
#         break#continue
#     else:
#         print(x)
#List=[] ordered and changable, Duplicates OK
#Set ={} unordered and immutable(can't change), but Add/Remove OK. No duplicates
#Tuple=() ordered and unchagable(can't change). Duplicates OK, Faster
#dictionary = {key:value} pairs ordered and changeable. No duplicates

#fruits=['apple','orange','banana','coconut']
# fruits={'apple','orange','banana','coconut'}
# fruits.pop()#remove random element
# print(fruits)
# #print(fruits[::2])
# #print(fruits[::3])
# print(fruits.insert(0,"pineapple"))
# #print(fruits.sort())
# print(fruits)
# print(fruits.index("apple"))
# print(fruits.count("pineapple"))
# fruits=('apple','orange','banana','coconut')#tuple
# print(fruits.index("apple"))
# print(fruits.count("orange"))
# print(fruits)
# capitals={"USA": "Washintong D.C.","India":"New Dlelhi","China":"Beijing","Russia":"Moscow" }
# #print(help(capitals))
# #print(capitals.get("USA"))#Washintong D.C.
# # capitals.update({"Germany":"Berlin"})
# # capitals.pop("China")
# # print(capitals)
# # keys = capitals.keys()
# # values= capitals.values()
# # print(keys)
# # print(values)
# # for key in capitals.keys():
# #     print(key)
# items=capitals.items()
# # print(items)
# for key, value in capitals.items():
#     print(f"{key}:{value}")
import csv
file_path="C:/Repository_for_LabTest/Practice_Lab2/input.csv"
with open(file_path,'r') as file:
    dict_list=[]
    content=csv.reader(file)
    for line in content:
        print(line)
        dict_list.append(line)
    print(dict_list)