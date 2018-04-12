import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = "hotel.db"

    sql_create_hotelroom_table = """ CREATE TABLE IF NOT EXISTS hotelroom (
                                    room_id int (4) NOT NULL,
                                    hotel_id int(4) NOT NULL ,
                                    PRIMARY KEY(room_id,hotel_id)
                                    ); """

    sql_create_room_table = """CREATE TABLE IF NOT EXISTS room (
                                    room_id int (4) NOT NULL PRIMARY KEY,
                                    number_beds int(10) NOT NULL, 
                                    price CHAR (30) NOT NULL,
                                    category CHAR (50) NOT NULL,
                                    FOREIGN KEY (category) REFERENCES roomcategory (category),
                                    FOREIGN KEY (price) REFERENCES roomprice (price));"""

    sql_create_roomprice_table = """CREATE TABLE IF NOT EXISTS roomprice (
                                       price CHAR (30) NOT NULL PRIMARY KEY
                                   );"""
    sql_create_roomcategory_table = """CREATE TABLE IF NOT EXISTS roomcategory (
                                           category CHAR (30) NOT NULL PRIMARY KEY
                                       );"""

    sql_create_hotel_table = """ CREATE TABLE IF NOT EXISTS hotel (
                                            id int (4) NOT NULL PRIMARY KEY,
                                            name CHAR (50) NOT NULL
                                        ); """

    sql_create_address_table = """CREATE TABLE IF NOT EXISTS address (
                                        id int (4) NOT NULL PRIMARY KEY,
                                        hotel_id int(4) NOT NULL,
                                        zip CHAR(5),
                                        street CHAR(30),
                                        city CHAR (30) NOT NULL,
                                        country CHAR(30) NOT NULL,
                                          FOREIGN KEY (hotel_id) REFERENCES hotel (id));"""


    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_hotel_table)
        create_table(conn, sql_create_address_table)
        create_table(conn, sql_create_hotelroom_table)
        create_table(conn, sql_create_roomprice_table)
        create_table(conn, sql_create_roomcategory_table)
        create_table(conn, sql_create_room_table)

        hotel = (10,'Prague Hotel'),(20,'Brno Hotel'), (30,'Hradec Hotel')
        address= (60601,10,'11000','Na prikope 2','Prague', 'CZ'), (60602,30,'53000','city center','Hradec', 'CZ'),(60603,20,'42200','Na prikope 2','Brno', 'CZ')
        roomprice= ('40',), ('30',), ('20',), ('10',), ('25',), ('15',)
        roomcategory=('suite',),('superior',), ('standard',),('basic',)
        room=(133,'suite',4,'40'),(233,'superior',3, '30'),(222,'standard',2, '20'),(241,'basic',1, '10'),(524,'standard',2, '25'),(546,'basic',1, '15')
        hotelroom=(133, 10),(233, 10),(222, 20),(241, 20),(133, 30),(524, 30),(546, 30)
        # insert data
        create_hotel(conn, hotel)
        create_address(conn, address)
        create_roomprice(conn, roomprice)
        create_roomcategory(conn, roomcategory)
        create_room(conn, room)
        create_hotelroom(conn, hotelroom)

    else:
        print("Error! cannot create the database connection.")


def create_hotel(conn, hotel):
    sql = ''' INSERT INTO hotel
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.executemany(sql, hotel)
    conn.commit()
    return cur.lastrowid

def create_address(conn, address):
    sql = ''' INSERT INTO address
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    print address
    cur.executemany(sql, address)
    conn.commit()
    return cur.lastrowid

def create_roomprice(conn, roomprice):
    sql = ''' INSERT INTO roomprice
              VALUES(?) '''
    cur = conn.cursor()
    print roomprice
    cur.executemany(sql, roomprice)
    conn.commit()
    return cur.lastrowid

def create_roomcategory(conn, roomcategory):
    sql = ''' INSERT INTO roomcategory
              VALUES(?) '''
    cur = conn.cursor()
    cur.executemany(sql, roomcategory)
    conn.commit()
    return cur.lastrowid

def create_room(conn, room):
    sql = ''' INSERT INTO room
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.executemany(sql, room)
    conn.commit()
    return cur.lastrowid

def create_hotelroom(conn, hotelroom):
    sql = ''' INSERT INTO hotelroom
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.executemany(sql, hotelroom)
    conn.commit()
    return cur.lastrowid



if __name__ == '__main__':
    main()
