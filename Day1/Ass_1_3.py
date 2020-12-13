std = {
    'Devesh': 1,
    'Kunal': 2,
    'Vaibhav': 3,
    'Rohit': 4
}
c = std.copy()
print(c)

d = std.items()
print(d)

e = std.keys()
print(e)

std.pop('Kunal')
print(std)

std.clear()
print(std)