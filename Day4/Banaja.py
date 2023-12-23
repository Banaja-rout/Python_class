num=[]
n=int(input("Enter Your limit: "))
for i in range(n):
    x=int(input("Enter your number: "))
    num.append(x)           
print(num)

st=input("Enter any of these mentioning Operation(add,sub,mul,div,fdiv): ")

if st=='add':
    sum=0
    for i in list:
        sum+=i
    print(sum)
elif st=='sub':
    sub=0
    for i in list:
        sub=i-sub
    print(sub)
if st=='mul':
    mul=1
    for i in list:
        mul*=i
    print(mul)
elif st=='div':
    div=1
    for i in list:
        div=i/div
    print(div)
elif st=='fdiv':
    fdiv=1
    for i in list:
        fdiv=i//fdiv
    print(fdiv)
else:
    print("Sorry Your Choice is not in the List!!!\nPlese Select one Opration in the list....")
