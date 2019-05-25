arr = [1,2,3,4,5]
head, *rest, tail = arr
print(head, rest, tail)


head_2, *rest_2 = arr
print(head_2, rest_2)
print("--------")



arr_1 = [1,2,0]
arr_2 = [1,2,3]
arr_3 = [1,2,3,0]
arr_4 = [1,9]

list_of_arrays = [("arr_1", arr_1), ("arr_2", arr_2), ("arr_3", arr_3), ("arr_4", arr_4)]
list_of_arrays.sort(key= lambda x: x[1])

print("list after sorting in ascending order is {}".format([x[0] for x in list_of_arrays]))

print("--------")
