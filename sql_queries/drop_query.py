# DROP TABLES
# >>songplays, users, songs, artists, time

def dropTables():
    users = '''DROP TABLE IF EXISTS users CASCADE;'''
    songs = '''DROP TABLE IF EXISTS songs CASCADE;'''
    artists = '''DROP TABLE IF EXISTS artists CASCADE;'''
    time = '''DROP TABLE IF EXISTS time CASCADE;'''
    songplays = '''DROP TABLE IF EXISTS songplays CASCADE;'''
    
    queries = users, songs, artists, time, songplays
    drop_table_lists = []
    for query in queries:
        drop_table_lists.append(query)
    return drop_table_lists