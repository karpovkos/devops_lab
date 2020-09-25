def check_leap(input_year):
    if input_year % 4 == 0 and input_year % 100 != 0 and input_year % 400 == 0:
        return True
    return False


year_to_check = int(input())
print(check_leap(year_to_check))
