lst1 = ["a", "b", "c"]
lst2 = ["x", "y", "z"]

reverse_lst2 = lst2[::-1]
lst_res = [lst1[index] + reverse_lst2[index] for index in range(len(lst1))]
print(lst_res)