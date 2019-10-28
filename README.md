# Sparkify-Data-Modeling-Postgres

## Summary

This project aims to model data to an SQL analytics database using PostgreSQL for a fictional music streaming service called Sparkify

## Overview
### Use-Case
As mentioned above in the summary, Sparkify is a music streaming service that provides online musical contents for its listeners. Currently, its analytics team will like to understand what, when and how users are playing songs on the company's music app. The analysts need an easy way to query and analyze the songplay data, which is currently stored in raw JSON logs and metadata files on a local directory.

Now as the data engineer assigned to the project, I am responsible for ensuring that data is made available for sparkify's data scientists; in order to achieve this i have to implement an ETL pipeline in python to process and upload the data into a PostgreSQL database (=> their SQL-choice basically <=). The ETL process will extract each songplay from the list of page actions recorded by the app. Data for analysis, such as song name, user information, subscription tier, and location of user, is structured into the main songplay table and related dimensional tables. 

## Pre-requisite Softwares
The software which i must work with includes:-

> ***Python 3.5 +***
 
 > ***PostgreSQL***
 
>  ***Psycopg2*** (*through pip installer package => Postgresql Client for python)
 
>  ***Pandas*** (*through pip installer package)
 
> ***Numpy*** (*through pip installer package)
 
>  ***JupyterLab*** (*through pip installer package)

## File Structure and Description
```bash
├──── Config =>: (FOLDER)
│     ├─ config.cfg =>: (.cfg contains configuration keys and values)
│     └─ config.py =>: (.py contains functions that execute the .cfg file through the help of ConfigParser)
│
├──── Sql_Queries =>: (FOLDER)
│     ├─ create_query.py =>: (create_query.py returns a list of execution templates that creates tables and if not present the SQL database)
│     ├─ drop_query.py =>: (drop_query.py returns a list of execution templates that deletes/drops tables from the database)
│     └─ insert_query.py =>: (insert_query.py contains execution templates that inserts data to tables)
│ 
├──── Data =>: (FOLDER)
│     ├─ Log_Data =>: (Folder contains .json log files)
│     │  ├─ 2018
│     │  │   ├─ 11
│     │  └───└───└─ {.json}
│     │  
│     ├─ Song_Data =>: (Folder contains .json song files)
│     │  ├─ A
│     │  │  ├─ A
│     │  │  │  └─ A
│     │  │  │     └─ {.json}
│     │  └──└── B
│     │         └── A
│     │         │   └─ {.json}
│     │         └───B
│     │         │   └─ {.json} 
│     │         └───C
│     └─────────────└─ {.json}
│
├────── etl.py =>: (etl.py iterates through the song_data and log_data directories and then returns lists of all the extracted and processed data)
├────── migrations.py =>: (migrations.py inserts and executes the data output of etl.py file to the queries from sql_queries)
├────── main.py =>: (main.py is the starting point for execution for this project)
├────── test.ipynb =>: (test.ipynb is basically a notebook where queries can be tested and executed)
├────── README.md
└────── .gitignore
```

## Execution Steps

To begin execution, **cd** to the directory where **main.py** resides and run the following command on terminal
> <code> python main.py </code>   

The following occurs if the script executed successfully without any hassle

1.) The database **sparkifydb** will be created.

2.) The tables - **users**, **songs**, **artists**, **time** and **songplays** will be included into the database.

3.) Data from the log_data and song_data directories will also be appended to the tables.

## Database Schema

The sparkify database design uses the simple star schema shown below. The schema contains one fact table, *songplays*, and four dimension tables: *songs*, *artists*, *users* and *time*. The fact table references the primary keys of each dimention table, enabling joins to songplays on song_id, artist_id, user_id and start_time, respectively. This structure will enable the analysts to aggregate the data efficiently and explore it using standard SQL queries. 

![Database schema diagram](database_schema_diagram.png)

###### Instructions for generating the schema diagram using [sqlalchemy_schemadisplay](https://github.com/fschulze/sqlalchemy_schemadisplay) were provided by Syed Mateen in the project-1-dend-v1 slack channel. Thanks Syed!

Each songplay in the fact table is identified by a unique uuid generated from the song, user id and timestamp of the log entry. This field is set as a primary key, so that it is unique and non-null. A constraint on the UPSERT operation ensures that there are no duplicate songplays in the database. If the log contains multiple entries with the same song, user id and timestamp, only the first entry is imported. The process of generating unique uuid's could be applied to all of the primary identifiers of the dimension tables. This would improve join efficiency if the database were very large.

To keep subscription data as up-to-date as log data allows, the users table updates the subscription status of the user ("level") when processing the data to reflect membership status as of the most recent songplay timestamp.

## Data Processing and Quality Checks

Data is extracted from two types of JSON source files: song data from the [Million Song Dataset](https://labrosa.ee.columbia.edu/millionsong/) and songplay data from user logs. The JSON files are read into pandas dataframes, processed and uploaded into the database using psycopg2. 

A number of steps clean the data and reduce the size of the database by removing data not needed for the analysis: 
* Songplays are identified by filtering for actions initiated from the 'NextSong' page. 
* Timestamps are converted from UNIX time to datetime format without time zone prior to upload.
* Rows from the users table are excluded where user_id is missing.
* Rows from the artists table are excluded where artist_id is missing. 

## Example Queries and Results

The dataset contains 6,820 songplays from November 2018.

> <code> SELECT tm.month, tm.year, COUNT(sp.songplay_id) as songplay_count 
  FROM songplays sp 
  LEFT JOIN time tm 
   ON sp.start_time = tm.start_time 
  GROUP BY tm.month, tm.year;</code>

81% of songplays -- 5591 streams -- are generated by paid members.

> <code> SELECT 
    sp.level, 
    COUNT(sp.songplay_id) as songplay_count, 
    100*COUNT(sp.songplay_id)/(select count(s.songplay_id) from songplays s) as percent 
  FROM songplays sp GROUP BY sp.level; </code>
  
<p>

    for more info on how to execute some queries, you can checkout test.ipynb notebook
</p>



