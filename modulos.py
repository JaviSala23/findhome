# -*- coding: 850 -*-


import psycopg2
import sys
import base64
import datetime
from datetime import date

#coneccion
cone= "false"
def coneccion(hosts,base,user,password):
    con = None
    try:
        con = psycopg2.connect(host=hosts,database=base, user=user, password=password)
        cone= "true"
        retorno=[con,cone]
        return retorno
    except psycopg2.DatabaseError, e:
        con="out"
        cone= "false"
        retorno=[con,cone]
        return retorno
        print 'imposible conectar'

def serverfile(a,b):
    a=base64.encodestring(a)
    b=base64.encodestring(b)
    files = open("server.txt","w")
    files.write("localhost\n")
    files.write("basedb1\n")
    files.write(a)
    files.write(b)
    files.close()

def readline():
    informacion=[]
    files=open("server.txt","r")
    for line in files:
        informacion=informacion + [line]
    sal= informacion[0]
    sal= sal[0:(len(sal)-1)]
    informacion[0]=sal

    sal= informacion[1]
    sal= sal[0:(len(sal)-1)]

    informacion[1]=sal

    sal= informacion[2]
    sal= sal[0:(len(sal)-1)]
    informacion[2]=sal
    informacion[2]=base64.decodestring(informacion[2])
    sal= informacion[3]
    sal= sal[0:(len(sal)-1)]
    informacion[3]=sal
    informacion[3]=base64.decodestring(informacion[3])
    return informacion
    files.close()

def seleccion(fecha):
    d=date.today()
    day=int(d.day)
    month=int(d.month)
    year=int(d.year)
    fechan=fecha.split('/')
    year1=int(fechan[2])
    month1=int(fechan[1])
    day1=int(fechan[0])
    if year1<year:
        return "vencido"
    elif year1 == year:
        if month1 < month:
            return "vencido"
        if month1== month:
            if day1 < day:
                return "vencido"
    else:
        return "en orden"



