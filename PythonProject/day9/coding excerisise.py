def is_leap_year(year):
    if year % 4 != 0:
        return "False"
    elif year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "True"
            else:
                return "False"
        else:
            return "True"
    else:
        return "Please enter a valid year"


print(is_leap_year(int(input("Enter a year to see if its a leap year!"))))

