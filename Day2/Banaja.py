#Nested List
print("THIS IS A NESTED LIST PROGRAM:-")
marks=[64,89,98,[9.1,6.8,7.9],90,86]
print("Marks: ",marks)
print("CGPA: ",marks[3])
print(marks[3][2])
marks[3][0]=9.4
print(marks)
print(marks[0::2],'\n')

#Nested Tuple
print("THIS IS A NESTED TUPLE PROGRAM:-")
names=('Rajesh','pankaj','Sachin','Raja',('Chinu',"Pinky",'Sonam'))
print("Names:- ",names)
print("Boys name:- ",names[0:4])
print("Girls name:- ",names[4])
print(names[4][0],'\n')

#Nested Dictionary.
print("THIS IS A NESTED DICTIONARY PROGRAM:-")
myBrothers={
    'Bro1':{
        'name':"Lilu",
        'age':42
        },
    'Bro2':{
         'name':"Tulu",
        'age':38
        },
    'Bro3':{
         'name':"Munu",
        'age':22
        }
    }
print(myBrothers)
print(myBrothers['Bro3']['name'])
myBrothers['Bro1']['name']="Bijay"
print(myBrothers['Bro1'])



