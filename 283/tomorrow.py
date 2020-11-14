from datetime import date, timedelta


def tomorrow(today: date = None) -> date:
    if today:
        return today + timedelta(days=1)
    else:
        return date.today() + timedelta(days=1)
