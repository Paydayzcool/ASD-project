file = [i.strip().split() for i in open("results.txt").readlines()][1:]
#exclude 1st line because its just what the individual numbers mean
#Event No, Age Level, Gender, Event Name, Place, StuCode, Competitor_First, Competitor_Last, Team/House, Performance, Points

#Discus function. Returns a sorted list of entries
def discus(start_end,f):
    array = []
    for j in range(start_end[0],start_end[1]):
        if len(f[j]) == 11:
            array.append((float(f[j][-2]),float(f[j][-1]),f[j][-5]+" "+f[j][-4]))
        else:
            array.append((float(f[j][-1]),"DSQ",f[j][-4]+" "+f[j][-3]))
    return sorted(array)[::-1]
"""events = []
for line in file:
    #get rid of relays and set place, distance and event to int/float
    if line[6] == 'Relay':
        continue
    line[0] = int(line[0])
    line[4] = int(line[4])
    line[9] = float(line[9])
    try:
        events[line[0]].append(line)
    except:
        events.append(line)
"""
# Coen, I'm going to assume that the events will appear in the same order this year. This will definetely be helpful!

#U/13 Discus (Normal length is 11. Disqualified lines should be length 10 and should be missing the points part.)

discus_U13 = discus([0,16],file)
discus_U13 = discus([16,31],file)

#U/13 High Jump

high_U13 = []
for j in range(32,49):
    high_U13.append((float(file[j][-2]),float(file[j][-1]),file[j][-5]+" "+file[j][-4]))

high_U13 = sorted(high_U13)[::-1]


#U/
