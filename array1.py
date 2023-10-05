'''
    Let us say your expense for every month are listed below,
        January - 2200
        February - 2350
        March - 2600
        April - 2130
        May - 2190

Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this'''

list1 = [2200, 2350, 2600, 2130, 2190]

# sol1
extra_spend = list1[0] - list1[1] 
print(f'{extra_spend} extra dollars were spend in feb comapared to january.')

#sol2
quater_expense = list1[0] + list1[1] + list1[2]
print(f'total expense in first quater: {quater_expense}')

#sol3
list2 = []
for elem in list1:
    if elem == 2000:
        list2.append(elem)
if not list2:
    list2 = 'None'
print(f'exact 2000 dollars were spent in {list2} months')

#sol4
list1.append(1980)
print(list1)

#sol5
list1[3] = list1[3] - 200
print(list1)