import datetime
import random
from lvdate import LvDate


def get_alldays(year):
    the_date = datetime.date(year, 1, 1)
    
    while True:
        yield the_date
        if the_date.month == 12 and the_date.day == 31:
            break

        the_date += datetime.timedelta(days=1)


def get_lvdates(year):
    lvdate_list = []
    for thedate in get_alldays(year):
        # only consider weekend for now
        is_holiday = 1 if thedate.weekday() in [5, 6] else 0
        lvdate = LvDate(thedate.year, thedate.month, thedate.day, 0, is_holiday, 0)
        
        if not lvdate.is_holiday:
            # set lv_type and history
            chance = random.randint(1, 100)
            if chance > 98:
                lvdate.lv_type = 1
            elif chance > 95:
                lvdate.lv_type = 2
        
            if lvdate.lv_type > 0:
                lvdate.is_history = 1

        lvdate_list.append(lvdate)

    return lvdate_list

if __name__ == '__main__':
    all_lvdates = get_lvdates()
    print(len(all_lvdates))