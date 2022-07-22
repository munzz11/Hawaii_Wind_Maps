import wget
import pickle
import time
import math
import os
import re
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

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
region = parameters['region']
#Render Res:
width = parameters['width']
height = parameters['height']

utc_timestamp = int(time.time()//3600*3600)  
request_timestamp = utc_timestamp + (int(start_time) * 86400)
hours_requested = int(num_days) * 24
url = ''    
while hours_requested > 0 :
    request_timestamp = request_timestamp + 3600
   
    url = ('https://www.pacioos.hawaii.edu/cgi-bin/get_screenshot.py?url=http%3A//www.pacioos.hawaii.edu/voyager/index.html%3Fregion%3D'+
      region+
      '%26b%3D'+
      ymin+
      '%2C'+
      xmin+
      '%2C'+
      ymax+
      '%2C'+
      xmax+
      '%26o%3Dwfore%3A2%3Akts%3Ad2s2t'+
      str(request_timestamp)+
      '%26output%3Dprint&format=png&width='+
      width+
      '&height='+
      height+
      '&wait_for_dom_id=map&crop_dom_id=map&v='+ 
      str(int(time.time()*1000)))

    readable_request = time.ctime((request_timestamp))

    print("Requesting rendered wind map for " + readable_request)
    
    path = os.path.join(os.getcwd(), re.sub(r'.', '', readable_request.replace(' ','_')[:10], count = 4))
    filename = readable_request.replace(' ','_')[4:] + '.png'
    filename = filename.replace(':','_')
    outfile = os.path.join(path,filename) 

    if not os.path.exists(path):
        os.mkdir(path)

    print('Saving to: ' + outfile)
    try:
      wget.download(url,outfile)
    except:
      print('ERROR: Could not acquire image for: ' + outfile)
    try:
      img = Image.open(outfile)
      I1 = ImageDraw.Draw(img)
      font = ImageFont.truetype('FreeMono.ttf',64)
      I1.text((100,100), readable_request, font=font, fill=(0,0,0))
      img.save(outfile)
    except:
      print('ERROR: Could not apply timestamp')

    print()
    hours_requested = hours_requested - int(interval)
    
    

