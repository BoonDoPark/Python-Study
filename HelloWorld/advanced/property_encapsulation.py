class Obj:
    def __init__(self, name: str = None):
        self.name = name


class EncapsulatedObj:
    def __init__(self, name: str = None):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


class ReadOnlyObj:
    def __init__(self, name: str = None):
        self._name = name

    @property
    def name(self):
        return self._name


if __name__ == "__main__":
    obj = Obj('obj')
    en_obj = EncapsulatedObj('capsule')
    re_obj = ReadOnlyObj('read only')

    field = obj.name
    prop = en_obj.name
    read = re_obj.name

    # access to field
    print(field)

    # access to @property
    print(prop)
    # access to @name.setter
    en_obj.name = 'capsule2'
    print(en_obj.name)

    print(read)
    # THIS IS ERROR!
    # re_obj.name = 'wrtie'
