# Question 3 solution:
lst = [31, 99, 3, 1943]
sort_order = input("Enter sort type: asc/desc \n")

str_lst = str(lst)
set_lst = set()
for index in range(len(str_lst)):
    if str_lst[index].isnumeric():
        set_lst.add(str_lst[index])

lst_res = list(sorted(set_lst))
if sort_order == "asc":
    for index in range(len(lst_res)):
        if index == len(lst_res)-1:
            print(lst_res[index])
        else:
            print(lst_res[index] + ", ", end="")
if sort_order == "desc":
    lst_res.reverse()
    for index in range(len(lst_res)):
        if index == len(lst_res) - 1:
            print(lst_res[index])
        else:
            print(lst_res[index] + ", ", end="")
