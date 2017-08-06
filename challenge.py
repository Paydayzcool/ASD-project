file = [i.strip().split() for i in open("results.txt").readlines()][1:]
#exclude 1st line because its just what the individual numbers mean
#Event No, Age Level, Gender, Event Name, Place, StuCode, Competitor_First, Competitor_Last, Team/House, Performance, Points

#No discus function. Returns a sorted list of entries
def discus(f):
    array = []
    for j in f:
        if j[4] != "998":
            array.append([float(j[-2]),float(j[-1]),j[-5]+" "+j[-4],j[-3]])
        else:
            array.append([float(j[-1]),"DSQ",j[-4]+" "+j[-3],j[-2]])
    return sorted(array)[::-1]

#(High/Triple/Long Jump)/Shot Put function. Returns a sorted list of entries (This actually works well)
def jump_put(f):
    array = []
    for i in f:
        if i[5] != "998":
            array.append([float(i[-2]),float(i[-1]),i[-5]+" "+i[-4],i[-3]])
        else:
            array.append([float(i[-1]),"DSQ",i[-4]+" "+i[-3],i[-2]])
    return sorted(array)[::-1]

#Timed events function
def timed(f):
    array = []
    for j in f:
        if j[4] != "998":
            array.append([j[-2],float(j[-1]),j[-5]+" "+j[-4],j[-3]])
        else:
            array.append([j[-1],"DSQ",j[-4]+" "+j[-3],j[-2]])
    return sorted(array)

#Relay events function (Let's say the Ray House Run is also a relay)
def relay(f):
    array = []
    for j in f:
        if j[4] != "998":
            array.append([j[-2],float(j[-1]),j[-3]])
        else:
            array.append([j[-1],"DSQ",j[-2]])
    return sorted(array)

#Get the age group champion
def age_champion(d):
    points = [10,7,5,3,1]
    before = None
    for i in range(5):
        if d[i-1][0] == before:
            d[i].append(before[-1])
        else:
            d[i].append(points[i])
    return d

array = []
results = {}
house_points = {
    "N": 0,
    "J": 0,
    "H": 0,
    "R": 0,
    "W": 0,
    "Q": 0,
    "C": 0,
    "M": 0
    }

i = 0
number = 1
l = len(file)

while i < l:
    while i < l and int(file[i][0]) == number:
        array.append(file[i])
        i += 1
    
    #Getting the age level and event from the file.
    age_level = file[i-1][1]
    event = file[i-1][3]
    if event.lower() == "discus":
        if age_level+event in results.keys():
            results[age_level+event].extend(discus(array))
            results[age_level+event] = sorted(results[age_level+event])[::-1]
        else:
            results[age_level+event] = discus(array)
    elif event.lower() in ["high","triple","shot","long"]:
        if age_level+event in results.keys():
            results[age_level+event].extend(jump_put(array))
            results[age_level+event] = sorted(results[age_level+event])[::-1]
        else:
            results[age_level+event] = jump_put(array)
    elif event.lower() in ["80m","90m","100m","110m"] and file[i-1][4].lower() == "hurdles":
        if age_level+event+"Hurdles" in results.keys():
            results[age_level+event+"Hurdles"].extend(timed(array))
            results[age_level+event+"Hurdles"] = sorted(results[age_level+event+"Hurdles"])
        else:
            results[age_level+event+"Hurdles"] = timed(array)
    elif event.lower() in ["3000m","100m","200m","800m","400m","1500m"]:
        if age_level+event in results.keys():
            results[age_level+event].extend(timed(array))
            results[age_level+event] = sorted(results[age_level+event])
        else:
            results[age_level+event] = timed(array)
    elif event.lower() in ["10","4x100m","ray"]:
        if age_level+event in results.keys():
            results[age_level+event].extend(relay(array))
            results[age_level+event] = sorted(results[age_level+event])
        else:
            results[age_level+event] = relay(array)
            
    number += 1

    array = []

for i,j in results.items():
    #Printing out the age champions
    results[i] = age_champion(results[i])
    print("Age champion for %s: %s with performance of %s" % (i,j[0][2],j[0][0]))
    for k in range(5):
        house_points[j[k][-2]] += j[k][-1]

