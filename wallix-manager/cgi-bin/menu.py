#!/usr/bin/env python
import cgi
import cgitb
import sqlite3 as sql
import dbserver
cgitb.enable()

customer_list=[]
form = cgi.FieldStorage()
if not form.has_key('product'):
	#default to suite!
	product = 'suite'
else:
	product = form['product'].value
	
webheader='''<!DOCTYPE html">
Content-type: text/html

<html>
<head>
<link rel="stylesheet" type="text/css" href="/www/interface.css">
</head>
<body>
<center>
Wallix<br>Session Manager
<hr>
<div style="width:150px;border:1px;"">
<a href="/cgi-bin/menu.py?product=fx" target="menu">APP1</a>
  |  
<a href="/cgi-bin/menu.py?product=suite" target="menu">APP2</a>
  |  
<a href="/cgi-bin/menu.py?product=treasury" target="menu">APP3</a>
</center>
</div>
'''

webfooter='''
	<hr><h4>Search</h4>
	<center>
	<form action="/cgi-bin/search.py" method="get" target="main"><input type="text" name="customer">
	</form></center>
	<hr><h4>Other Servers</h4>
	<a href="/cgi-bin/select-customers.py?customer=shared" target="main">SHARED SERVERS</a>
	<center>
	<hr>
	<div style="position:absolute; bottom:5;left:0; width:200px;">
	<h4>Admin</h4><hr>
	<a class="img" href="/cgi-bin/config.py" target="main"><img src="/www/config.png" title="Update Configuration"></a>
	<br><h3>&copy2014 Nigel_Heaney</h3>
	</div>
	
	</center>
</body>
</html>
'''

conn = sql.connect(dbserver.connStr)
dbCursor = conn.cursor()
query = "SELECT Customer FROM ASPServer where Product like '"
query += product + "';"

dbCursor.execute(query)
customer_list = [str(x[0]) for x in dbCursor]
customer_list = list(set(customer_list))
customer_list.sort()

print webheader
#show current customer list
for cust in customer_list:
	#print str(cust), "<br>"
	print '</br><a href="/cgi-bin/select-customers.py?customer=' + str(cust) + '" target="main">' + str(cust) + "</a>"

print webfooter
