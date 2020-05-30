data = open("data-low.txt")
table = []
tempTuple = []
tempTuple2 = []
for i in range(6):
    tempTuple.append(data.readline()[0:-1])
table.append(tempTuple)
tempTuple*=0
for i in range(6):
    tempTuple2.append(data.readline()[0:-1])
table.append(tempTuple2)
print(table)
data.close()