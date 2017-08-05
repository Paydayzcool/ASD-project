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
    
    #Why the [::-1]?
    
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

    number += 1
    array = []

#THIS NEEDS A REMAKE TO CONSIDER AGE GROUPS
students = {}
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
        students[element[4][2]] = [element[4],1]