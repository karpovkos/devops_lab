def remove_duplicates(list1, list2):
    final_list = []
    for num in list1:
        if (num in list2) and (num not in final_list):
            final_list.append(num)
    final_list.sort()
    return final_list


list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))
print(remove_duplicates(list_1, list_2))
