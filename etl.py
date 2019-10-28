# Process file path - (song_data, log_data)
import os
import glob
import pandas as pd
import psycopg2
from config.config import data_path
from sql_queries.insert_query import *
# from migrations import retrieve

song_path = data_path('song')
log_path = data_path('log')

def process_json_path(filepath):
    """
    get all files matching .json extension from file path
    """
    all_json_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for json in files:
            all_json_files.append(os.path.abspath(json))
    return all_json_files
    

def process_song_file(filename):
    """
    process insert query for song_record, artist_record
    """
    song_list = []
    artist_list = []
    
    for everything in process_json_path(song_path):
        df = pd.read_json(everything, lines=True)
        all_songs = df[['song_id', 'title', 'artist_id', 'year', 'duration']].values.tolist()[0]
        all_artists = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']].values.tolist()[0]
        song_list.append(all_songs)
        artist_list.append(all_artists)    
        
    if filename == 'song':
        return song_list
    
    if filename == 'artist':
        return artist_list
    
    
def process_log_file(filename):
    """
    process insert query for users_record, time_record, songplay_record
    """
    user_lists = []
    time_lists = []
    songplay_lists = []
    
    for everything in process_json_path(log_path):
        df = pd.read_json(everything, lines=True)
        df = df.loc[df['page']=='NextSong']
        
        all_users = df[['userId', 'firstName', 'lastName', 'gender', 'level']].values.tolist()[0]
    
        # convert timestamp column to datetime
        t = df['ts'] = pd.to_datetime(df['ts'], unit='ms')
        # insert non-null time data records
        time_data = list((t, t.dt.hour, t.dt.day, t.dt.week, t.dt.month, t.dt.year, t.dt.weekday))
        column_labels = ('timestamp', 'hour', 'day', 'week', 'month', 'year', 'weekday')
        time_df = pd.DataFrame.from_dict(dict(zip(column_labels,time_data)))
        all_time = time_df.values.tolist()[0]

    

    # insert songplay record
        all_songplays = (pd.to_datetime(row.ts,unit='ms'),row.userId,row.level,songid,artistid,row.sessionId,row.location,row.userAgent)
        
        user_lists.append(all_users)
        time_lists.append(all_time)
        songplay_lists.append(all_songplays)
         
    if filename == 'users':
        return user_lists
        
    if filename == 'time':
        return time_lists
        
    if filename == 'songplay':
        return songplay_lists
        
    
def inject_data(table):
    """
    Sends data as lists to insert_query file
    """
    arg_songs_list = []
    arg_artists_list = []
    arg_users_list = []
    arg_songplays_list = []
    arg_time_list = []
    
    all_songs = process_song_file('song')
    all_artists = process_song_file('artist')
    
    all_users = process_log_file('users')
    all_time = process_log_file('time')
    
    song_range = list(range(0, len(all_songs)))
    user_range = list(range(0, len(all_users)))
    time_range = list(range(0, len(all_time)))
    
    for index in song_range:
        songs_data = all_songs[index]
        artists_data = all_artists[index]
        
        arg_songs_list.append(songs_data)
        arg_artists_list.append(artists_data)
        
    for index in user_range:
        users_data = all_users[index]
        time_data = all_time[index]
        
        arg_users_list.append(users_data)
        arg_time_list.append(time_data)
    
    if table == 'songs':
        return arg_songs_list
    
    if table == 'artists':
        return arg_artists_list
    
    if table == 'users':
        return arg_users_list
    
    if table == 'time':
        return arg_time_list
        
