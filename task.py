import os
from requests import get
import json
import csv
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Task(object):
    def __init__(self):
        self.response = get('https://labrinidis.cs.pitt.edu/cs1656/data/hours.json', verify=False) 
        self.hours = json.loads(self.response.content) 

    def part4(self):
        with open('hours.csv', 'w', newline='') as csvfile:
            fieldnames = ['name', 'day', 'time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.hours)
        

    def part5(self):
        f = open('part5.txt', 'w') 
        with open('hours.csv', 'r') as csvfile:
             content = csvfile.read()
             f.write(content)
        f.close()
        
    def part6(self):
        f = open('part6.txt', 'w') 
        with open('hours.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                f.write(str(row))
        f.close()
        

    def part7(self):
        f = open('part7.txt', 'w') 
        with open('hours.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                for cell in row:
                    f.write(str(cell))
        
        f.close()
        


if __name__ == '__main__':
    task = Task()
    task.part4()
    task.part5()
    task.part6()
    task.part7()
