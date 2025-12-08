import re
invalid_id_count= 0
input_list = None

test_list= [-68,-30, 48,-5,60, -55,-1,-99,14,-82]

with open("./inputs/input-day2.txt", "r") as file:
    input_list = file.read().strip().split(",")
        
# print(input_list)

for item in input_list:
    start_str = item.split("-")[0]
    end_str = item.split("-")[1]
    start = int(start_str)
    end = int(end_str)
    
    
    for number in range(start,end):
        number_str = str(number)
        if len(number_str)%2 == 0:
            if number_str[0:int(len(number_str)/2)] == number_str[int(len(number_str)/2):]:
            
                invalid_id_count += number

print(invalid_id_count)
            
            
    
