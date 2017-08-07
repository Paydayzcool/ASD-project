file = [i.strip().split() for i in open("results.txt").readlines()][1:]
#exclude 1st line because its just what the individual numbers mean
#Event No, Age Level, Gender, Event Name, Place, StuCode, Competitor_First, Competitor_Last, Team/House, Performance, Points
print('working...')

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
        #I test for longer names then split student ids and then if both happened
        if i[-2][0].isdigit() and i[-6][-2].isdigit() and i[-7].isdigit() and len(i[-9]!=1):
            array.append((float(i[-2]),i[-7],i[-5]+" "+i[-4]))
        else:
            #gets out all of the 3 space names COUGH COUGH VON ALTENSTADT COUGH COUGH
            if (not i[-6][-2].isdigit()) and len(i[-9])!=1:
                array.append((float(i[-2]),i[-8],i[-6]+" "+i[-5]+" "+i[-4]))
                       
        #if theres only one division we'll need it sorted properly
        return sorted(array)[::-1]

#And this one for all the ones you need a low score for?
def low(f):
    array = []
    for i in f:
        if i[-2][0].isdigit() and i[-6][-2].isdigit() and i[-7].isdigit() and len(i[-9]!=1):
            array.append((float(i[-2]),i[-7],i[-5]+" "+i[-4]))
        else:
            #gets out all of the 3 space names COUGH COUGH VON ALTENSTADT COUGH COUGH
            if (not i[-6][-2].isdigit()) and len(i[-9])!=1:
                array.append((float(i[-2]),i[-8],i[-6]+" "+i[-5]+" "+i[-4]))
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

    number += 1
    array = []

class student:
    def __init__(self, name, event, points):
        self.name = name
        self.events = [event]
        self.points = points
    def addEvent(self, event):
        self.events.extend(event)
    def addPoints(self, points):
        self.points+=points
    def getPoints(self):
        return(self.points)
    def getName(self):
        return(self.name)
    def getEvents(self):
        return(self.events)
#all in the same dictionary makes it easy to put in
students = {'U/13':{}, 'U/14':{}, 'U/15':{}, 'U/16':{}, 'U/17':{}, 'U/21':{}}
#element is key and value is what value it stores, also this is how to loop over a dictionary if you want the values stored as well, otherwise you just go over the keys
for element, value in results.items():
    #element is key and value is definition
    #I test if the student has been entered already
    #The dictionary has seprate age groups which contain the students which are just dictionaries with their class in it
    #value = performance,place, name for the smaller indexes
    #in the big mess of indexes element[0:4] is the age group eg U/13 which is defined in the dictionary, value is one of dictionary definitions of the ordered pooled events and element[4:] is the event name.
    if value[0][2] in students[element[0:4]].keys():
        students[element[0:4]][value[0][2]].addEvent((value[0][1],'place in',element[4:]))
        students[element[0:4]][value[0][2]].addPoints(10)
    else:
        students[element[0:4]][value[0][2]] = student(value[0][2], (value[0][1],'place in',element[4:]), 10)

    if value[1][2] in students[element[0:4]].keys():
        students[element[0:4]][value[1][2]].addEvent((value[1][1],'place in',element[4:]))
        students[element[0:4]][value[1][2]].addPoints(7)
    else:
        students[element[0:4]][value[1][2]] = student(value[1][2], (value[1][1],'place in',element[4:]), 7)
        
    if value[2][2] in students[element[0:4]].keys():
        students[element[0:4]][value[2][2]].addEvent((value[2][1],'place in',element[4:]))
        students[element[0:4]][value[2][2]].addPoints(5)
    else:
        students[element[0:4]][value[2][2]] = student(value[2][2], (value[2][1],'place in',element[4:]), 5)
        
    if value[3][2] in students[element[0:4]].keys():
        students[element[0:4]][value[3][2]].addEvent((value[3][1],'place in',element[4:]))
        students[element[0:4]][value[3][2]].addPoints(3)
    else:
        students[element[0:4]][value[3][2]] = student(value[3][2], (value[3][1],'place in',element[4:]), 3)
        
    if value[4][2] in students[element[0:4]].keys():
        students[element[0:4]][value[4][2]].addEvent((value[4][1],'place in',element[4:]))
        students[element[0:4]][value[4][2]].addPoints(1)
    else:
        students[element[0:4]][value[4][2]] = student(value[0][2], (value[4][1],'place in',element[4:]), 1)
