#!/usr/bin/env python3
import pprint
import sqlite3
import argparse
import xlsxwriter
import mysql.connector

parser = argparse.ArgumentParser(description='Process db file')
parser.add_argument('--filename', help='sqlite3 filename')
parser.add_argument("--export", help="Export all tables to xlsx", action="store_true")
args = parser.parse_args()


def read_data_sqlite3(filename):
    conn_lite = sqlite3.connect(filename)
    cursor_lite = conn_lite.cursor()
    cursor_lite.execute("SELECT * FROM univer")
    return cursor_lite.fetchall()



def write_data_mysql(data):
    conn_mysql = mysql.connector.connect(
            host='localhost',
            user='temp',
            password='123',
            database='univer'
        )
    cursor_mysql = conn_mysql.cursor()
    cursor_mysql.execute('drop table if exists customers')
    cursor_mysql.execute('drop table if exists branch')
    cursor_mysql.execute('drop table if exists group_customers')
    cursor_mysql.execute('drop table if exists groups')
    cursor_mysql.execute('drop table if exists gender')
    cursor_mysql.execute('create table customers(id integer(255), name varchar(255), sur_name varchar(255), registration_date varchar(255), gender_id integer(255), city varchar(255))')
    cursor_mysql.execute('create table branch(id integer(255),name varchar(255),phone varchar(255))')
    cursor_mysql.execute('create table group_customers(id integer(255),customer_id integer(255),group_id integer(255))')
    cursor_mysql.execute('create table groups(id integer(255), branch_id integer(255), name varchar(255))')
    cursor_mysql.execute('create table gender(id integer(255), name varchar(255))')
    id = 1
    cursor_mysql.execute(f'INSERT INTO gender(id,name) VALUES (1,"male")')
    cursor_mysql.execute(f'INSERT INTO gender(id,name) VALUES (2,"female")')
    for item in data:
        #('Petr', 'Petrov', 'male', 'Perm', 'new', '2222222222', 'normal', '31.11.2019')
        print(item)
        if item[2] == 'male':
            gender_id = 1
        else:
            gender_id = 2
        cursor_mysql.execute(f'INSERT INTO customers(id,name,sur_name,registration_date,gender_id,city) VALUES ({id},"{item[0]}","{item[1]}","{item[7]}",{gender_id},"{item[3]}")')
        cursor_mysql.execute(f'INSERT INTO branch(id,name,phone) VALUES ({id},"{item[4]}","{item[5]}")')
        cursor_mysql.execute(f'INSERT INTO group_customers(id,customer_id,group_id) VALUES ({id},{id},{id})')
        cursor_mysql.execute(f'INSERT INTO groups(id,branch_id,name) VALUES ({id},{id},"{item[6]}")')
        conn_mysql.commit()
        id += 1

    conn_mysql.close()
    print(f"Successfully inserted to univer ")
    return "kek"


#TODO: DODELAT'
def export():
    conn_mysql = mysql.connector.connect(
            host='localhost',
            user='temp',
            password='123',
            database='univer'
        )
    cursor_mysql = conn_mysql.cursor()
    cursor_mysql.execute("SHOW tables")
    tables = cursor_mysql.fetchall()
    print(tables)
    workbook = xlsxwriter.Workbook('all_tables.xlsx')
    worksheet = workbook.add_worksheet('MENU')
    header_cell_format = workbook.add_format({'bold': True, 'border': True, 'bg_color': 'yellow'})
    body_cell_format = workbook.add_format({'border': True})
    row_index = 0
    for tablename_raw in tables:
        rows = []
        tablename = str(tablename_raw)[2:-3]
        print(f'{tablename}')
        cursor_mysql.execute(f'select * from {tablename}')
        header = [row[0] for row in cursor_mysql.description]
        rows += cursor_mysql.fetchall()


        column_index = 0
        row_index += 1
        worksheet.write(row_index, column_index, tablename, header_cell_format)
        row_index += 1

        for column_name in header:
            worksheet.write(row_index, column_index, column_name, header_cell_format)
            column_index += 1

        row_index += 1
        for row in rows:
            column_index = 0
            for column in row:
                # write
                worksheet.write(row_index, column_index, column, body_cell_format)
                column_index += 1
            row_index += 1

    print(str(row_index) + ' rows written successfully to ' + workbook.filename)
    workbook.close()
    conn_mysql.close()




if args.export:
    export()
elif args.filename:
    data = read_data_sqlite3(args.filename)
    write_data_mysql(data)
else:
    print("Add some functions or --help for help")










