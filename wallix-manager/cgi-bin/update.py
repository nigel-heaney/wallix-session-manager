#!/usr/bin/env python
import sqlite3 as sql
import pyodbc
import cgi
import cgitb
import dbserver
import sys
cgitb.enable()

debug=0
form = cgi.FieldStorage()

webheader='''<!DOCTYPE html">
Content-type: text/html

<html>
<head>
</head>
<body>
<center>
<p>
<br>
'''

webfooter='''
</table>
<br><br><br><br>
<table>
<tr><td style="width: 150px" align="center">
<FORM><INPUT type="image" src="/www/back.jpg" VALUE="Back" title="Go Back to server list" onClick="history.go(-1);return false;"></FORM>
</td>
<td style="width: 150px" align="center">
<a href="/www/main.html"><img src="/www/home2.jpg" Title="Home"/>
</td>
<td style="width: 150px" align="center">
<img src="/www/help.png" Title="Help" onclick="confirm('Are you serious?')" />
</td>
</table>
</form>

</p>
</center>
</body>
</html>

'''

#Retrieve form data and validate
wallix_server = form.getvalue('wserver')
username = form.getvalue('wuserid')
suite_linuxuser1 = form.getvalue('suitel1')
suite_linuxuser2 = form.getvalue('suitel2')
suite_winuser1 = form.getvalue('suitew1')
suite_winuser2 = form.getvalue('suitew2')
fxbo_linuxuser1 = form.getvalue('fxbol1')
fxbo_linuxuser2 = form.getvalue('fxbol2')
fxbo_winuser1 = form.getvalue('fxbow1')
fxbo_winuser2 = form.getvalue('fxbow2')
other_linuxuser1 = form.getvalue('otherl1')
other_linuxuser2 = form.getvalue('otherl2')
other_winuser1 = form.getvalue('otherw1')
other_winuser2 = form.getvalue('otherw2')
swift_user1 = form.getvalue('swiftw1')
swift_user2 = form.getvalue('swiftw2')
try_winuser1 = form.getvalue('tryw1')
try_winuser2 = form.getvalue('tryw2')


conn = sql.connect(dbserver.config_db)
dbCursor = conn.cursor()

query=[]
query.append("update config SET parameter = '" + wallix_server + "' WHERE value = 'wallix_server'")
query.append("update config SET parameter = '" + username      + "' WHERE value = 'username'")
query.append("update config SET parameter = '" + suite_linuxuser1 + "' WHERE value = 'suite_linuxuser1'")
query.append("update config SET parameter = '" + suite_linuxuser2 + "' WHERE value = 'suite_linuxuser2'")
query.append("update config SET parameter = '" + suite_winuser1 + "' WHERE value = 'suite_winuser1'")
query.append("update config SET parameter = '" + suite_winuser2 + "' WHERE value = 'suite_winuser2'")
query.append("update config SET parameter = '" + fxbo_linuxuser1 + "' WHERE value = 'fx_linuxuser1'")
query.append("update config SET parameter = '" + fxbo_linuxuser2 + "' WHERE value = 'fx_linuxuser2'")
query.append("update config SET parameter = '" + fxbo_winuser1 + "' WHERE value = 'fx_winuser1'")
query.append("update config SET parameter = '" + fxbo_winuser2 + "' WHERE value = 'fx_winuser2'")
query.append("update config SET parameter = '" + other_linuxuser1 + "' WHERE value = 'other_linuxuser1'")
query.append("update config SET parameter = '" + other_linuxuser2 + "' WHERE value = 'other_linuxuser2'")
query.append("update config SET parameter = '" + other_winuser1 + "' WHERE value = 'other_winuser1'")
query.append("update config SET parameter = '" + other_winuser2 + "' WHERE value = 'other_winuser2'")
query.append("update config SET parameter = '" + swift_user1 + "' WHERE value = 'swift_user1'")
query.append("update config SET parameter = '" + swift_user2 + "' WHERE value = 'swift_user2'")
query.append("update config SET parameter = '" + try_winuser1 + "' WHERE value = 'try_winuser1'")
query.append("update config SET parameter = '" + try_winuser2 + "' WHERE value = 'try_winuser2'")

print webheader

try:
	for r in range(len(query)):
		if debug: print >>sys.stderr, query[r]
		dbCursor.execute(query[r])
except Exception, e :
	print "<h4>ERROR: problem writing to DB</h4>"
	print e
	pass
else:
	conn.commit()
	print '<h1>Database Successfully Updated!</h1>'
print webfooter
