from scapy.config import conf
conf.ipv6_enabled = False
from scapy.all import *
import sys

# get path of pcap file
h3 = sys.argv[1] 
h4 = sys.argv[2]
Uh3 = sys.argv[3]
Uh4 = sys.argv[4]

# read pcap
packetsT3 = rdpcap(h3) 
packetsT4 = rdpcap(h4)
packetsU3 = rdpcap(Uh3)
packetsU4 = rdpcap(Uh4)

count = 0
Tsize_1 = 0

Tstart_1 = 0

Tend_1 = 0


Tstart_1 = packetsT3[TCP][0].time
for packet in packetsT3[TCP]:
    if packetsT3[TCP][count][2].dport == 7777 :
        Tend_1 = packetsT3[TCP][count].time
        Tsize_1 += len(packetsT3[TCP][count])
    count+=1

m=0
Tstart_3 = 0
Tend_3 = 0
Tsize_3 = 0
Tstart_3 = packetsT4[TCP][0].time
for packet in packetsT4[TCP]:
    if packetsT4[TCP][m][2].dport == 7777:
        Tend_3 = packetsT4[TCP][m].time
        Tsize_3 += len(packetsT4[TCP][m])
    m+=1
              
print("---TCP---")
print("Flow1(h2-->h3): ", (Tsize_1)/(Tend_1-Tstart_1)*8/1000000, "Mbps")
print("Flow2(h1-->h4): ",(Tsize_3)/(Tend_3-Tstart_3)*8/1000000, "Mbps")



u_count = 0
Usize_1 = 0

Ustart_1 = 0

Uend_1 = 0

Ustart_1 = packetsU3[UDP][0].time

for packet in packetsU3[UDP]:
    if packetsU3[UDP][u_count][2].dport == 7777 :
        Uend_1 = packetsU3[UDP][u_count].time
        Usize_1 += len(packetsU3[UDP][u_count])
    u_count+=1

i=0
Ustart_3 = 0
Uend_3 = 0
Usize_3 = 0
Ustart_3 = packetsU4[UDP][0].time
for packet in packetsU4[UDP]:
    if packetsU4[UDP][i][2].dport == 7777:
      Uend_3 = packetsU4[UDP][i].time
      Usize_3 += len(packetsU4[UDP][i])
    i+=1
print("---UDP---")
print("Flow1(h2->h3): ", (Usize_1)/(Uend_1-Ustart_1)*8/1000000, "Mbps")
print("Flow2(h1->h4): ",(Usize_3)/(Uend_3-Ustart_3)*8/1000000, "Mbps")
