# CREATE TABLES
# >>songplays, users, songs, artists, time

def createTables():
    users = ('''
        CREATE TABLE IF NOT EXISTS users(
            user_id VARCHAR(255) PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            gender TEXT,
            level TEXT 
            );
        ''')
    
    songs = ('''
        CREATE TABLE IF NOT EXISTS songs(
            song_id VARCHAR PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            artist_id VARCHAR(255) NOT NULL,
            year INTEGER NOT NULL,
            duration NUMERIC NOT NULL       
            );
        ''')
    
    artists = ('''
        CREATE TABLE IF NOT EXISTS artists( 
            artist_id VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            location VARCHAR(255) NOT NULL,
            latitude NUMERIC NOT NULL,
            longitude NUMERIC NOT NULL
            );
        ''')
    
    time = ('''
        CREATE TABLE IF NOT EXISTS time(
            start_time TIMESTAMP PRIMARY KEY,
            hour INTEGER NOT NULL,
            day INTEGER NOT NULL,
            week INTEGER NOT NULL,
            month INTEGER NOT NULL,
            year INTEGER NOT NULL,
            weekday INTEGER NOT NULL
            );
        ''')
    
    songplays = ('''
        CREATE TABLE IF NOT EXISTS songplays(
            songplay_id SERIAL PRIMARY KEY,
            start_time TIMESTAMP NOT NULL REFERENCES time(start_time),
            user_id VARCHAR(255) NOT NULL REFERENCES users(user_id),
            level TEXT NOT NULL,
            artist_id VARCHAR(255) NOT NULL REFERENCES artists(artist_id),
            song_id VARCHAR(255) NOT NULL REFERENCES songs(song_id),
            session_id INTEGER NOT NULL,
            location TEXT NOT NULL,
            user_agent TEXT NOT NULL
            );
        ''')
    
    queries = users, songs, artists, time, songplays
    create_table_lists = []
    for query in queries:
        create_table_lists.append(query)
    return create_table_lists
    
    
