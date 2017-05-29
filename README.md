# wallix-session-manager

Wallix is a managed bastion appliance which can audit all user activity to security sensitive servers.  It has the ability to record user sessions and perform advanced keylogging not to mention others.

I created this tool in Python to help manage accessing servers via wallix due to the complicated launch strings which must be supplied to walllix so it knows what you want to access and if you are permitted. This tool is a simple local web frontend application and Its main purpose is to:

1) Manager connection strings and launch sessions to servers via wallix (ssh, sftp and rdp).

2) Provide simple offline mechanism so it can be copied to multiple locations and not need the source or on-line DB to function (this is achieved by replicating an on-line database to a local sqlite DB).

3) Remove the need to maintain complex launch strings which are bespoke to each server and each user.

4) Make it easy to copy this app to other machines so all team members can set it up and use quickly.


Limitations:

1) Its designed to run on windows desktops as this was corporate policy so there was no need to support anything else.

2) /bin - has been emptied, it should hold a copy of putty.exe and winscp.exe to provide ssh and sftp functionality.

3) Its not designed to be run from a central webserver so its limited to localhost access only. It needs to be local so it can launch whatever tool is required to connect to the server.  Localhost will also provide some much needed security.

4) This tool will not save passwords.  It was designed to manage connections only, so all authentications must be validated (ssh key or manual entry).


More information to follow
 
