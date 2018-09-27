#!/usr/bin/python
import pexpect, time

#List all your Sonicwalls here
firewalls = (
	    ('IPHERE','USERNAME', 'PASSWORD', 'NAME'),
        ('IPHERE','USERNAME', 'PASSWORD', 'NAME'),
        ('IPHERE','USERNAME', 'PASSWORD', 'NAME'),
)

#FTP Server you're sending the config to
FTP_Server = "Enter IP/Hostname"
FTP_User = "ENTER USERNAME"
FTP_Password = "ENTER PASSWORD"
FTP_Protocol = "ftp" #FTP

#Running the backup.
def ssh(host, username, password, name):
 sshc = pexpect.spawn('sshpass -p ' + password + ' ssh ' + username + '@' + host)
 print 'Logging into SonicWall.'
 dt = time.strftime('%Y%m%d')
 sshc.sendline('export current-config exp ftp ' + FTP_Protocol + '://' + FTP_User + ':' + FTP_Password + '@' + FTP_Server + '/export_' + name + '_' + dt + '.exp')
 time.sleep(5)
 print 'config dumped & copied from ' + name
 print 'Logging out of ' + name
 sshc.close()
 print 'Connected Closed to ' + name
 print 'Backup Saved As export_' + name + '_' + dt + '.exp'
 time.sleep(2)

#SonicWall Array
for i in range(0,len(firewalls)):
	print 'Backing up ' + firewalls[i][3]
	ssh(firewalls[i][0], firewalls[i][1],firewalls[i][2],firewalls[i][3])
	print 'Finished Backing up ' + firewalls[i][3]


    
