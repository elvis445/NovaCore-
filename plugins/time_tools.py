from datetime import datetime


def get_time():
    now = datetime.now()
    return "Current time is " + now.strftime("%H:%M:%S")


def get_date():
    today = datetime.now()
    return "Today's date is " + today.strftime("%Y-%m-%d")
