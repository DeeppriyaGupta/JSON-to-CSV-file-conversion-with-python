
import json
import csv


with open(r'J:\Tech Ascent\temporary\json to csv conversion with python\info.json') as f:
    data=json.load(f)

store_data=data['Student']

csv_file=open(r'J:\Tech Ascent\temporary\json to csv conversion with python\output.csv', 'w') 

write= csv.writer(csv_file)

c=0
for i in store_data:
    if c==0:
        write.writerow(i.keys())
        c+=1
    write.writerow(i.values())

csv_file.close()



