num=[]
n=int(input("Enter Your limit: "))
for i in range(n):
    x=int(input("Enter your number: "))
    num.append(x)           
print(num)

st=input("Enter any of these mentioning Operation(add,sub,mul,div,fdiv): ")

def Add(value):
    sum=0
    for i in value:
        sum+=i
    return sum

def Sub(value):
    sub=0
    for i in value:
        sub=i-sub
    return sub

def Mul(value):
    mul=1
    for i in value:
        mul*=i
    return mul

def Div(value):
    div=1
    for i in value:
        div=i/div
    return div

def Fdiv(value):
    fdiv=1
    for i in value:
        fdiv=i//fdiv
    return fdiv

if st=='add':
    print("Addition: ",Add(num))
elif st=='sub':
    print("Substraction: ",Sub(num))
elif st=='mul':
    print("multiplication: ",Mul(num))
elif st=='div':
    print("Division: ",Div(num))
elif st=='fdiv':
    print("Floor Division: ",Fdiv(num))
else:
    print("Sorry Your Choice is not in the List!\nPlese Select one Opration in the list....")


    
     
       
