import sys
import os.path

#making it non IT teacher proof and blocking out the errors. Pretty neat trick!
class DevNull:
    def write(self, msg):
        pass
    
class student:
    def __init__(self, name, event, points, house):
        self.name = name
        self.events = [event]
        self.points = points
        self.house = house
    def addEvent(self, event):
        self.events.extend(event)
    def addPoints(self, points):
        self.points+=points

def isDist(num):
    try:
        float(num)
        return True
    except:
        return False

def high(f):
    array = []

    for i in f:
        #if someone is disqualified it'll be their house which wont be a digit, int in output is place
        if i[-2][0].isdigit():
            array.append((float(i[-2]),i[-7],i[-5]+" "+i[-4], i[-3]))
            
    #if theres only one division we'll need it sorted properly
    return sorted(array)[::-1]

#And this one for all the ones you need a low score for?
def low(f):
    array = []
    for i in f:
        #if someone is disqualified it'll be their house which isnt an int, int in output is place
        if i[-2][0].isdigit() and i[-6][-2].isdigit():
            array.append((i[-2],i[-7],i[-5]+" "+i[-4], i[-3]))
            
    array.sort()
    return array

# PLEASE NOTE: IF ANY UNEXPECTED ERRORS OCCUR eg: NO OUTPUT, COMMENT THE LINE BELOW AND RUN THE PROGRAM AGAIN.
sys.stderr = DevNull()

if not os.path.isfile("results.txt"):
    print("Please place a 'results.txt' file in the same folder as this program and it should work this time. ;)")
    raise AssertionError

file = [i.strip().split() for i in open("results.txt").readlines()][1:]
#Event No, Age Level, Gender, Event Name, Place, StuCode, Competitor_First, Competitor_Last, Team/House, Performance, Points  

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
        
#all in the same dictionary makes it easy to put in
students = {'U/13':{}, 'U/14':{}, 'U/15':{}, 'U/16':{}, 'U/17':{}, 'U/21':{}}
#element is key and value is what value it stores, also this is how to loop over a dictionary if you want the values stored as well, otherwise you just go over the keys
for element, value in results.items():
    #element is key and value is definition
    #I test if the student has been entered already
    #The dictionary has seprate age groups which contain the students which are just dictionaries with their class in it
    #value = performance,place, name, house for the smaller indexes
    #in the big mess of indexes element[0:4] is the age group eg U/13 which is defined in the dictionary, value is one of dictionary definitions of the ordered pooled events and element[4:] is the event name.
    
    # Uhh, Coen, have you taken into account the fact that two or more people can earn the same points because they got the same times?
    if value[0][2] in students[element[0:4]].keys():
        students[element[0:4]][value[0][2]].addEvent([value[0][1],'in',element[4:]+'.'])
        students[element[0:4]][value[0][2]].addPoints(10)
    else:
        students[element[0:4]][value[0][2]] = student(value[0][2], [value[0][1],'in',element[4:]], 10, value[0][3])

    if value[1][2] in students[element[0:4]].keys():
        students[element[0:4]][value[1][2]].addEvent([value[1][1],'in',element[4:]+'.'])
        students[element[0:4]][value[1][2]].addPoints(7)
    else:
        students[element[0:4]][value[1][2]] = student(value[1][2], [value[1][1],'in',element[4:]], 7, value[1][3])
        
    if value[2][2] in students[element[0:4]].keys():
        students[element[0:4]][value[2][2]].addEvent([value[2][1],'in',element[4:]+'.'])
        students[element[0:4]][value[2][2]].addPoints(5)
    else:
        students[element[0:4]][value[2][2]] = student(value[2][2], [value[2][1],'in',element[4:]], 5, value[2][3])
        
    if value[3][2] in students[element[0:4]].keys():
        students[element[0:4]][value[3][2]].addEvent([value[3][1],'in',element[4:]+'.'])
        students[element[0:4]][value[3][2]].addPoints(3)
    else:
        students[element[0:4]][value[3][2]] = student(value[3][2], [value[3][1],'in',element[4:]], 3, value[3][3])
        
    if value[4][2] in students[element[0:4]].keys():
        students[element[0:4]][value[4][2]].addEvent([value[4][1],'in',element[4:]+'.'])
        students[element[0:4]][value[4][2]].addPoints(1)
    else:
        students[element[0:4]][value[4][2]] = student(value[4][2], [value[4][1],'in',element[4:]], 1, value[4][3])
    #assigning the rest of the events that don't give points, we still need them
    for i in range(5,len(value)):
        if value[i][2] in students[element[0:4]].keys():
            students[element[0:4]][value[i][2]].addEvent([value[i][1], 'in ',element[4:]+'.'])
        else:
            students[element[0:4]][value[i][2]] = student(value[i][2], [value[i][1],'in',element[4:]], 0, value[i][3])

def niceEvents(events):
    output = events[0][0]+' '+events[0][1]+' '+events[0][2]+'.'
    for i in range(1,len(events)):
        output = output+' '+events[i]
    return output
    
def getTop(ageGroup):
    output = []
    for name, data in students[ageGroup].items():
        output.append([data.points, data.name])
    output.sort()
    #sort puts it into an ascending order
    output = output[::-1]
    print('Age Group =', ageGroup)
    print(output[0][1],'House='+ students[ageGroup][output[0][1]].house+',', str(output[0][0]), "Points")
    print(niceEvents(students[ageGroup][output[0][1]].events))
    #not inclusive of final element
    for i in range(1,5):
        print(output[i][1]+',', students[ageGroup][output[i][1]].house+',', output[i][0], "Points")
        
    print(30*'=')
print(30*"=")
u13 = getTop('U/13')
u14 = getTop('U/14')
u15 = getTop('U/15')
u16 = getTop('U/16')
u17 = getTop('U/17')
u21 = getTop('U/21')
