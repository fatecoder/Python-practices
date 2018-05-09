#!/bin/python

import MySQLdb

def expample() :
    db = MySQLdb.connect("localhost", "testuser", "test123", "prueba")

    cursor = db.cursor()

    cursor.execute("select * from empleado")

    data = cursor.fetchone()

    print data[0]

    db.close()

def creating_table():
    db = MySQLdb.connect("localhost", "testuser", "test123", "prueba")
    cursor = db.cursor()
    cursor.execute("drop table if exists empleado")
    sql = """create table empleado (
             nombre varchar(25) not null,
             apellidos varchar(40) not null,
             edad int not null,
             sexo varchar(1) not null,
             ingresos float not null)"""

    cursor.execute(sql)

    db.close()

def insert_values():
    db = MySQLdb.connect("localhost", "testuser", "test123", "prueba")
    cursor = db.cursor()
    sql = "insert into employee values,\
           ('%s', '%s', '%d', '%c', '%d')" %\
           ('Ricardo', 'Ramirez Rodriguez', 20, 'H', 10000)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()

insert_values()
