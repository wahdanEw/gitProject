import statistics


def split_male_female(data_set) -> dict:
    """
    data_set = {info1": {"name": "x", "gender": "male"},
                info2": {"name": "y", "gender": "female"}}
    for example: split_male_female(data_set) -> 2 Dictionaries
    :param data_set : dictionary data type
    :return: 2 sorted dictionaries, sorted by gender 'male/female'.
    """

    gender_f_dict = {}
    gender_m_dict = {}
    for dic in data_set:
        if "gender" in data_set[dic].keys():
            if "male" == data_set[dic]["gender"]:
                gender_m_dict[dic] = data_set[dic]
            if "female" == data_set[dic]["gender"]:
                gender_f_dict[dic] = data_set[dic]
    return gender_f_dict, gender_m_dict


def find_median_average(data_set) -> float:
    """
    data_set = {info1": {"name": "x", "age": 18},
                info2": {"name": "y", "age": 47},
                info3": {"name": "z", "age": 30}}
    for example: find_median_average(data_set) -> 31.67, 30
    :param data_set : dictionary data type
    :return: float numbers, average and the median of the ages in dictionary.
    """

    lst_ages = []
    for dic in data_set:
        for key in data_set[dic].keys():
            if key == "age":
                lst_ages.append(data_set[dic][key])
    return statistics.mean(lst_ages), statistics.median(lst_ages)


def print_values_above(data_set, num: int = None):
    """
    data_set = {info1": {"name": "x", "age": 18},
                info2": {"name": "y", "age": 47},
                info3": {"name": "z", "age": 30}}
    for example: print_values_above(data_set, 20) -> if age > 20, output:
                                                    info2": {"name": "y", "age": 47}
                                                    info3": {"name": "z", "age": 30}
                                                    if age == None, output:
                                                    info1": {"name": "x", "age": 18}
                                                    info2": {"name": "y", "age": 47}
                                                    info3": {"name": "z", "age": 30}
    :param data_set : dictionary data type
    :param num: integer number, default value - None
    """

    for dic in data_set:
        if num == None:
            print(data_set[dic].items())
        for key, value in data_set[dic].items():
            if isinstance(num, int) and num > 0:
                if key == "age" and value > num:
                    print(data_set[dic].items())


def main():
    data_set = {"info1": {"name": "Tal", "gender": "male", "age": 22},
                "info2": {"gender": "female", "age": 57, "ID": 17686401, "name": "Anat"},
                "info3": {"gender": "male", "age": 60, "ID": 10641111, "name": "Tomer"},
                "info4": {"gender": "male", "age": 52, "ID": 12345678, "name": "jack"}}

    gender_f_dict, gender_m_dict = split_male_female(data_set)
    print("1.Dictionary data with gender 'female' :")
    for key in gender_f_dict.keys():
        print(gender_f_dict[key])
    print(end="\n")
    print("2.Dictionary data with gender 'male':")
    for key in gender_m_dict.keys():
        print(gender_m_dict[key])
    print(end="\n")

    average_of_age, median_of_age = find_median_average(data_set)
    print(f"The average of ages is: {average_of_age:.2f}" + "\n"
          f"The median of ages is: {median_of_age}" + "\n")

    print_values_above(data_set, 25)


if __name__ == main():
    main()
