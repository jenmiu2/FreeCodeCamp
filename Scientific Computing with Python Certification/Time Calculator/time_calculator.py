from datetime import datetime
from datetime import timedelta
import time
import calendar


def add_time(start, duration, dayOfTheWeek=""):
    # convert to date
    datetimeStart = datetime.strptime(start, '%I:%M %p')

    # convert number
    durationsplit = duration.split(":")
    hours = int(durationsplit[0])
    minutes = int(durationsplit[1])
    # sum
    addTime = datetimeStart + timedelta(hours=hours, minutes=minutes)

    # difference day
    res = addTime.day - datetimeStart.day
    new_time = addTime.strftime('%I:%M %p')
    if new_time[0] == "0":
        new_time = new_time.replace("0", "", 1)

    weekday = 0
    if len(dayOfTheWeek) > 0:
        weekday = time.strptime(dayOfTheWeek, "%A").tm_wday
        day = (res + weekday) % 7
        new_time += "{:1}{}".format(", ", calendar.day_name[day])

    if res == 1:
        new_time += "{:1}(next day)".format(" ", res)
    elif res > 1:
        new_time += "{:1}({} days later)".format(" ", res)

    return new_time