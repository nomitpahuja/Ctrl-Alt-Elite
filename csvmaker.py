import csv
import re
b=[]
with open('all.csv',encoding='utf-8') as file_csv:
    csv_reader=csv.reader(file_csv)
    for line in csv_reader:
        a= line[0]
        a=re.sub("[ ?()-.,]","",a)
        b.append(str(a))

with open('comp.csv','w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f,delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(b)):
        j=str(b[i])
        writer.writerow([j,])
    
