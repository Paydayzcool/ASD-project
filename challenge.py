file = [i.strip().split() for i in open("results.txt").readlines()][1:]
#exclude 1st line because its just what the individual numbers mean
#Event No, Age Level, Gender, Event Name, Place, StuCode, Competitor_First, Competitor_Last, Team/House, Performance, Points
print('working...')
'''#Discus function. Returns a sorted list of entries
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
'''
def isDist(num):
    try:
        float(num)
        return True
    except:
        return False
#the 3rd character is a : which won't be a float, I'm removing it
def timeToFloat(time):
    time = time[0:2] + time[3:]
    return(float(time))
    

#We can just have very general functions actually, theres no difference between the high and triple jump ones so why use multiple ones? Couldn't we use this one for all of the ones that you need a high score for?
def high(f):
    array = []

    for i in f:
        #if someone is disqualified it'll be their house which wont be a digit
        if i[-2][0].isdigit():
            array.append((float(i[-2]),float(i[-1]),i[-5]+" "+i[-4]))
    #if theres only one division we'll need it sorted properly
    return sorted(array)[::-1]

#And this one for all the ones you need a low score for?
def low(f):
    array = []
    for i in f:
        #if someone is disqualified it'll be their house which isnt an int
        if i[-2][0].isdigit():
            array.append((timeToFloat(i[-2]),float(i[-1]),i[-5]+" "+i[-4]))
    array.sort()
    return array
        

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
    
    #The running events all have times like 1:00.45 note the :, it wont be a float
    if isDist(array[0][-2]):
            if age_level+event in results.keys():
                results[age_level+event].extend(high(array))
                results[age_level+event] = sorted(results[age_level+event])[::-1]
            else:
                results[age_level+event] = high(array)
                
    #not else or we'll get the relays as well... First one gets rid of 10 x 80 and second one gets rid of 4x100
    elif(array[0][4] != 'x' and event != '4x100m' and event!='Ray'):
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

class student:
    def __init__(self, name, event, points):
        name = name
        events = [event]
        points = points
    def addEvent(event):
        events.extend(event)
#all in the same dictionary makes it easy to put in
students = {'U/13':{}, 'U/14':{}, 'U/15':{}, 'U/16':{}, 'U/17':{}, 'U/21':{}}
#element is key and value is what value it stores, also this is how to loop over a dictionary if you want the values stored as well, otherwise you just go over the keys
'''for element, value in results.items():
    #The numbers after are the points the students have gotten
    #I test if the student has been entered already
    #value will be a layered array with the first person being value[0] etc. the arrays inside are[performance, place,name], Im also adding on which event because we'll need that as well
    
    #in the big mess of indexes element[0:4] is the age group eg U/13 which is defined in the dictionary, value is one of dictionary definitions of the ordered pooled events and element[4:] is the event name. Im using layered dictionaries if you're still confused
    if value[0][2] in students[element[0:4]].keys():
        students[element[0:4]].extend(value[0].append(element[4:]),10)
    else:
        students[element[0:4]][value[2]] = [value[0].append(element[4:],10)

    if value[1][2] in students[element[0:4]].keys():
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
'''
