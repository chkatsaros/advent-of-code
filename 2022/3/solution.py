def search_same_type(first_compartment, second_compartment):
    for item in first_compartment:
        if item in second_compartment:
            return item
    
def calculate_prio(item):
    if (item.isupper()):
        return ord(item) - 38
    else:
        return ord(item) - 96
    
input = open('test.txt', 'r')
lines = input.readlines()

prios = []

for line in lines:
    first_compartment, second_compartment = line[:len(line)//2], line[len(line)//2:]
    type = search_same_type(first_compartment, second_compartment)
    prios.append(calculate_prio(type))
    
print(sum(prios))

input.close()