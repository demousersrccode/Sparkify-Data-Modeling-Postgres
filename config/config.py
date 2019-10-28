import os
from configparser import ConfigParser

config = ConfigParser()
CONFIG_DIR = os.path.abspath(os.path.join('__FILE__','../config/config.cfg'))
config.read(os.path.join(CONFIG_DIR))

def param_handler(data_path):
    lst = {}
    params = config.items(data_path)
    for param in params:
        lst[param[0]] = param[1]
    return lst['data_path']

def conn_config():
    database = {}
    if config.has_section('postgresql'):
        params = config.items('postgresql')
        for param in params:
            database[param[0]] = param[1]
    return database

def data_path(path):
    if path == 'song':
        return param_handler('song_data_path')
    if path == 'log':
        return param_handler('log_data_path')