file = [i.strip().split() for i in open("results.txt").readlines()][1:]
#exclude 1st line because its just what the individual numbers mean
#Event No, Age Level, Gender, Event Name, Place, StuCode, Competitor_First, Competitor_Last, Team/House, Performance, Points

#Discus function. Returns a sorted list of entries
def discus(f):
    array = []
    for j in f:
        # NOTE: Some discus entry lengths are larger than 11 because of the Student Codes - They can have spaces.
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
        
#Ok Coen, I've got Discus "Sorted" (harhar lol)

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

    number += 1

    array = []


