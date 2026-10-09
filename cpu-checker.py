import psutil
import time

print("----------First project----------")
#Place a while true to keep it running in the background
while true:
#To get cpu i need to use the function "psutil.cpu_percent(interval=1)"
  cpu_usage = psutil.cpu_percent(interval=1)
  print("Current CPU usage is" + cpu_usage+"%")

#For number of cpu cores i need to use the function "psutil.cpu_count()"
  Num_of_cores = psutil.cpu_count()
  print("Your cpu has "+ Num_of_cores + "cores")

#Now warning logic is needed for healthcare monitoring
  if cpu_usage > 80:
    Print("WARNING, A DANGEROUS AMOUNT OF ACTIVITY HAS BEEN DETECTED ON YOUR CPU")
