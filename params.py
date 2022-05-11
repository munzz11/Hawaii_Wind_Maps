
############################### Parameters for getWind.py ###############################

parameters = {
    'start_time': '0',                  # Not working yet leave as 0, eventually will be able to use YYYY-DD-MMThh:mm in UTC or 0 for current time
    'num_days': '5',                    # Max 6 days of forcast
    'interval': '1',                    # Interval in hours e.g, 1 = every hour, 2 = every other hour
    'ymin' : '20.501959',               # The following define the BBox for the map to render, its supposedly based on EPSG:4326 but I'm not sure thats accurate   
    'ymax' : '20.913021',
    'xmin' : '-157.155304',
    'xmax' : '-156.297684',
    'basepath' : '/home/devenv/HI_Wind_Maps_Output'
    }

#########################################################################################



import pickle

file_name = 'parameters.pickled'

with open(file_name, 'wb') as out_file:
  pickle.dump(parameters, out_file)
