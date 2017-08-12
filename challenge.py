import sys
import os.path

print("If there's no/partial results or an error occured somewhere, please comment line 51 for further details.")
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
#This one for all the ones you want a high score for
def high(f):
    array = []

    for i in f:
        #if someone is disqualified it'll be their house which wont be a digit, int in output is place
        if i[-2][0].isdigit():
            array.append((float(i[-2]),i[-7],i[-5]+" "+i[-4], i[-3]))
            
    #if theres only one division we'll need it sorted properly
    return sorted(array)[::-1]

#Thos one for all the ones you want a low score
def low(f):
    array = []
    for i in f:
        #if someone is disqualified it'll be their house which isnt an int, int in output is place
        if i[-2][0].isdigit() and i[-6][-2].isdigit():
            array.append((i[-2],i[-7],i[-5]+" "+i[-4], i[-3]))
            
    array.sort()
    return array

# LINE 51 JUST BELOW: IF ANY UNEXPECTED ERRORS OCCUR eg: PARTIAL/NO OUTPUT, COMMENT THE LINE BELOW AND RUN THE PROGRAM AGAIN FOR DEBUGGING.
sys.stderr = DevNull()

if not os.path.isfile("results.txt"):
    print("Please place a 'results.txt' file in the same folder as this program and it should work this time. ;)")
    raise AssertionError

file = [i.strip().split() for i in open("results.txt").readlines()][1:]
#Event No, Age Level, Gender, Event Name, Place, StuCode, Competitor_First, Competitor_Last, Team/House, Performance, Points  

#sorting out extra space edge cases
for line in file:
    #gets rid of relays, will be place instead of last name and any disqualifications
    if line[-4].isdigit() or not line[-2][0].isdigit():
        continue
    #tests for any longer names
    if not line[-6][-2].isdigit():
        line[-5] = line[-5] + line[-4]
        line.pop(-4)
    #should be place, if not their student id has a space in it
    if not line[-7].isdigit():
        line[-7] = line[-7]+' '+line[-6]
        line.pop(-6)

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
    
    double_ups = []
    for i in range(5):
        if value[i][1] == value[i+1][1]:
            double_ups.append(i)
    
    points = {1: 10, 2:7, 3:5, 4:3, 5:1}
    place = 1
    for i in range(5):
        if i-1 not in double_ups:
            place = i+1
            if value[i][2] in students[element[0:4]].keys():
                students[element[0:4]][value[i][2]].addEvent([value[i][1],'in',element[4:]+'.'])
                students[element[0:4]][value[i][2]].addPoints(points[place])
            else:
                students[element[0:4]][value[i][2]] = student(value[i][2], [value[i][1],'in',element[4:]], points[place], value[i][3])
        #if i-1 is in double_ups it means that it's the same place as the person before them
        else:
            if value[i][2] in students[element[0:4]].keys():
                students[element[0:4]][value[i][2]].addEvent([value[i][1],'in',element[4:]+'.'])
                students[element[0:4]][value[i][2]].addPoints(points[place])
            else:
                students[element[0:4]][value[i][2]] = student(value[i][2], [value[i][1],'in',element[4:]], points[place], value[i][3])
    
    #assigning the rest of the events that don't give points, we still need them
    for i in range(5,len(value)):
        if value[i][2] in students[element[0:4]].keys():
            students[element[0:4]][value[i][2]].addEvent([value[i][1], 'in ',element[4:]+'.'])
        else:
            students[element[0:4]][value[i][2]] = student(value[i][2], [value[i][1],'in',element[4:]], 0, value[i][3])

    #above loop won't catch people that have equal 5th
    upTo = 5
    while value[upTo][0] == value[upTo-1][0]:
        students[element[0:4]][value[upTo][2]].addEvent([value[upTo][1],'in',element[4:]+'.'])
        students[element[0:4]][value[upTo][2]].addPoints(1)
        upTo += 1
        

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

    #checks if any people got the same amount of points
    upTo = 4
    buffer = 0
    while buffer <= upTo:
        #There can be shared places
        if output[buffer][0] == output[buffer+1][0]:
            upTo += 1
        buffer += 1

    print('Age Group =', ageGroup)
    print(output[0][1],'House='+ students[ageGroup][output[0][1]].house+',', str(output[0][0]), "Points;")
    print(niceEvents(students[ageGroup][output[0][1]].events))
    #not inclusive of final element
    for i in range(1,upTo+1):
        print(output[i][1]+',', students[ageGroup][output[i][1]].house+',', output[i][0], "Points;")
            
    print(30*'=')
print(30*"=")
u13 = getTop('U/13')
u14 = getTop('U/14')
u15 = getTop('U/15')
u16 = getTop('U/16')
u17 = getTop('U/17')
u21 = getTop('U/21')
