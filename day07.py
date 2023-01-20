class Bear:
    def eats(self):
        return 'Berries'

class Rabbit:
    def eats(self):
        return "Clover"

class Octothorpe:
    def eats(self):
        return 'campers'

a = Bear()
b = Rabbit()
c = Octothorpe()
print(a.eats(),b.eats(),c.eats())