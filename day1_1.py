import re
dial = 50
zero_count= 0
input_list = []

test_list= [-68,-30, 48,-5,60, -55,-1,-99,14,-82]

with open("./inputs/input-day1.txt", "r") as file:
    for line in file.readlines():
        digits = int(re.findall("\d+", line)[0])
        if "L" in line:
            input_list.append((-1*digits))
        else:
            input_list.append(digits)   
# print(input_list)

for i in input_list:  
    if i < 0:
        dial += (i%(-100))
        
        if dial < 0:
            dial+=100
        else:
            dial = dial%100
            
        if dial == 0:
            zero_count += 1
    else:
        dial = (dial + (i%100))%100
        
        if dial == 0:
            zero_count += 1
    # print(dial)


print(zero_count)