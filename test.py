import copy
list1 = [1, [2, 3], 4]
list2 = copy.deepcopy(list1)
list3 = copy.copy(list1)
list3[1][1]='x'

print("List 1 : ",list1, "\nList 2 : ", list2, "\nList 3 : ", list3)