import csv
import random

oc = open("occupations.csv","r").readlines()[1:-1]
oc = csv.reader(oc)
dictionary = {}


for job in oc:
    dictionary[float(job[1])] = job[0]

def jobme():
    counter = 0
    choose = random.uniform(0,99.8)
    for i in dictionary:
        counter += i
        if choose < counter:
            return dictionary[i]
        
print(jobme())

