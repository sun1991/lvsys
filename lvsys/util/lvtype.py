import json

class LvTypeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, LvType):
            return {'name': obj.name, 'value': obj.value}
        return json.JSONEncoder.default(self, obj)


class LvType(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

