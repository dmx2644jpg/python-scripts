# Is a year a leap year?


year_input = input("What is the year you want to test please ?")
year_input = int(year_input)

if year_input %4 ==0:
    print("This is a leap year")
else:
    print("This is not a leap year")