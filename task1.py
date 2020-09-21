def check_leap(input_year):
    if input_year % 4 == 0:
        return True
    elif input_year % 100 == 0:
        return False
    elif input_year % 400 == 0:
        return True
    else:
        return False


year_to_check = 0
while year_to_check <= 0:
    year_to_check = int(input("Input the 'Year' : "))
    if year_to_check < 0:
        print("Wrong 'Year' input, try again")

year_checked = check_leap(year_to_check)

# if year_checked:
#     print("The Year %d is a leap year" % year_to_check)
# else:
#     print("The Year %d is NOT a leap year" % year_to_check)

print(year_checked)
