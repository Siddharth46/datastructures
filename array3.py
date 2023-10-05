max_number = int(input('input the max number'))
list1=[]
for i in range(max_number+1):
    if i%2 != 0:
        list1.append(i)

print(list1)