def find_pairs(base_list, target_sum):
    base_list.sort()
    print(base_list)

    left_p = 0
    right_p = len(base_list) -1
    new_list = []
    while left_p < right_p:

        print(left_p, right_p)
        sum_value = base_list[left_p]+ base_list[right_p]
        if sum_value == target_sum:
            new_list.append((base_list[left_p], base_list[right_p]))
            right_p -= 1
            left_p += 1
        elif sum_value > target_sum:
            right_p -= 1
        elif sum_value < target_sum:
            left_p += 1
    return new_list

'''program to find all the pairs in a list that
sums up to a given number'''

base_list= [1,2,4,6,8,3,5,72,23]
target_sum = int(input('enter the target value'))
result = find_pairs(base_list, target_sum)
print(result)