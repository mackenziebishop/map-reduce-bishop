# Mackenzie Bishop
#02 Sorter

f = open("01.txt", "r")
o = open("02.txt", "w")

dataLines = f.readlines()
dataLines.sort()

for line in dataLines:
    o.write(line)

f.close()
o.close()