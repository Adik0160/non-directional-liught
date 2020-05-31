import csv

# file = open("private/data.txt")

openPath = input("ścieżka do pliku TXT ")
savePath = input("ścieżka do zapisania plikus CSV ")
phiw = input("wprowadź Φw ")
deltaw = input("prowadź Δw ")

data = []
cutOut = []
def to_matrix(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]
# data = file.readlines()

def time_to_sec(str):
    h, m, s = str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def cosfiu(pu, un, il): # power factor
    return pu/(un*il)

def fi(phiw, deltax, deltaw):    # lm
    return phiw*(deltax/deltaw)

def n(fi, pu):          # efficiency
    return fi/pu

with open(openPath) as f:
    for line in f:
        data.append(line.rstrip())

data = to_matrix(data, 6)

for i in range(1, len(data)):
    data[i][0] = time_to_sec(data[i][0])                # time
    data[i][1] = float(data[i][1].replace(',', '.'))    # U
    data[i][2] = float(data[i][2].replace(',', '.'))    # I
    data[i][3] = float(data[i][3].replace(',', '.'))    # P
    data[i][4] = float(data[i][4].replace(',', '.'))    # lambda
    data[i][5] = float(data[i][5].replace(',', '.'))    # delta x
    data[i].append(float(cosfiu(data[i][3], data[i][1], data[i][2])))  # cosFiu
    data[i].append(float(fi(float(phiw), data[i][5], float(deltaw))))       # fi
    data[i].append(float(n(data[i][7], data[i][3])))       # efficiency

for i in range(0, int(len(data)/10)):
    cutOut.append(data[i*10])

cutOut[0].extend(['cosfiu [-]', 'fi [lm]', 'efficiency [lm/W]'])


with open(savePath, 'w', newline='') as f:
    thewriter = csv.writer(f)
    for line in cutOut:
        thewriter.writerow(line)
# todo naprawic błąd zapisu
print(cutOut)
# with open("/private/data-low.txt") as file: 