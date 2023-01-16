li = ['duck', 'gourd', 'spitz']

for string in li:
    string = string.capitalize()
    shape = "{}y M{}sface".format(string, string)
    shape = f"{string}y M{string}sface"
    print(shape)