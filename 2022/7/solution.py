def is_cd(str):
    if str.strip().startswith('$'):
        return len(str[2:].split(' ')) == 2
    return False

def is_ls(str):
    if str.strip().startswith('$'):
        return len(str[2:].split(' ')) == 1
    return False

def is_dir(str):
    return str.startswith('dir')

def cd(folders, str, index, back_count):
    if (str != '..'):
        folders.append(str)
        index += 1 + back_count
        back_count = 0
    else:
        back_count += 1
        index -= 1
    return (folders, index, back_count)

def find_index(folders, str):
    return folders.index(str)
        
def ls(str):
    print(str)
    
def sum_of_folder(folder, folders, files):
    print("here")
    sum = 0
    for sth in folder:
        if (not is_dir(sth.getName())):
            sum += int(sth.getSize())
        else:
            index_of_folder = find_index(folders, sth.getName().split(' ')[1])
            sum += sum_of_folder(files[index_of_folder], folders, files)
            
    return sum
 
from File import File 
input = open('input.txt', 'r')
lines = input.readlines()

folders = []
files = []
index = -1
back_count = 0

for line in lines:
    if is_cd(line):
        folder = line.strip().split(' ')[2]
        if folder != '..':
            files.append([])
        folders, index, back_count = cd(folders, folder, index, back_count)
    elif is_ls(line): 
        continue
    # ls output 
    elif is_dir(line):
        files[index].append(File(line.strip()))
    else:
        name, size = line.strip().split(' ')[1], line.strip().split(' ')[0]
        files[index].append(File(name, size))

sums = []
for i in range(len(files)):
    sums.append(sum_of_folder(files[i], folders, files))

result = 0
count = 0
sums.reverse()
for sum in sums:
    if (sum <= 100000):
        result += sum
        if (count == 2):
            break

print(sums)    
print(result)

input.close()