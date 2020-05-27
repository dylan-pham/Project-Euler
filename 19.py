import time

t0 = time.time()
# ------------------------------

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def count_days(start_date, end_date, ref_date, target_day):
    # ref_date must be exactly 1 year before start_date
    month = start_date[0]
    day = start_date[1]
    year = start_date[2]

    end_month = end_date[0]
    end_day = end_date[1]
    end_year = end_date[2] 

    ref_year = ref_date[2] 
    ref_day_of_week = ref_date[3]
    if (ref_year % 100 == 0) & (ref_year % 400 == 0):
        ref_days_in_year = 366
    elif ref_year % 4 == 0:
        ref_days_in_year = 366
    else:
        ref_days_in_year = 365

    day_of_week = ref_day_of_week + ref_days_in_year % 7
    day_of_week = day_of_week % 7 if day_of_week > 7 else day_of_week

    day_counter = 0

    if day_of_week != 1:
        day_of_week += days_in_month[month] - day + 1
        day_of_week %= 7
        month += 1 

    while year <= end_year:
        days_in_month[2] = 29 if year % 4 == 0 else 28
        while ( (year != end_year) & (month <= 12) |
                (year == end_year) & (month <= end_month) ):
            day_of_week += days_in_month[month] % 7
            day_of_week = day_of_week % 7 if day_of_week > 7 else day_of_week
            day_counter += 1 if day_of_week == target_day else 0
            month += 1
        month = 1
        year += 1

    return day_counter

print(count_days( (1, 1, 1901), (12, 31, 2000), (1, 1, 1900, 1), 7))

# ------------------------------
t1 = time.time()
print(f"program took {(t1-t0)*1000} milliseconds")
