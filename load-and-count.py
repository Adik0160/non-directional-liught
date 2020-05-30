#i = int(input("ile kolumn? "))
data = open("data-low.txt")
table = []
tempTuple = {}

for i in range(6):
    line = data.readline()
    tempTuple[line[0:-1]] = 0
print(tempTuple)

tempTuple

data.close()