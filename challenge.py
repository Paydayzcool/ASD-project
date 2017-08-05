#We can just have very general functions actually, theres no difference between the high and triple jump ones so why use multiple ones? Couldn't we use this one for all of the ones that you need a high score for?
def high(f):
    array = []
    for i in f:
        #if someone is disqualified it'll be their house which isnt an int
        if isinstance(int, i[-2]):
            array.append((float(i[-2]),float(i[-1]),i[-5]+" "+i[-4]))
    return sorted(array)

#And this one for all the ones you need a low score for?
def low(f):
    array = []
    for i in f:
        #if someone is disqualified it'll be their house which isnt an int
        if isinstance(int, i[-2]):
            array.append((float(i[-2]),float(i[-1]),i[-5]+" "+i[-4]))
    return array.sort()
        

array = []
results = {}

#THIS NEEDS A REMAKE TO CONSIDER AGE GROUPS
# I'm not sure what this part of the program is meant to do.
"""students = {}
for element in results:
    #the numbers after are the points the students have gotten
    if element[0][2] in students.keys():
        students.extend(element[0], 10)
    else:
        students[element[0][2]] = [element[0],10]

    if element[1][2] in students.keys():
        students.extend(element[1], 10)
    else:
        students[element[1][2]] = [element[1],7]
        
    if element[2][2] in students.keys():
        students.extend(element[2], 10)
    else:
        students[element[2][2]] = [element[2],5]
        
    if element[3][2] in students.keys():
        students.extend(element[3], 10)
    else:
        students[element[3][2]] = [element[3],3]
        
    if element[4][2] in students.keys():
        students.extend(element[4], 10)
    else:
        students[element[4][2]] = [element[4],1]"""
       
file = [i.strip().split() for i in open("results.txt").readlines()][1:]
#exclude 1st line because its just what the individual numbers mean
#Event No, Age Level, Gender, Event Name, Place, StuCode, Competitor_First, Competitor_Last, Team/House, Performance, Points

#No space events function. Returns a sorted list of entries
def discus(f):
    array = []
    for j in f:
        if j[4] != "998":
            array.append((float(j[-2]),float(j[-1]),j[-5]+" "+j[-4],j[-3]))
        else:
            array.append((float(j[-1]),"DSQ",j[-4]+" "+j[-3],j[-2]))
    return sorted(array)[::-1]

#(High/Triple/Long Jump)/Shot Put function. Returns a sorted list of entries (This actually works well)
def jump_put(f):
    array = []
    for i in f:
        if i[5] != "998":
            array.append((float(i[-2]),float(i[-1]),i[-5]+" "+i[-4],i[-3]))
        else:
            array.append((float(i[-1]),"DSQ",i[-4]+" "+i[-3],i[-2]))
    return sorted(array)[::-1]

#Timed events function
def timed(f):
    array = []
    for j in f:
        if j[4] != "998":
            array.append((j[-2],float(j[-1]),j[-5]+" "+j[-4],j[-3]))
        else:
            array.append((j[-1],"DSQ",j[-4]+" "+j[-3],j[-2]))
    return sorted(array)
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
    elif event.lower() == "3000m":
        if age_level+event in results.keys():
            results[age_level+event].extend(timed(array))
            results[age_level+event] = sorted(results[age_level+event])
        else:
            results[age_level+event] = timed(array)
    number += 1

    array = []

# This part here just prints the 3000m run times to make sure there are 16 entries.
for i,j in results.items():
    if "3000m" in i:
        print(i)
        [print(k) for k in j]
        print("")

