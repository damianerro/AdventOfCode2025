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
    start_num = int(start_str)
    end_num = int(end_str)
    
    
    for number in range(start_num,end_num):
        dict = {}
        number_str = str(number)
        least_occurrent=None
        
        for c in number_str:
            if c in dict.keys():
                
                dict[c]+= 1
            else:
                dict[c]=1
            
        print(dict)
        
        
        # si la lista tiene 1 de length: ES PATRON
        if len(list(dict.keys())) == 1:
            num_sum += number
            break
        else:
            # el digito de menor ocurrencia es la pista para saber el numero maximo de ocurrencias de patrones. 
            least_occurrent=min(dict.values())
            print(least_occurrent)
            pattern_qty=int((len(number_str)) / least_occurrent)
            regex = fr"\d{pattern_qty}"
            print(re.findall(regex,number_str))
            
                    
    
    
    
           
