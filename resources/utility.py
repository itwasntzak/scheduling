from datetime import timedelta


def week_list(date):
    monday = date - timedelta(days=date.weekday())
    week = [ monday ]
    for number in range(1, 7):
        week.append( monday + timedelta(days=number))
    
    return week


def week_range(date):
    monday = date - timedelta(days=date.weekday())
    sunday = monday + timedelta(days=6)

    return [monday, sunday]
