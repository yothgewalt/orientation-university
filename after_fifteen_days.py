day, month, year = [int(e) for e in input().split()]
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if year % 400 == 0:
    days_in_month[1] = 29

elif year % 100 == 0:
    pass

elif year % 4 == 0:
    days_in_month[1] = 29

else:
    pass

day += 15
if day > days_in_month[month - 1]:
    day -= days_in_month[month - 1]
    month += 1

    if month > 12:
        month = 1
        year += 1

print(f"{day}/{month}/{year}")
