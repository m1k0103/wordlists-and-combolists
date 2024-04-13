import os

to_split = "10M_wattpad.txt"

#will split the file into 3M segments

newdir = f"{to_split}_fragmented"
os.mkdir(newdir)

with open(to_split, 'r') as f: 
    count = 0 
    while True: 
        output_file = open(f'{newdir}/part{count}_{to_split}', 'w') 
        for i in range(3000000): 
            line = f.readline() 
            if not line: 
                output_file.close() 
                break 
            output_file.write(line) 
        else: 
            output_file.close() 
            count += 1 
            continue 
        break 