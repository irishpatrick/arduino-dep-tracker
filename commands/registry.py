

class Registry:
    dict = {}

    @staticmethod
    def insert(name, obj):
        Registry.dict[name] = obj

    @staticmethod
    def get(name):
        return Registry.dict[name]

    @staticmethod
    def contains(name):
        return (name in Registry.dict.keys())
