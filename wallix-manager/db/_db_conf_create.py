#!/usr/bin/env python
# DB_connection strings

import sqlite3 as sql
import sys

debug=1


con = sql.connect('conf.db')
cur = con.cursor()    
cur.execute("CREATE TABLE Config(Suite_LinuxUser1 text, Suite_LinuxUser2 text, Suite_Win1User text, Suite_Win2User text,FX_LinuxUser1 text, FX_LinuxUser2 text, FX_Win1User text, FX_Win2User text,TRY_Win1User text, TRY_Win2User text,Swift1User text,Swift2User text,username text)")
