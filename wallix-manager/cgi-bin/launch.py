#!/usr/bin/env python
# launch rdp/putty/sftp connection via wallix
# wallix_user, servername

import sqlite3 as sql
import re
import os
import sys
import subprocess
import cgi
import cgitb
import dbserver

debug=1

webheader='''<!DOCTYPE html">
Content-type: text/html

<!DOCTYPE html">
<html>
<head>
<script>
function CloseWin()
{
	close();
}

</script>
</head>
<body onLoad="CloseWin()">
'''

webfooter='''
</body>
</html>
'''

def printweb():
	print webheader
	print webfooter
	sys.exit()
	
def launch(config,wid='',servername='',appuser=1,type='',product='',domain='DOMAIN',serveros='None'):
	'''search db for matching entry and launch - this can use any part of the string but mainly use server name or wallixid'''
	if wid=='NA': 
		print >>sys.stderr, "ERROR: Wallix does not support this server"
		printweb()
	#determine putty profile to use
	if re.search("inux",serveros):
		if re.search('PROD',type): 
			profile='Production'
		elif re.search('DR',type): 
			profile='DR'
		else:
			profile='Test'

		#determine which product so the correct user can be chosen.
		if product=='suite':
			u='suite_linuxuser' + str(appuser)
			user=config[u]
		elif product=='fx':
			u='fx_linuxuser' + str(appuser)
			user=config[u]
		else:
			#if product is unknown then allow to default to other users
			u='other_linuxuser' + str(appuser)
			user=config[u]
	
		
		f=open('temp\\ssh.vbs','w')
		f.write('Set objShell = WScript.CreateObject("WScript.Shell")\n')
		f.write('objShell.Run ("bin\\putty.exe -load '  +  profile + " " + user + "@" + wid + ":SSH:" + config["username"] + "@" + config["wallix_server"] + '") \n')
		f.close()
		#cmd=[ 'start', 'bin\\putty.exe','-load', profile, user + '@' + wid + ':SSH:' + config['username'] + '@' + config['wallix_server'] ]
		cmd=[ 'start', 'temp\\ssh.vbs' ]
		if debug: print cmd
		subprocess.Popen(cmd,shell=True,stdin=None, stdout=None, stderr=None,close_fds=True)
		printweb()

	elif re.search("[Ww]indows",serveros):
		if product=='suite':
			u='suite_winuser' + str(appuser)
			user=config[u]
		elif product=='fx':
			u='fx_winuser' + str(appuser)
			user=config[u]
		elif product=='try':
			u='fx_winuser' + str(appuser)
			user=config[u]
		else:
			#if product is unknown then allow to default to other users
			u='other_winuser' + str(appuser)
			user=config[u]

		f=open('temp\\launch.rdp','w')
		f.write("full address:s:" + config['wallix_server'] + "\n")
		print "username:s:" + domain + "\\" + user + "@" + wid + ":RDP:" + config['username'] + "\n"
		f.write("username:s:" + domain + "\\" + user + "@" + wid + ":RDP:" + config['username'] + "\n")
		f.write("drivestoredirect:s:*\n")
		f.close()
		
		cmd=[ 'start','temp\\launch.rdp' ]
		print >>sys.stderr, cmd
		if debug: print cmd
		subprocess.Popen(cmd,shell=True)
		printweb()
	else:
		print >>sys.stderr, "ERROR: This server is not supported"
		printweb()

def load_config():
	'''Dump config into a dictionary'''
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
	if not form.has_key('servername'):
		print "ERROR: no servername"
		printweb()
	else:
		servername = form['servername'].value

	if not form.has_key('wid'):
		print "ERROR: no wid"
	else:
		wid = form['wid'].value

	if not form.has_key('type'):
		print "ERROR: no type"
	else:
		type = form['type'].value

	if not form.has_key('p'):
		print "ERROR: no product"
	else:
		product = form['p'].value
		product = product.lower()
	if not form.has_key('u'):
		print "ERROR: no appuser"
	else:
		appuser = form['u'].value

	if not form.has_key('d'):
		print "ERROR: no appuser"
	else:
		domain = form['d'].value

	if not form.has_key('os'):
		print "ERROR: no os specified"
	else:
		serveros = form['os'].value
		
	config=load_config()
	launch(config,wid,servername,appuser,type,product,domain,serveros)


if __name__ == "__main__":
	main()
	