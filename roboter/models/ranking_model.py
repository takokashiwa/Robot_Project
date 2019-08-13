#from roboter.models import robot
import csv 

class RankingModel():
    def __init__(self, name = None, count = None):
        self.name = name 
        self.count = count 
        
    def register_csv(self): 
        with open('ranking.csv', mode='w') as csv_file:
            fieldnames = ['Name', 'Count']
            writer = csv.Dictwriter(csv_file, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerow({'Name' : self.name , 'Count' : self.count})
            
    def open_csv(self):
        with open('ranking.csv' , 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                print(row['Name'] , row['Count'])
            
        