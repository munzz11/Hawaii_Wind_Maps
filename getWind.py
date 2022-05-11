import wget
import pickle
import time
import math
import os

def roundup(x):                             # For some reason the api requires a requested timestamp ending with 00
    return int((x / 100.0)) * 100

params_file = 'parameters.pickled'
parameters = pickle.load(open(params_file, 'rb')) 

start_time = parameters['start_time']
interval = parameters['interval']
num_days = parameters['num_days']
ymin = parameters['ymin']
ymax = parameters['ymax']
xmin = parameters['xmin']
xmax = parameters['xmax']

if start_time == '0':
    utc_timestamp = int(time.time()//3600*3600)  
    request_timestamp = roundup(utc_timestamp)
hours_requested = int(num_days) * 24
url = ''    
while hours_requested > 0 :
    request_timestamp = request_timestamp + 3600
    url = ('https://www.pacioos.hawaii.edu/cgi-bin/get_screenshot.py?url=http%3A//www.pacioos.hawaii.edu/voyager/index.html%3Fb%3D'+ 
        ymin + 
        '%2C' + 
        xmin + 
        '%2C' + 
        ymax + 
        '%2C' + 
        xmax + 
        '%26o%3Dwfore%3A2%3Amph%3Ad3s2t' + 
        str(request_timestamp) + 
        '%26output%3Dprint&format=png&width=1920&height=1080&wait_for_dom_id=map&crop_dom_id=map&v=' + 
        str(int(time.time()*1000)))
    
    readable_request = time.ctime((request_timestamp))
    print("Requesting rendered wind map for " + readable_request)
    
    path = os.path.join(os.getcwd(), readable_request.replace(' ','_')[:10])
    filename = readable_request.replace(' ','_')[4:] + '.png'
    outfile = os.path.join(path,filename) 

    if not os.path.exists(path):
        os.mkdir(path)
        
    print('Saving to: ' + outfile)

    wget.download(url,outfile)
    hours_requested = hours_requested - 1
    
    
