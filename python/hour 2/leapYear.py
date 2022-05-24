#write a program that works out whether if a given year is a leap year. a normal year has 
#365 days, leap years have 366, with an extra day in feburary. the reason why we have leap years
#is reall fascinating, this video does it more justice. 
#on every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 ** unless**
#the year is also evenly divisible by 400 


year = int(input("Which year do you want to check? "))

check4 = year % 4
check100 = year % 100
check400 = year % 400

if check4 == 0 and check100 == 0 and check400 == 0:
    print(f"{year} Is a leap year")
elif check4 == 0 and check100 != 0 and check400 == 0:
    print(f"{year} Is a leap year")

elif check4 == 0 and check100 == 0 and check400 != 0:
    print(f"{year} Is NOT a leap year")
elif check4 != 0 and check100 == 0 and check400 == 0:
    print(f"{year} Is NOT a leap year")
elif check4 != 0 and check100 == 0 and check400 != 0:
    print(f"{year} Is NOT a leap year")
elif check4 != 0 and check100 != 0 and check400 == 0:
    print(f"{year} Is NOT a leap year")
elif check4 == 0 and check100 != 0 and check400 != 0:
    print(f"{year} Is NOT a leap year")
elif check4 != 0 and check100 != 0 and check400 != 0:
    print(f"{year} Is NOT a leap year")