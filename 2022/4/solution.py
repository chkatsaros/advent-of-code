def transform_sections(line):
    elf_1, elf_2 = [], []
    range_1, range_2 = line[0].split('-'), line[1].split('-')
    for i in range(int(range_1[0]),int(range_1[1])+1):
        elf_1.append(i)
    
    for i in range(int(range_2[0]),int(range_2[1])+1):
        elf_2.append(i)
    
    return(elf_1, elf_2)

def is_subarray(A, B):
    i = 0; j = 0
    while (i < len(A) and j < len(B)):
        if (A[i] == B[j]):
            i += 1
            j += 1
            if (j == len(B)):
                return True
        else:
            i = i - j + 1
            j = 0
    return False

def is_overlap(A, B):
    for i in range(0, len(A)):
        if (A[i] in B): 
            return True
    
    return False

input = open('input.txt', 'r')
lines = input.readlines()

pairs_1 = 0
pairs_2 = 0

for line in lines:
    elf_1, elf_2 = transform_sections(line.strip().split(','))
    if (is_subarray(elf_1, elf_2) or is_subarray(elf_2, elf_1)):
        pairs_1 += 1
        pairs_2 += 1
    elif (is_overlap(elf_1, elf_2)):
        pairs_2 += 1
    
        
print(pairs_1)
print(pairs_2)

input.close()