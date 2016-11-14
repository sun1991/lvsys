import json

class LvDateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, LvDate):
            return {'year': obj.year, 'month': obj.month, 'day': obj.day, 
                    'lv_type': obj.lv_type, 'is_approved': obj.is_approved, 'is_holiday': obj.is_holiday}
        return json.JSONEncoder.default(self, obj)

class LvDate(object):
    def __init__(self, year, month, day, lv_type, is_holiday, is_approved):
        self.year = year
        self.month = month
        self.day = day
        self.lv_type = lv_type
        self.is_holiday = is_holiday
        self.is_approved = is_approved

    def to_string(self):
        return "m:{0} d:{1} lv:{2} apr:{3}".format(self.month, self.day, self.lv_type, self.is_approved)