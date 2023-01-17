surprise = ["Groucho", "Chico", "Harpo"]
target = surprise[-1]
target = target.lower()
target = target[::-1]
target = target.capitalize()
surprise[-1] = target
print(surprise)