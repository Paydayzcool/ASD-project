file = [i.strip().split() for i in open("results.txt").readlines()][1:]
#exclude 1st line because its just what the individual numbers mean
#Event No, Age Level, Gender, Event Name, Place, StuCode, Competitor_First, Competitor_Last, Team/House, Performance, Points

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

discus_U13 = []
for j in range(16):
    if len(file[j]) == 11:
        discus_U13.append((float(file[j][-2]),float(file[j][-1]),file[j][-5]+" "+file[j][-4]))
    else:
        discus_U13.append((float(file[j][-1]),"DSQ",file[j][-4]+" "+file[j][-3]))

discus_U13 = sorted(discus_U13)[::-1]

#U/14 Discus (Normal length is 11. Disqualified lines should be length 10 and should be missing the points part.)

discus_U14 = []
for j in range(15,32):
    if len(file[j]) == 11:
        discus_U14.append((float(file[j][-2]),float(file[j][-1]),file[j][-5]+" "+file[j][-4]))
    else:
        discus_U14.append((float(file[j][-1]),"DSQ",file[j][-4]+" "+file[j][-3]))

discus_U14 = sorted(discus_U14)[::-1]

#U/13 High Jump

high_U13 = []
for j in range(32,49):
    high_U13.append((float(file[j][-2]),float(file[j][-1]),file[j][-5]+" "+file[j][-4]))

high_U13 = sorted(high_U13)[::-1]


#U/
