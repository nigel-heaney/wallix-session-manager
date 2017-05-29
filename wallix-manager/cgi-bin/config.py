#!/usr/bin/env python

import sqlite3 as sql
import cgi
import cgitb
import dbserver

debug=0

#<link rel="stylesheet" type="text/css" href="/www/interface-main.css">

webheader='''<!DOCTYPE html">
Content-type: text/html

<html>
<head>
</head>
<body>
<center>
<br>
<form name="insert" action="/cgi-bin/update.py" method="post">
<table>
'''

webfooter='''
</table>
<br><br><br><br>
<table>
<tr><td style="width: 150px">
<FORM><INPUT type="image" src="/www/back.jpg" VALUE="Back" title="Go Back to server list" onClick="history.go(-1);return false;"></FORM>
</td>
<td style="width: 150px">
<INPUT TYPE="image" title="Save Configuration" src="/www/save2.jpg" />
</td>
</td>
<td style="width: 150px">
<img src="/www/help.png" Title="Help" onclick="confirm('Errrh comeback later...')" />
</td>
</table>
</form>
</center>
</body>
</html>

'''

def load_config():
	config={}
	conn = sql.connect(dbserver.config_db)
	dbCursor = conn.cursor()
	query = "SELECT * from config;"
	dbCursor.execute(query)
	for (parameter,value) in dbCursor:
		config[parameter]=value
		if debug: print "DEBUG: Parameter:", parameter, '  -->  ',value
	return config

	
def main():
	cgitb.enable()
	form = cgi.FieldStorage()
	config=load_config()

	print webheader
	print '<tr><td><font color="#0000FF"; size="4";>Wallix Server Configuration</font></td></tr>'
	print '<tr><td>Wallix Server</td><td> <input type="text" name="wserver" value="' + config['wallix_server'] + '"></td></tr>'
	print '<tr><td>Wallix AD User</td><td> <input type="text" name="wuserid" value="' + config['username'] + '"></td></tr>'
	print '<tr><td><br></td></tr>'
	print '<tr><td><font color="#0000FF"; size="4";>Suite User Configuration</font></td></tr>'
	print '<tr><td>Wallix Linux user 1</td><td> <input type="text" name="suitel1" value="' + config['suite_linuxuser1'] + '"></td></tr>'
	print '<tr><td>Wallix Linux user 2</td><td> <input type="text" name="suitel2" value="' + config['suite_linuxuser2'] + '"></td></tr>'
	print '<tr><td>Wallix Windows user 1</td><td> <input type="text" name="suitew1" value="' + config['suite_winuser1'] + '"></td></tr>'
	print '<tr><td>Wallix Windows user 2</td><td> <input type="text" name="suitew2" value="' + config['suite_winuser1'] + '"></td></tr>'
	print '<tr><td><br></td></tr>'
	print '<tr><td><font color="#0000FF"; size="4";>FXBO User Configuration</font></td></tr>'
	print '<tr><td>Wallix Linux user 1</td><td> <input type="text" name="fxbol1" value="' + config['fx_linuxuser1'] + '"></td></tr>'
	print '<tr><td>Wallix Linux user 2</td><td> <input type="text" name="fxbol2" value="' + config['fx_linuxuser2'] + '"></td></tr>'
	print '<tr><td>Wallix Windows user 1</td><td> <input type="text" name="fxbow1" value="' + config['fx_winuser1'] + '"></td></tr>'
	print '<tr><td>Wallix Windows user 2</td><td> <input type="text" name="fxbow2" value="' + config['fx_winuser2'] + '"></td></tr>'
	print '<tr><td><br></td></tr>'
	print '<tr><td><font color="#0000FF"; size="4";>Swift User Configuration</font></td></tr>'
	print '<tr><td>Wallix Windows user 1</td><td> <input type="text" name="swiftw1" value="' + config['swift_user1'] + '"></td></tr>'
	print '<tr><td>Wallix Windows user 2</td><td> <input type="text" name="swiftw2" value="' + config['swift_user2'] + '"></td></tr>'
	print '<tr><td><br></td></tr>'
	print '<tr><td><font color="#0000FF"; size="4";>Treasury User Configuration</font></td></tr>'
	print '<tr><td>Wallix Windows user 1</td><td> <input type="text" name="tryw1" value="' + config['try_winuser1'] + '"></td></tr>'
	print '<tr><td>Wallix Windows user 2</td><td> <input type="text" name="tryw2" value="' + config['try_winuser2'] + '"></td></tr>'
	print '<tr><td><br></td></tr>'
	print '<tr><td><font color="#0000FF"; size="4";>Miscellaneous User Configuration</font></td></tr>'
	print '<tr><td>Wallix Linux user 1</td><td> <input type="text" name="otherl1" value="' + config['other_linuxuser1'] + '"></td></tr>'
	print '<tr><td>Wallix Linux user 2</td><td> <input type="text" name="otherl2" value="' + config['other_linuxuser2'] + '"></td></tr>'
	print '<tr><td>Wallix Windows user 1</td><td> <input type="text" name="otherw1" value="' + config['other_winuser1'] + '"></td></tr>'
	print '<tr><td>Wallix Windows user 2</td><td> <input type="text" name="otherw2" value="' + config['other_winuser2'] + '"></td></tr>'
	print webfooter

if __name__ == "__main__":
	main()
	
	
