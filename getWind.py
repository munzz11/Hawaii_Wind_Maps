import wget
import pickle
import time
import math
import os
import threading

def get_image(get_time):
    url = ('https://www.pacioos.hawaii.edu/cgi-bin/get_screenshot.py?url=http%3A//www.pacioos.hawaii.edu/voyager/index.html%3Fb%3D'+ 
    ymin + 
    '%2C' + 
    xmin + 
    '%2C' + 
    ymax + 
    '%2C' + 
    xmax + 
    '%26o%3Dwfore%3A2%3Amph%3Ad3s2t' + 
    str(get_time) + 
    '%26output%3Dprint&format=png&width=1920&height=1080&wait_for_dom_id=map&crop_dom_id=map&v=' + 
    str(int(time.time()*1000)))
    
    readable_request = time.ctime(get_time)
    print("Requesting rendered wind map for " + readable_request)
    
    path = os.path.join(os.getcwd(), readable_request.replace(' ','_')[:10])
    filename = readable_request.replace(' ','_')[4:] + '.png'
    outfile = os.path.join(path,filename) 

    if not os.path.exists(path):
        os.mkdir(path)

    print('Saving to: ' + outfile)

    wget.download(url,outfile)
    print()

if __name__ == "__main__":
    os.environ['TZ'] = 'US/Hawaii'      #Set timezone to HI
    time.tzset()

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
        request_timestamp = utc_timestamp
    hours_requested = int(num_days) * 24
    url = ''    
    while hours_requested > 0 :
        request_timestamp = request_timestamp + 3600
        x = threading.Thread(target=get_image, args=(request_timestamp,))
        x.start()
        hours_requested = hours_requested - 1
    
    

