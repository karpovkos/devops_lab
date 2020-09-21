def remove_duplicates(list1, list2):
    final_list = []
    duplicate = list1 + list2
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    final_list.sort()
    return final_list


# list_1 = [3, 9, 91, 102, 4, 5]
# list_2 = [29, 2, 1]

# hard way to remove duplicates in 2 lists
list_1 = [int(x) for x in input("Input numbers for list1: ").split()]
# print(list_1)
list_2 = [int(x) for x in input("Input numbers for list2: ").split()]
# print(list_2)

print(remove_duplicates(list_1, list_2))

# another way to remove duplicates
list_0 = list(set(list_1) | set(list_2))
list_0.sort()
print(list_0)
