#List
list=[]
for i in range(10):
    list.append(i)
print(list)

# Comprehension
print("After Comprehension:-")
list1=[i for i in range(10)]
print(list1)


#Dictionary
dict={}
for i in range(10):
    dict[i]=i+1
print(dict)

#comprehension
print("After Comprehension:-")
dict1={i:i+1 for i in range(10)}
print(dict1)
