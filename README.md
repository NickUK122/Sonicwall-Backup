# Sonicwall-Backup
Backup your Sonicwalls to FTP

* - SSH Needs to be enabled on the Sonicwall
* - Lock SSH down to your IP (Address Object)

----
Recommend - 
 - Create a file called ~/.ssh/config
 - nano ~/.ssh/config
 - Add single line StrictHostKeyChecking no

This is to get around SSH wanting to approve the fingerprint on SSH Connections.
