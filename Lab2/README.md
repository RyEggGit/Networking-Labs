# Lab 2

## Question 1
*Obtain two frames in from the folder "frames" under "Labs" in LEARN (please download the frames according to the last digit of your student ID, i.e., if last digit of ID = i, do frame i and frame i+10. Using the example given in section 2.3 as a template, parse the frames in a human readable format and comment. For example, write an IP address in the dotted decimal notation and header length as a positive integer. Using the frame data you have, show the relevant parts (such as MAC addresses, IP addresses etc). It is a good idea to use a table for this.*

Ethernet Header (Link Layer)

| Frame    | Desitionation Mac | Source Mac        | Type  | CRC  |
| -------- | ----------------- | ----------------- | ----- | ---- |
| Frame 8  | 00:15:60:f8:c6:00 | 00:22:19:f4:30:97 | IPv4  |  ??  |
| Frame 18 | 00:22:19:f4:30:9  | 00:1d:7e:46:ec:49 | IPv4  |  ??  |

IP Header (Network Layer)

| Frame    | Version | Header Length | Precedence |      | 
| -------- | ------- | ------------- | ---------- | ---- |
| Frame 8  |    4    |   20 bytes    |  routine   |      |
| Frame 18 |    4    |   20 bytes    |  routine   |      |

_TODO_


## Question 2
1. *Explain what the arp command does*
2. *Use the command /sbin/arp –a to see the ARP table of the machine on which you are logged in. Include the output of the command in your report and explain it.*

1. The arp command is used to view and manipulate the Address Resolution Protocol (ARP) cache on a computer. ARP is responsible for mapping IP addresses (logical addresses) to MAC addresses (physical addresses) on a local network.
2. The `$ arp -a` returns: 

`Laptop.mshome.net (172.22.240.1) at 00:15:5d:01:8b:b6 \[ether\] on eth0`

This shows my local IPv4 address (172.22.240.1) and the corresponding MAC address of my machine.
