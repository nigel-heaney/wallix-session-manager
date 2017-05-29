#!/usr/bin/env python
import sqlite3 as sql
import cgi
import cgitb
import dbserver
cgitb.enable()

debug=0
form = cgi.FieldStorage()

if not form.has_key('servername'):
	#default to !
	servername = 'nobody'
else:
	Servername = form['servername'].value


odd=1
oddstr="<td id=odd>"
evenstr="<td id=even>"

webheader='''<!DOCTYPE html">
Content-type: text/html

<html>
<head>
<link rel="stylesheet" type="text/css" href="/www/interface-main.css">
</head>
<body>
<center>
<p>
<br>
'''

webfooter='''
</p>
</center>
</body>
</html>

'''
conn = sql.connect(dbserver.connStr)
dbCursor = conn.cursor()

query = "SELECT ServerName,[Alternate IP], [Alternate IP Type], [Alternate IP Description] FROM ASPAlternateIPs where ServerName like '"
query += Servername + "' order by [Alternate IP];"

dbCursor.execute(query)

print webheader

print "<h4>", "Alternate IP Details", "</h4><br>"
print "<table><tr><th>Options</th><th>Server Name</th><th>Alternate IP</th><th>Type</th><th>Description</th></tr>"
for (servername,vip,viptype,vipdesc) in dbCursor:
	if odd: 
		odd=0
		htmlstr=oddstr
	else:
		htmlstr=evenstr
		odd=1
	
	print htmlstr + '<a href="/cgi-bin/deletevip.py?vip=' + vip + '" title="Delete alternate IP"><img src="/www/delete.png" /></a></td>'
	print htmlstr + servername + "</td>"
	print htmlstr + vip + "</td>"
	print htmlstr + viptype + "</td>"
	print htmlstr + vipdesc + "</td>"
	print "</tr>"
print "</table><br>"
	
print webfooter
