import csv
with open('data.csv','r')as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
data=[
    ['Name','Age','Location'],
    ['Arun','23','Salem'],
    ['Pavithra','22','Chennai'],
    ['Sabitha','23','Kerala'],
    ]
With open('output.csv','w'newline='')as file:
    writer=csv.write(file)
    write.writerows(data)
    