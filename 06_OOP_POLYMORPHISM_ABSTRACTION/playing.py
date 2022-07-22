def start_playing(obj):
    return obj.play()


class Guitar:
    def play(self):
        return 'Playing the guitar'


class Child:
    def play(self):
        return 'Play on the playground'


class Piano:
    def play(self):
        return 'Playing the piano'


g = Guitar()
c = Child()
p = Piano()

print(start_playing(g))
print(start_playing(c))
print(start_playing(p))
