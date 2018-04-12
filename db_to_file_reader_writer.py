import sqlite3
import csv
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def select_table(conn, table):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    print table
    sql = ''' SELECT * FROM  ''' + table
    cur.execute(sql)

    with open(table + '_file.csv', 'wb') as fout:
        writer = csv.writer(fout)
        writer.writerow([i[0] for i in cur.description])  # heading row
        writer.writerows(cur.fetchall())


def main():
    database = "hotel.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        tables = ["hotel", "address", "room", "roomprice", "roomcategory", "hotelroom"]
        print("Query table and write to file")
        for line in tables:
            select_table(conn, line)
        print ("thanks for running me :) ")

if __name__ == '__main__':
    main()
