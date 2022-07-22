
############################### Parameters for getWind.py ###############################

parameters = {
    'start_time': '2',                  # Not working yet leave as 0, eventually will be able to use YYYY-DD-MMThh:mm in UTC or 0 for current time
    'num_days': '6',                    # Max 6 days of forcast
    'interval': '1',                    # Interval in hours e.g, 1 = every hour, 2 = every other hour
    'ymin' : '21.376360',               # The following define the BBox for the map to render, its supposedly based on EPSG:4326 but I'm not sure thats accurate   
    'ymax' : '22.378016',
    'xmin' : '-160.842590',
    'xmax' : '-158.936462',
    'region' : 'hi',
    'width' : '1920',
    'height':'1080'
    }

#########################################################################################



import pickle

file_name = 'parameters.pickled'

with open(file_name, 'wb') as out_file:
  pickle.dump(parameters, out_file)
