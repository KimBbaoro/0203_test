class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(self.name)
        print(self.symbol)
        print(self.number)


#element = Element("Hydrogen","H",1)

el_dict = {'name':"Hydrogen", "symbol" : "H", "number" : 1}
hydrogen = Element(el_dict['name'],el_dict['symbol'],el_dict['number'])

hydrogen.dump()



