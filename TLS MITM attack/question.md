## 1.0 Objective
Transport Layer Security, TLS, is one of the world’s most important forms of commercial
encryption. It is the public key system generally employed by e-commerce websites like
Amazon in order to prevent payment details from being intercepted by third parties.
The tool called “SSL strip” is an attack on TLS based around a man-in-the-middle
vulnerability where the system redirects people from the secure version of a webpage to an
unsecured one. By acting as a man-in-the-middle, the attacker can compromise any
information sent betwee
PAGE 2 OF 5
CS6823 - NETWORK SECURITY

## 1.2 Lab Setup and Background
The VLAB architecture for this attack is depicted in the diagram below:
The green box represents the VLAB environment that each student has an individual instance of.
There is a gateway (router) that connects the student VLAN to a second VLAN in which resides
the fakebook webserver that will be used in the attack.
Start up the following VMs in order: rtr (external router), Kali (the attacking machine), and XP
(the Windows XP victim).
The website to be attacked is inside the VLAB environment, and can be accessed at
<http://fakebook.vlab.local>. Startup IceWeasel on the Kali VM and ensure that you can
successfully get to the fakebook website.
NEWORK SECURITY 
PAGE 3 OF 5
CS6823 - NETWORK SECURITY
2.0 Perform Man- in- the-Middle Attack
Browse the fakebook webserver from the Kali machine using IceWeasel, and click “view
page source”.
Find and record the FORM statement for the login. This shows that although the page is not
secure, the actual login method uses a URL starting with https. Many websites use this
system (Facebook, Back of America, etc) in which a single page has both secure and
insecure items. That is the vulnerability we will exploit.
Make sure that the Kali machine has an IP address and that the default gateway is
pointed at the .1 address of the router (rtr).
Now on the Kali machine, we first have to setup up the machine to accept packets inbound
and forward them outbound and vice versa. This functionality can be modified in Linux by
performing the commands below. (The first of the two commands ensures that sudo applies
to the entire command, not just the echo statement. As a result, all commands performed in
the same terminal after this one will also be with root privileges.)
sudo su
echo "1" > /proc/sys/net/ipv4/ip_forward
Next we need to modify IPTables. IPTables is a firewalling application available in Linux
distributions. We will be covering IPTables in more detail later in the course. For now,
understand that IPtables is taking traffic coming inbound to the Kali machine which is
destined to port 80 (HTTP Web) and redirecting only that traffic to the SSLStrip application
which in turn is listening on port 8080.
iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j
REDIRECT --to-port 8080
Note: These changes are lost after a reboot.
Finally we need to perform an ARP spoofing attack on client machine. Write a SCAPY program
that sends gratuitous ARP messages from Kali to both the Windows XP machine and the router
(rtr). The gratuitous ARPs sent to the Windows XP changes the entry for the MAC address for rtr
to that of Kali’s MAC address (making the Windows XP machine think that Kali is actually the
router), while the gratuitous ARPs sent to the router changes the entry for the MAC address of the
Windows XP address that of Kali’s MAC address (making the rtr think that the Kali is actually
the Windows XP machine). The Python script may need sudo to run properly. Use the arp
command on each to show that the IP-MAC association has been changed on each.
NEWORK SECURITY 
PAGE 4 OF 5
CS6823 - NETWORK SECURITY

## 2.1 SSLstrip Attack
SSLstrip can be found in the directory /usr/share/sslstrip. Run SSLstrip on the
Kali machine. To do this use the command:
sudo python sslstrip.py -l 8080
This starts sslstrip with it listening on port 8080 of the Kali machine.
Go back to the victim machine and browse back to the webserver (use Internet
Explorer). Again go to “view source” in the web browser. Look for the FORM
method. Record the new FORM post method and explain what is different. (If
nothing is different, you may need to do a hard refresh in the browser.)
From the victim machine, login to the webserver using the credentials
username: memon
password: evilproffy
Now go back to the Kali machine. Open a new terminal window and find the sslstrip log file
“sslstrip.log”
