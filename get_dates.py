from datetime import timedelta, date


def generate_dates(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date.strftime("%Y-%m-%d")
        current_date += timedelta(days=1)
        

start_date = date(2023, 11, 29)
end_date = date(2023, 12, 3)
dates = list(generate_dates(start_date, end_date))

print(dates)