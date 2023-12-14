import sqlite3
from sqlite3 import Error
from conn import create_connection
from create_tables import cr
from insert_data import insert

if __name__ == '__main__':
    # create_connection(r"sql\mojabaza12.db")
    # cr()
    insert()
