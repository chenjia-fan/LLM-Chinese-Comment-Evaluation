def valid_date(date):
    if not date:
        return False
    if date.count('-') != 2:
        return False
    parts = date.split('-')
    if len(parts) != 3:
        return False
    month_str, day_str, year_str = parts
    if not (month_str.isdigit() and day_str.isdigit() and year_str.isdigit()):
        return False
    if len(month_str) != 2 or len(day_str) != 2 or len(year_str) != 4:
        return False
    month = int(month_str)
    day = int(day_str)
    year = int(year_str)
    if month < 1 or month > 12:
        return False
    if month in (1, 3, 5, 7, 8, 10, 12):
        if day < 1 or day > 31:
            return False
    elif month in (4, 6, 9, 11):
        if day < 1 or day > 30:
            return False
    else:
        if day < 1 or day > 29:
            return False
    return True