num=[]
n=int(input("Enter Your limit: "))
for i in range(n):
    x=int(input("Enter your number: "))
    num.append(x)           
print(num)

st=input("Enter any of these mentioning Operation(add,sub,mul,div,fdiv): ")

if st=='add':
    sum=0
    for i in num:
        sum+=i
    print(sum)
elif st=='sub':
    sub=0
    for i in num:
        sub=i-sub
    print(sub)
elif st=='mul':
    mul=1
    for i in num:
        mul*=i
    print(mul)
elif st=='div':
    div=1
    for i in num:
        div=i/div
    print(div)
elif st=='fdiv':
    fdiv=1
    for i in num:
        fdiv=i//fdiv
    print(fdiv)
else:
    print("Sorry Your Choice is not in the List!\nPlese Select one Opration in the list....")


#Using Function
def fun1(add):
    sum=0
    for i in add:
        sum+=i
    return sum

def fun2(sub):
    count=0
    for i in sub:
        count=i-count
    return count

def fun3(mul):
    count=1
    for i in mul:
        count*=i
    return count

def fun4(div):
    count=1
    for i in div:
        count=i/count
    return count

def fun5(fdiv):
    count=1
    for i in fdiv:
        count=i//count
    return count

if st=='add':
    print("Addition: ",fun1(num))
elif st=='sub':
    print("Substraction: ",fun2(num))
elif st=='mul':
    print("multiplication: ",fun3(num))
elif st=='div':
    print("Division: ",fun4(num))
elif st=='fdiv':
    print("Floore Division: ",fun5(num))
else:
    print("Sorry Your Choice is not in the List!\nPlese Select one Opration in the list....")


    
     
       

