print("Hello advent of code")
handle = open('.\day-01\input.txt', 'r')
current = 0 
maxEnergies = [0, 0, 0]
for line in handle:
    if(line.strip().isdecimal()):
        current = current + int(line.strip())
    else:
        minEnergy = min(current, maxEnergies[0], maxEnergies[1], maxEnergies[2])
        if(minEnergy != current):
            maxEnergies[maxEnergies.index(minEnergy)] = current
        current = 0
        
print(maxEnergies[0] + maxEnergies[1] + maxEnergies[2])

