#I will use the last project to experiment with CSV saving

import psutil
import time
import sys
#To save data to a csv file i need to import the module "csv"
import csv
#to save date and time i need to import this
from datetime import datetime
import os

print("----------Second project----------")
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#files the timestamp
filename = f"data_{timestamp}.csv"
#To start saving to a csv i need to make a csv file path
def savetime(data, folder = "output"):
  #formats the date and time
  timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
  #files the timestamp
  filename = f"data_{timestamp}.csv"
  csv_file_path = filename
  os.makedirs(folder, exist_ok=True)
  csv_file_path = os.path.join(folder, filename)
  #This line will open the csv file in write mode allowing me to save data
  with open(csv_file_path, mode = 'a', newline = '') as file:
    #line below allows me to write data to a csv file
    writer = csv.writer(file)
    writer.writerows(data)
while True:
  cpu_usage = psutil.cpu_percent(interval=1)
  print(f"Current CPU usage is {cpu_usage}%", flush = True)
  Num_of_processes = len(psutil.pids())
  print(f"number of processes is equal to: {Num_of_processes}", flush = True)
  Num_of_cores = psutil.cpu_count()
  print(f"Your cpu has {Num_of_cores} cores", flush = True)
  RAM = psutil.virtual_memory()
  print(f"The total RAM and percent is shown as: {RAM}", flush = True)
  #To cleanly create formally acceptable data submissions i formatted it in an array
  data = [
    [f"{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}"],
    [f"{cpu_usage}"],
    [f"{Num_of_processes}"],
    [f"{RAM}"]
  ]
  if cpu_usage > 80 or RAM.percent > 80:
    print("WARNING, A DANGEROUS AMOUNT OF ACTIVITY HAS BEEN DETECTED ON YOUR CPU")
  #place def savetime(data, folder = "output) to make the csv file and time saves operational
  savetime(data, folder = "output")
  sys.stdout.flush()
  time.sleep(5)
  print(f"-------------------------------", flush = True)
