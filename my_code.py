
from scapy.all import *

sniff(filter="port 80", count=100)

for packet in packets:
    if packet.haslayer(TCP) and packet[TCP].sport == 80:
        if packet.haslayer(HTTP):
            print(packet.show())

