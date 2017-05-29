#!/usr/bin/env python
import sqlite3 as sql
import cgi
import cgitb
import dbserver
import re
cgitb.enable()

debug=0
form = cgi.FieldStorage()

if not form.has_key('customer'):
	#default to nobody!
	customer = 'noclient'
else:
	#customer = form['customer'].value[1:-1]
	customer = form['customer'].value


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

funcs='''
<script>	
	function launch(servername,wallixid,serverenv,product,domain,u) {
		var request = new XMLHttpRequest();
		var url = '/cgi-bin/launch.py?servername=' + servername + '&wid=' + wallixid + '&u=' + u + '&type=' + serverenv + '&p=' + product + '&d=' + domain;
		request.open("GET", url, true);
		request.send(null);
	}
	function launchsftp(servername,wallixid,serverenv,product,domain,u) {
		var request = new XMLHttpRequest();
		var url = '/cgi-bin/launchsftp.py?servername=' + servername + '&wid=' + wallixid + '&u=' + u + '&type=' + serverenv + '&p=' + product + '&d=' + domain;
		request.open("GET", url, true);
		request.send(null);
	}
</script>
'''

webfooter='''
</p>
</center>
</body>
</html>

'''
conn = sql.connect(dbserver.connStr)
dbCursor = conn.cursor()

query = "SELECT ServerEnvironment,ServerUsage,NATIP,Servername,DataCentre,Domain,ServerDescription,mainip,site,wallixid,Product,ServerOS FROM ASPServer where  "
query += "Customer like '%" + customer + "%' OR "
query += "ServerEnvironment like '%" + customer + "%' OR "
query += "ServerUsage like '%" + customer + "%' OR "
query += "NATIP like '%" + customer + "%' OR "
query += "Servername like '%" + customer + "%' OR "
query += "DataCentre like '%" + customer + "%' OR "
query += "Domain like '%" + customer + "%' OR "
query += "ServerDescription like '%" + customer + "%' OR "
query += "mainip like '%" + customer + "%' AND "
query += "Deleted = 'N' order by ServerEnvironment desc, ServerUsage;"

dbCursor.execute(query)

if debug:
	print webheader
	print "form:",form
	print "<br>query:", query
	exit(0)

print webheader
print funcs

print "<h4>", customer, "</h4><br>"
print "<table><tr><th>Options</th><th>Customer</th><th>Server Name</th><th>Main IP</th><th>NAT</th><th>Type</th><th>Function</th><th>Description</th><th>DC</th><th>Domain</th><th>Wallix ID</th></tr>"
for (serverenv,serverusage,wssnat,servername,datacentre,domain,serverdesc,mainip,site,wallixid,product,serveros) in dbCursor:
	if serverenv == None: serverenv = "--NA--"
	if serverusage == None: serverusage = "--NA--"
	if wssnat == None: wssnat = "--NA--"
	if mainip == None: mainip = "--NA--"
	if servername == None: servername = "--NA--"
	if serverdesc == None: serverdesc = "--NA--"
	if serveros == None: serverdesc = "--NA--"
	if odd: 
		odd=0
		htmlstr=oddstr
	else:
		htmlstr=evenstr
		odd=1
	
	print htmlstr + '<a href="/cgi-bin/select-customer-vips.py?servername=' + servername + '" title="List Alternate IP Addresses"><img src="/www/showvip.png" /></a>'
	title1="Connect to " + servername + " using application user1"
	title2="Connect to " + servername + " using application user2"
	print '''<img src="/www/ssh1.png" onclick="launch('{0}','{1}','{2}','{3}','{4}','{5}','{7}')" title="{6}"/>'''.format(servername,wallixid,serverenv,product,domain,"1", title1,serveros)
	print '''<img src="/www/ssh2.png" onclick="launch('{0}','{1}','{2}','{3}','{4}','{5}','{7}')" title="{6}"/>'''.format(servername,wallixid,serverenv,product,domain,"2", title2,serveros)
	if re.search("[Ll]inux",serveros):
		print '''<img src="/www/sftp1.png" onclick="launchsftp('{0}','{1}','{2}','{3}','{4}','{5}','{7}')" title="{6}"/>'''.format(servername,wallixid,serverenv,product,domain,1, "SFTP with server using app user 1",serveros)
		print '''<img src="/www/sftp2.png" onclick="launchsftp('{0}','{1}','{2}','{3}','{4}','{5}','{7}')" title="{6}"/>'''.format(servername,wallixid,serverenv,product,domain,"2", "SFTP with server using app user 2",serveros)
	
	print htmlstr + servername + "</td>"
	print htmlstr + mainip + "</td>"
	print htmlstr + wssnat + "</td>"
	print htmlstr + serverenv + "</td>"
	print htmlstr + serverusage + "</td>"
	print htmlstr + serverdesc + "</td>"
	print htmlstr + datacentre + "</td>"
	print htmlstr + domain + "</td>"
	print htmlstr + site + "</td>"
	print htmlstr + wallixid + "</td>"
	print "</tr>"

print "</table><br>"
	
print webfooter
