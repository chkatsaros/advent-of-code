def rearrange_packet(packet, new_char, length):
    packet.append(new_char)
    if (len(packet) > length):
        packet = packet[1:]
    
    return packet

def has_duplicates(list):
    if len(list) == len(set(list)):
        return False
    
    return True

def find_start_index(mssg, index):
    start_of_packet = []
    for i in range(len(mssg)-1):
        if (mssg[i] in start_of_packet):
            start_of_packet = rearrange_packet(start_of_packet, mssg[i], index)
        else:
            start_of_packet = rearrange_packet(start_of_packet, mssg[i], index)
            
            if (len(start_of_packet) == index and not has_duplicates(start_of_packet)):
                return(i+1) 

input = open('input.txt', 'r')
line = input.readlines()[0]

start_of_packet = find_start_index(line, 4)
start_of_message = find_start_index(line, 14)
print('start_of_packet:', start_of_packet)
print('start_of_message:', start_of_message)

input.close()