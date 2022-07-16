import datetime


class Date:
    """
    Class Date, example:    dd/mm/yy
                            __str__(self) -> str: self.dd/mm/yy
                            isValid(self) -> bool:  True/False, (self.dd/mm/yy - in/valid date)
                            getNextDay(self) -> datetime: self.dd/mm/yy, (+1 day = next date)
                            getNextDays(self, daysToAdd: int) -> datetime: self.dd/mm/yy, (int number = new date)
                            __lt__(self, other) -> bool: True/False, self.dd/mm/yy < other.dd/mm/yy
                            __gt__(self, other) -> bool: True/False, self.dd/mm/yy < other.dd/mm/yy
                            __eq__(self, other) -> bool: True/False, self.dd/mm/yy == other.dd/mm/yy
                            __ne__(self, other) -> bool: True/False, self.dd/mm/yy != other.dd/mm/yy
                            __sub__(self, other) -> int: integer number, self.dd/mm/yy - other.dd/mm/yy
    """
    def __init__(self, day: int, month: int, year: int):
        if not isinstance(year, int) or len(str(year)) != 4:
            raise TypeError("year must be integer number, and contain 4 digits..")
        if not isinstance(month, int) or month > 12 or month <= 0:
            raise TypeError("month must be integer number, between 1-12..")
        if not isinstance(day, int) or day > 31 or day <= 0:
            raise TypeError("day must be integer number, between 1-31..")

        self._year = year
        self._month = month
        self._day = day

    def __str__(self) -> str:
        """
        The __str__ method represents the class objects as a string
        :return: Instances attribute of the class as a string, dd/mm/yy.
        """
        return f"{self._year}-{self._month}-{self._day}"

    def isValid(self) -> bool:
        """
        The isValid method checking the Instances attribute of the class if it is a valid date.
        :return: True if the dd/mm/yy is valid, False if the dd/mm/yy invalid.
        """
        day, month, year = self._day, self._month, self._year

        isValidDate = True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False

        if isValidDate:
            return isValidDate
        else:
            return isValidDate

    def getNextDay(self) -> datetime:
        """
        The getNextDay method return next day date, dd/mm/yy +1(next date by adding 1 day).
        :return: datetime, dd/mm/yy + 1.
        """
        NextDay_Date = datetime.datetime(int(self._year), int(self._month), int(self._day)) + datetime.timedelta(
            days=1)
        return NextDay_Date

    def getNextDays(self, daysToAdd: int) -> datetime:
        """
        The getNextDays method return next day date, dd/mm/yy + days(next date by adding numbers of days).
        :param daysToAdd: integer number
        :return: datetime, dd/mm/yy + days.
        """
        NextDay_Date = datetime.datetime(int(self._year), int(self._month), int(self._day)) + datetime.timedelta(
            days=daysToAdd)
        return NextDay_Date

    def __lt__(self, other) -> bool:
        """
        The __lt__ method checking the instances attribute of the class if less than other attribute of the class
        :param other: class object
        :return: True if the dd/mm/yy self class date is less than other class date, False if not..
        """
        if isinstance(other, Date):
            return self._year < other._year or self._month < other._month or self._day < other._day

    def __gt__(self, other) -> bool:
        """
        The __gt__ method checking the instances attribute of the class if greater than other attribute of the class
        :param other: class object
        :return: True if the dd/mm/yy self class date is greater than other class date, False if not..
        """
        if isinstance(other, Date):
            return self._year > other._year or self._month > other._month or self._day > other._day

    def __eq__(self, other) -> bool:
        """
        The __eq__ method checking the instances attribute of the class if equal to other attribute of the class
        :param other: class object
        :return: True if the dd/mm/yy self class date is equal to other class date, False if not..
        """
        if isinstance(other, Date):
            return self._year == other._year and self._month == other._month and self._day == other._day

    def __ne__(self, other) -> bool:
        """
        The __eq__ method checking the instances attribute of the class if not equal(Different) to
        Other attribute of the class
        :param other: class object
        :return: True if the dd/mm/yy self class date is not equal to other class date, False if not..
        """
        if isinstance(other, Date):
            return self._year != other._year or self._month != other._month or self._day != other._day

    def __sub__(self, other) -> int:
        """"
        The __sub__ method (self, other) method returns a new object that represents the difference of two objects.
        It implements the subtraction operator '-' .
        :param other: class object
        :return: integer number, (dd/mm/yy self class date) - (dd/mm/yy other class date).
        """
        days = datetime.date(int(self._year), int(self._month), int(self._day)) - datetime.date(
            int(other._year), int(other._month), int(other._day))
        return days.days
