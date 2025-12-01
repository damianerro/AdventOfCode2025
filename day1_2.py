import re
dial = 50
zero_count= 0
input_list = []
zero_clicks= 0

test_list= [-68,-30, 48,-5,60, -55,-1,-99,14,-82]

with open("input-day1-1.txt", "r") as file:
    for line in file.readlines():
        digits = int(re.findall("\d+", line)[0])
        if "L" in line:
            input_list.append((-1*digits))
        else:
            input_list.append(digits)   
# print(input_list)

for i in test_list:  
    if i < 0:
        zero_clicks += int(i/(-100))
        dial += (i%(-100))
        
        if dial < 0:
            dial+=100
            zero_clicks+=1 
        else:
            dial = dial%-100
            
        if dial == 0:
            zero_count += 1
            zero_clicks += 1
    else:
        zero_clicks += int(i/100)
        
        dial = dial + (i%100)
        
        if dial > 99:
            zero_clicks += 1
            dial = dial % 100
            # print(dial)
        if dial == 0:
            zero_count += 1
            zero_clicks += 1
            
    # print(dial)


print(zero_count)
print(zero_clicks)