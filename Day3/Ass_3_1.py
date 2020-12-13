file = open("sample.txt", 'w')

file.write("I love letsupgrade")

file.close()

file = open("sample.txt", 'a')
file.write(" My name is Devesh")
file.close()

file = open("sample.txt")
print(file.read())
file.close()