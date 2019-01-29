import time
import sys
import random
import json

with open('config.json') as config_file:
    data = json.load(config_file)

toolbar_width_upper = data['toolbar_width_upper']
toolbar_width_lower = data['toolbar_width_lower']
upper_speed = data['upper_speed']
lower_speed = data['lower_speed']
task_list = data['task_list']
start_message = data['start_message']
finish_message = data['finish_message']

def do_toolbar(task):
    toolbar = "["
    sys.stdout.write("\n")
    for i in range(0, toolbar_width+1):
        sys.stdout.write("\033[F")
        sys.stdout.flush()
        message = task+": "+ str(round(i*increment,2))+"%"
        sys.stdout.write(message)
        sys.stdout.write("\n")
        bar = toolbar+(toolbar_width+1-len(toolbar))*" "+"]"
        sys.stdout.write(bar)
        sys.stdout.flush()
        toolbar +=  "0"
        int = random.randint(lower_speed, upper_speed)
        time.sleep(0.001*int)
    sys.stdout.write("\n")
print("\n\n"+start_message+"\n\n")
for task in task_list:
    toolbar_width = random.randint(toolbar_width_lower, toolbar_width_upper)
    increment = 100/toolbar_width
    do_toolbar(task)
print(finish_message)
