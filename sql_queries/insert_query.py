# INSERT VALUES INTO TABLES
# >>songplays, users, songs, artists, time

users = ('''
    INSERT INTO users(
        user_id, first_name, last_name, gender, level)
        VALUES (%s,%s,%s,%s,%s) ON CONFLICT (user_id) DO UPDATE SET level = excluded.level
''')
    
songs = ('''
    INSERT INTO songs(
        song_id, title, artist_id, year, duration)
        VALUES (%s,%s,%s,%s,%s) ON CONFLICT (song_id) DO NOTHING
''')
    
artists = ('''
    INSERT INTO artists(
        artist_id, name, location, latitude, longitude
    ) VALUES (%s,%s,%s,%s,%s) ON CONFLICT (artist_id) DO NOTHING
''')
    
time = ('''
    INSERT INTO time(
        start_time, hour, day, week, month, year, weekday
    ) VALUES (%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (start_time) DO NOTHING
''')
 
songplays = ('''
    INSERT INTO songplays(
        start_time, user_id, level, artist_id, song_id, session_id, location, user_agent)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
''')
    

    