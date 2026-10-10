import psutil
import time
import sys

print("----------First project----------")
#Place a while true to keep it running in the background
while True:
#To get cpu usage i need to use the function "psutil.cpu_percent(interval=1)"
  cpu_usage = psutil.cpu_percent(interval=1)
  print(f"Current CPU usage is {cpu_usage}%", flush = True)
#To get number of processes occuring in the cpu use "psutil.pids()"
  Num_of_processes = len(psutil.pids())
  print(f"number of processes is equal to: {Num_of_processes}", flush = True)
#For number of cpu cores i need to use the function "psutil.cpu_count()"
  Num_of_cores = psutil.cpu_count()
  print(f"Your cpu has {Num_of_cores} cores", flush = True)
#I also need to display RAM percentage and total RAM - done by the function psutil.virtualmemory()
  RAM = psutil.virtual_memory()
  print(f"The total RAM and percent is shown as: {RAM}", flush = True)

#Now warning logic is needed for healthcare monitoring
  if cpu_usage > 80 or RAM.percent > 80:
#When it comes to individual processes RAM.percent is used for used memory percentage
    print("WARNING, A DANGEROUS AMOUNT OF ACTIVITY HAS BEEN DETECTED ON YOUR CPU")
  sys.stdout.flush()
  time.sleep(5)
  print(f"-------------------------------", flush = True)
