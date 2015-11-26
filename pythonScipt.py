import sys
import mysql.connector
from mysql.connector import errorcode

DB_NAME = sys.argv[1]
print("DB name:",DB_NAME)

TABLES = {}
TABLES['WIND'] = (
    "CREATE TABLE `WIND` ("
    "  `runtime` DATETIME NULL,"
    "  `validtime` DATETIME NULL, `lat` FLOAT NULL,"
    "  `lon` FLOAT NULL,"
    "  `parameter` VARCHAR (255) NULL,"
    "  `level` VARCHAR (255) NULL,"
    "  `val` FLOAT NULL"
    ") ENGINE=InnoDB")

TABLES['TCDC'] = (
    "CREATE TABLE `TCDC` ("
    "  `runtime` DATETIME NULL,"
    "  `validtime` DATETIME NULL, `lat` FLOAT NULL,"
    "  `lon` FLOAT NULL,"
    "  `parameter` VARCHAR (255) NULL,"
    "  `level` VARCHAR (255) NULL,"
    "  `val` FLOAT NULL"
    ") ENGINE=InnoDB")
cnx = mysql.connector.connect(user='root',password='root')
cursor = cnx.cursor()
print cursor
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
try:
    cnx.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)
for name, ddl in TABLES.iteritems():
    try:
        print("Creating table: {} ".format(name))
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()
sys.exit()
