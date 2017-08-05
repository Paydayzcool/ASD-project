file = [i.strip().split() for i in open("results.txt").readlines()][1:]
#exclude 1st line because its just what the individual numbers mean
#Event No, Age Level, Gender, Event Name, Place, StuCode, Competitor_First, Competitor_Last, Team/House, Performance, Points

#Discus function. Returns a sorted list of entries
def discus(f):
    array = []
    for j in f:
        # NOTE: Some discus entry lengths are larger than 11 because of the Student Codes - They can have spaces.
        # Callum why does that matter with the way that you're doing it? Also we can just ignore any disqualified students, they wont be getting any points.
        if len(j) >= 11:
            array.append((float(j[-2]),float(j[-1]),j[-5]+" "+j[-4]))
        else:
            array.append((float(j[-1]),"DSQ",j[-4]+" "+j[-3]))
    return sorted(array)[::-1]

#High Jump function. Returns a sorted list of entries DOESN'T WORK YET
def high_jump(f):
    array = []
    for i in f:
        if len(i) >= 12:
            array.append((float(i[-2]),float(i[-1]),i[-5]+" "+i[-4]))
        else:
            array.append((float(i[-1]),"DSQ",i[-4]+" "+i[-3]))
    return sorted(array)
        
#Ok Coen, I've got Discus "Sorted"

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

i = 0
number = 1
l = len(file)

while i < l:
    while i < l and int(file[i][0]) == number:
        array.append(file[i])
        i += 1
            
    age_level = file[i-1][1]
    event = file[i-1][3]
    #there can be 100m sprint and hurdles
    if file[i-1][4] == "Hurdles":
        event = event + " Hurdles"
    
    #Imma use the high and low functions but Ill keep yours
    if event.lower() == "discus" or "high" or "triple" or "shot" or "discuss":
            if age_level+event in results.keys():
                results[age_level+event].extend(high(array))
                results[age_level+event] = sorted(results[age_level+event])[::-1]
            else:
                results[age_level+event] = high(array)
                
        #not else or we'll get the relays as well...
        elif event.lower() != 10 and 4 and "ray":
            if age_level+event in results.keys():
                results[age_level+event].extend(low(array))
                results[age_level+event] = sorted(results[age_level+event])
            else:
                results[age_level+event] = low(array)
        
        
    '''
    if event.lower() == "discus":
        if age_level+event in results.keys():
            results[age_level+event].extend(discus(array))
            results[age_level+event] = sorted(results[age_level+event])[::-1]
        else:
            results[age_level+event] = discus(array)
            
    elif event.lower() == "high":
        if age_level+event in results.keys():
            results[age_level+event].extend(high_jump(array))
            results[age_level+event] = sorted(results[age_level+event])[::-1]
        else:
            results[age_level+event] = high_jump(array)
            
    elif event.lower() == "triple":
        if age_level+event in results.keys():
            results[age_level+event].extend(triple_jump(array))
            results[age_level+event] = sorted(results[age_level + event])[::-1]
        else:
            results[age_level+event] = triple_jump(array)
    '''

    number += 1
    array = []

#all in the same dictionary makes it easy to put in
students = {'U/13':{}, 'U/14':{}, 'U/15':{}, 'U/16':{}, 'U/17':{}, 'U/21':{}}
#element is key and value is what value it stores, also this is how to loop over a dictionary if you want the values stored as well, otherwise you just go over the keys
for element, value in results.items():
    #The numbers after are the points the students have gotten
    #I test if the student has been entered already
    #value will be a layered array with the first person being value[0] etc. the arrays inside are[performance, place,name], Im also adding on which event because we'll need that as well
    
    #in the big mess of indexes element[0:4] is the age group eg U/13 which is defined in the dictionary, value is one of dictionary definitions of the ordered pooled events and element[4:] is the event name. Im using layered dictionaries if you're still confused
    if value[0][2] in students[element[0:4]].keys():
        students[element[0:4]].extend(value[0].append(element[4:]),10)
    else:
        students[element[0:4]][value[2]] = [value[0].append(element[4:],10])

    if value[1][2] in students.[element[0:4]]keys():
        students[element[0:4]].extend(value[1].append(element[4:],7)
    else:
        students[element[0:4]][value[1][2]] = [value[1].append(element[4:],7])
        
    if value[2][2] in students[element[0:4]].keys():
        students.extend(value[2].append(element[4:],5)
    else:
        students[element[0:4]][value[2][2]] = [value[2].append(element[4:],5])
        
    if value[3][2] in students[element[0:4]].keys():
        students[element[0:4]].extend(value[3].append(element[4:],3)
    else:
        students[element[0:4]][value[3][2]] = [value[3].append(element[4:],3])
        
    if value[4][2] in students[element[0:4]].keys():
        students[element[0:4]].extend(value[4].append(element[4:],1)
    else:
        students[element[0:4]][value[4][2]] = [value[4].append(element[4:],1])
"""VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV"""                                               
# COEN, LOOK HERE! I ONLY NEED TO TAKE CARE OF THE RELAYS NOW.
file = [i.strip().split() for i in open("results.txt").readlines()][1:]
#exclude 1st line because its just what the individual numbers mean
#Event No, Age Level, Gender, Event Name, Place, StuCode, Competitor_First, Competitor_Last, Team/House, Performance, Points

#No discus function. Returns a sorted list of entries
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

#Relay events function (Let's say the Ray House Run is also a relay)
def relay(f):
    pass

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
            
    number += 1

    array = []

for i,j in results.items():
    if "400m" in i:
        print(i)
        [print(k) for k in j]
        print("")

