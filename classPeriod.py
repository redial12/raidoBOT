import time
from datetime import datetime

from discord.utils import get


def get_minute():
    seconds = time.time()
    result = time.localtime(seconds)
    minutes = result.tm_min
    # print("tm_minute:", minutes)
    return minutes


def get_hour():
    seconds = time.time()
    result = time.localtime(seconds)
    hours = result.tm_hour
    # print("tm_hour:", hours-5)
    return hours


def get_time():
    global minute
    global hour
    minute = get_minute()
    hour = get_hour()
    # print('Hour: ' + str(hour))
    # print('Minute: ' + str(minute))

def get_day():
    global day
    day = datetime.today().weekday()


# minute = 35
# hour = 15


def period():
    get_day()
    if(day == 5 or day == 6):
        return "There is **no school** on the weekend!"
    else:
        return determine_period(hour)
# make the default into an else statement
# got rid of the switch-case
# add bold text

def determine_period(argument):
    # put pstart inside of if/elif statement
    p1start = 35
    p2start = 25
    p3start = 34
    p4start = 30
    p5start = 26
    p6start = 22
    p7start = 18
    p8start = 14
    if argument == 8:
        if minute >= p1start:
            x = 60 - minute + p2start
            cp = "The current class period is **1st**."
            p = "\nThere is **" + str(x) + "** minutes remaining until the period ends."
        else:
            x = p1start - minute
            cp = "School is starting in **" + str(x) + "** minutes."
            p = ""
    elif argument == 9:
        if minute < p2start:
            x = p2start - minute
            cp = "The current class period is **1st**."
            p = "\nThere is **" + str(x) + "** minutes remaining until the period ends."
        else:
            x = 60 - minute + p3start
            cp = "The current class period is **2nd**."
            p = "\nThere is **" + str(x) + "** minutes remaining until the period ends."
    elif argument == 10:
        if minute < p3start:
            x = p3start - minute
            cp = "The current class period is **2nd**."
            p = "\nThere is **" + str(x) + "** minutes remaining until the period ends."
        else:
            x = 60 - minute + p4start
            cp = "The current class period is **3rd**."
            p = "\nThere is **" + str(x) + "** minutes remaining until the period ends."
    elif argument == 11:
        if minute < p4start:
            x = p4start - minute
            cp = "The current class period is **3rd**."
            p = "\nThere is **" + str(x) + "** minutes remaining until the period ends."
        else:
            x = 60 - minute + p5start
            cp = "The current class period is **4th**."
            p = "\nThere is **" + str(x) + "** minutes remaining until the period ends."
    elif argument == 12:
        if minute < p5start:
            x = p5start - minute
            cp = "The current class period is **4th**."
            p = "\nThere is **" + str(x) + "** minutes remaining until the period ends."
        else:
            x = 60 - minute + p6start
            cp = "The current class period is **5th**."
            p = "\nThere is **" + str(x) + "** minutes remaining until the period ends."
    elif argument == 13:
        if minute < p6start:
            x = p6start - minute
            cp = "The current class period is **5th**."
            p = "\nThere is **" + str(x) + "** minutes remaining until the period ends."
        else:
            x = 60 - minute + p7start
            cp = "The current class period is **6th**."
            p = "\nThere is **" + str(x) + "** minutes remaining until the period ends."
    elif argument == 14:
        if minute < p7start:
            x = p7start - minute
            cp = "The current class period is **6th**."
            p = "\nThere is **" + str(x) + "** minutes remaining until the period ends."
        else:
            x = 60 - minute + p8start
            cp = "The current class period is **7th**."
            p = "\nThere is **" + str(x) + "** minutes remaining until the period ends."
    elif argument == 15:
        if minute < p8start:
            x = p8start - minute
            cp = "The current class period is **7th**."
            p = "\nThere is **" + str(x) + "** minutes remaining until the period ends."
        else:
            x = 60 - minute + 10
            cp = "The current class period is **8th**."
            p = "\nThere is **" + str(x) + "** minutes remaining until school ends."
    elif argument == 16:
        if minute < 10:
            x = 10 - minute
            cp = "The current class period is **8th**."
            p = "\nThere is **" + str(x) + "** minutes remaining until the period ends."
        else:
            x = minute - 10
            cp = "The school day recently ended **" + str(x) + "** minutes ago."
            p = ""
    else:
        cp = "**There is no school right now...**"
        p = ""
    return cp + p
