import datetime

#day checker

today = datetime.datetime.today()
dayofWeek = today.weekday()


print(f"Today is {today}")

def todaysday():
    if dayofWeek == 1:
        print("Today is Tuesday")
    elif dayofWeek == 0:
        print("Today is Monday")
    elif dayofWeek == 3:
        print("Today is Wednesday")
    elif dayofWeek == 4:
        print("Today is Thursday")
    elif dayofWeek == 5:
        print("Today is Friday")
    elif dayofWeek == 6:
        print("Today is Saturday")
    elif dayofWeek == 7:
        print("Today is Sunday")

