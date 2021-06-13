class Animal:
    def __init__(self, name, sound):
        self._name = name
        self._sound = sound

    @property
    def name(self):
        return self._name

    @property
    def sound(self):
        return self._sound

    @sound.setter
    def sound(self, value):
        self._sound = value

    def bark(self):
        print(self._sound)

    def sex(self):
        print('Love')


class Lion(Animal):
    def __init__(self):
        super().__init__('Lion', 'brrr..')

    def bark(self):
        print('overriding bark')


class Bird(Animal):
    def __init__(self):
        super().__init__('Bird', 'pp..')


lion = Lion()
lion.bark()
lion.sex()
print(lion.name)
print(lion.sound, '\n')

bird = Bird()
bird.bark()
bird.sex()
print(bird.name)
print(bird.sound)
