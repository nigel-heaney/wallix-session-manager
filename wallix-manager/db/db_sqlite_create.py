#!/usr/bin/env python
import sqlite3 as sql
import sys

debug=0

query = "SELECT * FROM ws.ASPServer"

con = sql.connect('C:\\wallix-hw\\db\\servers.db')
cur = con.cursor()    
cur.execute("CREATE TABLE ASPServer(ServerName text, MainIP text,NATIP text,Customer text, Product text, Domain text, DataCentre text, Site text,ServerOS text,ServerEnvironment text,ServerUsage text,ServerDescription text,ServerType text, ServerCores text, ServerRAM text,Gateway text,Notes text,Deleted text,URL text,AccountID text,wallixid text, PRIMARY KEY(ServerName))")

cur.execute("CREATE TABLE ASPAlternateIPs(ServerName text, 'Alternate IP' text,'Alternate IP Type' text, 'Alternate IP Description' text)")
