#Calculates the days between two dates

year1 = int(input("Enter the year for date 1: "))
month1 = int(input("Enter the month for date 1: "))
day1 = int(input("Enter the day for date 1: "))
year2 = int(input("Enter the year for date 2: "))
month2 = int(input("Enter the month for date 2: "))
day2 = int(input("Enter the day for date 2: "))

yeardate1 = int(year1 * 12 * 30) + int(month1 * 30) + int(day1)
yeardate2 = int(year2 * 12 * 30) + int(month2 * 30) + int(day2)
days = (abs(yeardate1 - yeardate2))

print(f'The difference between {month1}/{day1}/{year1} and {month2}/{day2}/{year2} is {days} days!')
