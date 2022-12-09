input = open('input.txt', 'r')
lines = input.readlines()

calories = 0
elves = []

for line in lines:
    if line == '\n':
        elves.append(calories)
        calories = 0
    else:
        calories += int(line)
        
elves.sort(reverse=True)
print(elves[0])
print(sum(elves[0:3]))

input.close()