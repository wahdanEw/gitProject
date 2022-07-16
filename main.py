from date import Date


def main():
    date1 = Date(20, 2, 2017)
    if date1.isValid():
        print(f"{date1.__str__()} Date is valid..")
    else:
        print("Date is not valid..")

    print(f"Current date is: {date1.__str__()} and the next day date is:", date1.getNextDay().date())
    print(f"Current date is: {date1.__str__()} and the next days date is:", date1.getNextDays(10).date())

    date2 = Date(15, 2, 2017)
    if date1 < date2:
        print(f"date1: {date1} is less than date2: {date2}")
    if date1 > date2:
        print(f"date1: {date1} is greater than date2: {date2}")
    if date1 == date2:
        print(f"date1: {date1} is equal to date2: {date2}")
    if date1 != date2:
        print(f"date1: {date1} is different than date2: {date2}")

    print(f"The difference days between {date1} - {date2} is: ", date1 - date2, "days")


if __name__ == main():
    main()
