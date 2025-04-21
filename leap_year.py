year = int(input("Enter a year: "))
print("Is leap year:", (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))