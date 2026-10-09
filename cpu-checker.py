import psutil
import time
import sys

print("----------First project----------")
#Place a while true to keep it running in the background
while True:
#To get cpu i need to use the function "psutil.cpu_percent(interval=1)"
  cpu_usage = psutil.cpu_percent(interval=1)
  print(f"Current CPU usage is {cpu_usage}%", flush = True)

#For number of cpu cores i need to use the function "psutil.cpu_count()"
  Num_of_cores = psutil.cpu_count()
  print(f"Your cpu has {Num_of_cores} cores", flush = True)

#Now warning logic is needed for healthcare monitoring
  if cpu_usage > 0:
    print("WARNING, A DANGEROUS AMOUNT OF ACTIVITY HAS BEEN DETECTED ON YOUR CPU")
  sys.stdout.flush()
  time.sleep(5)
  print(f"-------------------------------", flush = True)
