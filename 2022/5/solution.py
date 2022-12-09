def calculate_top(crates):
    top = ""
    for crate in crates:
        top += crate[len(crate)-1]
    print(top.replace(']','').replace('[',''))

def transform_crates_string(crates):
    new_crates = []
    for crate in crates:
        new_crate = ""
        for i in range(len(crate)):
            if (i%4 != 0):
                new_crate += crate[i-1]
        
        new_crates.append(new_crate)    
    
    return new_crates
    

def transform_crates(crates): 
    reversed = []
    for i in range(len(crates)-1,-1,-1):
        crate = crates[i].strip().split(' ')
        reversed.append(crate)
    
    transformed = []
    n = len(reversed)
    m = len(reversed[0])
    for i in range(m):
        temp = []
        for j in range(n):
            if (reversed[j][i] != '[0]'):
                temp.append(reversed[j][i])
        transformed.append(temp)
    return transformed

input = open('input.txt', 'r')
lines = input.readlines()

crates = transform_crates_string(lines[:lines.index('\n')-1])
crates = [line.replace('    ','[0]').replace('][','] [').strip() for line in lines[:lines.index('\n')-1]]
crates_1, crates_2 = transform_crates(crates), transform_crates(crates)
tasks = lines[lines.index('\n')+1:]

for task in tasks:
    quantity, place_1, place_2 = int(task.split(' ')[1]), int(task.split(' ')[3]) - 1, int(task.split(' ')[5]) - 1
    
    # First puzzle - machine 9000
    for i in range(quantity):
        crates_1[place_2].append(crates_1[place_1].pop())
    
    # Second puzzle - machine 9001
    for i in range(quantity):
        crates_2[place_2].append(crates_2[place_1].pop())    
    
    piece1 =  crates_2[place_2][:len(crates_2[place_2])-quantity]
    piece2 =  crates_2[place_2][len(crates_2[place_2])-quantity:]
    piece2.reverse()
    sum = piece1 + piece2
    crates_2[place_2] = sum

calculate_top(crates_1)
calculate_top(crates_2)

input.close()