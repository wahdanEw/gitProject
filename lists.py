lst1 = [11, 7, 5, 8, 5, 37, 11, 5]
lst2 = [22, 8, 10, 1, 11]
lst3 = [71, 3, 22, 8, 2, 14, 1]


# Question '2.a' solution:
def duplicated_element(lst):
    temp_set = set()
    setDuplicated_element = set()
    for item in lst:
        if item not in temp_set:
            temp_set.add(item)
        else:
            setDuplicated_element.add(item)
    return setDuplicated_element


def print_func(lst_res, lst_name):
    print(f"{lst_name} includes the values more than once: ", end="")
    for element in lst_res:
        print(element, end=" ")
    print("\n", end="")


lst1_res = duplicated_element(lst1)
lst2_res = duplicated_element(lst2)
lst3_res = duplicated_element(lst3)
if len(lst1_res) > 0:
    print_func(lst1_res, "lst1")
if len(lst2_res) > 0:
    print_func(lst2_res, "lst2")
if len(lst3_res) > 0:
    print_func(lst3_res, "lst3")

print("\n", end="")

# Question '2.b' solution :
intersection_lst1_lst2 = set(lst1).intersection(set(lst2))
intersection_lst1_lst3 = set(lst1).intersection(set(lst3))
intersection_lst2_lst3 = set(lst2).intersection(set(lst3))
if not len(lst1_res) > 0 and not len(lst2_res) > 0:
    if len(intersection_lst1_lst2) >= 1:
        print("the common values (of lst1 and lst2) are: ", end="")
        for item in intersection_lst1_lst2:
            print(item, end=" ")
        print("\n", end="")
    if len(intersection_lst1_lst3) >= 1:
        print("the common values (of lst1 and lst3) are: ", end="")
        for item in intersection_lst1_lst3:
            print(item, end=" ")
        print("\n", end="")
if not len(lst2_res) > 0 and not len(lst3_res) > 0:
    if len(intersection_lst2_lst3) >= 1:
        print("the common values (of lst2 and lst3) are: ", end="")
        for item in intersection_lst2_lst3:
            print(item, end=" ")

