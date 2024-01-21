names=['riya','ankita','rajesh','abhi','sonam','priya']
marks = [85,57,70,84,69,98]

for index,(name,mark) in enumerate(zip(names,marks)):
    if mark > 70:
        print(index,name,mark)
