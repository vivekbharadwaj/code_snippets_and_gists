import os
from dotenv import load_dotenv, find_dotenv
# find .env automagically by walking up directories until it's found
# this is the root directory path
project_root_path = os.path.dirname(find_dotenv())
# creating a path for DATA directory
data_dir = os.path.join(project_root_path, 'DATA')

# SETTING UP LOGGING
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# create a logging format
formatter = logging.Formatter('%(asctime)s - [%(filename)s: Line %(lineno)s - %(funcName)5s() ] - %(levelname)s - %(message)s')
# create a file handler
log_filename = os.path.join(data_dir, 'logfile.txt')
fh = logging.FileHandler(log_filename)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)
# also print it to the output screen
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

def some_big_function_name_used_for_testing():
	logger.debug('This is a test message')
	return None 

some_big_function_name_used_for_testing()



'''
***Output***
2016-11-16 12:36:19,974 - [File blah.py:Line 28 - Func some_big_function_name_used_for_testing() ] - DEBUG - This is a test message
'''