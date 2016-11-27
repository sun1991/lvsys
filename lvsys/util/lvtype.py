import json

class LvTypeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, LvType):
            return {'name': obj.name, 'value': obj.value, 'color': obj.color}
        return json.JSONEncoder.default(self, obj)


class LvType(object):
    def __init__(self, name, value, color):
        self.name = name
        self.value = value
        self.color = color

