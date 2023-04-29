import datetime as dt

abbr_month = {
    "Jan": "01",
    "Feb": "02",
    "Mar": "03",
    "Apr": "04",
    "May": "05",
    "Jun": "06",
    "Jul": "07",
    "Aug": "08",
    "Sep": "09",
    "Oct": "10",
    "Nov": "11",
    "Dec": "12"
}

d1 = dt.datetime(2021, 4, 23)
d2 = dt.datetime(2019, 12, 15)

print(d1>=d2)
