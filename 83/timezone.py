from pytz import timezone, utc

AUSTRALIA = timezone("Australia/Sydney")
SPAIN = timezone("Europe/Madrid")


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    loc_dt = utc.localize(naive_utc_dt)
    return (
        loc_dt.astimezone(AUSTRALIA),
        loc_dt.astimezone(SPAIN)
    )