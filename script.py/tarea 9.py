f = open("flag.txt", "w")
f.write("Hola")
f.close()

f = open("flag.txt", "r")
print(f.read())
f.close()
