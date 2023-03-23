"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""

import os
import inspect
import sqlite3
from faker import Faker
from datetime import datetime

def main():
    global db_path
    db_path = os.path.join(get_script_dir(), 'social_network.db')
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # TODO: Create function body

    # Open a connection to the database.
    con = sqlite3.connect(db_path)
    # Get a Cursor object that can be used to run SQL queries on the database.

    cur = con.cursor()
    # Define an SQL query that creates a table named 'people'.
    # Each row in this table will hold information about a specific person.
    create_ppl_tbl_query = """
    CREATE TABLE IF NOT EXISTS people
    (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    province TEXT NOT NULL,
    bio TEXT,
    age INTEGER,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
    );
    """
    
    # Execute the SQL query to create the 'people' table.
    # Database operations like this are called transactions.
    cur.execute(create_ppl_tbl_query)

    # Commit (save) pending transactions to the database.
    # Transactions must be committed to be persistent.
    con.commit()

    # Close the database connection.
    # Pending transactions are not implicitly committed, so any
    # pending transactions that have not been committed will be lost.
    con.close()
    return

def populate_people_table():
    """Populates the people table with 200 fake people"""
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    # Define an SQL query that inserts a row of data in the people table.
    # The ?'s are placeholders to be fill in when the query is executed.
    # Specific values can be passed as a tuple into the execute() method.
    add_person_query = """
    INSERT INTO people
    (
    name,
    email,
    address,
    city,
    province,
    bio,
    age,
    created_at,
    updated_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """


    # Create a faker object for English Canadian locale
    fake = Faker("en_CA")

    # Generate fake data for 200 people
    for _ in range(200):
        person = (fake.name(), 
                  fake.email(), 
                  fake.street_address(), 
                  fake.city(), 
                  fake.administrative_unit(), 
                  fake.sentence(nb_words=15, variable_nb_words=False),
                  fake.random_int(min=1, max=100),
                  datetime.now(),
                  datetime.now()) 
        cur.execute(add_person_query, person)
    
    # Execute query to add new person to people table
    con.commit()
    con.close()

    return

def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

if __name__ == '__main__':
   main()