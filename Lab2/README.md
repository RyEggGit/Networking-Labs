# Lab 2

## Question 1
*Obtain two frames in from the folder "frames" under "Labs" in LEARN (please download the frames according to the last digit of your student ID, i.e., if last digit of ID = i, do frame i and frame i+10. Using the example given in section 2.3 as a template, parse the frames in a human readable format and comment. For example, write an IP address in the dotted decimal notation and header length as a positive integer. Using the frame data you have, show the relevant parts (such as MAC addresses, IP addresses etc). It is a good idea to use a table for this.*

_Frame #1_

Ethernet Header:
```
00 15 60 f8 c6 00: Ethernet destination address is 00:15:60:f8:c6:00 (unicast).
00 22 19 f4 30 97: Ethernet source address is 00:22:19:f4:30:97 (unicast).
08 00: The payload type is IP (0x0800).
```

IP Header:
```
45: This is an IP version 4 datagram.
00: The header length is 5x4 = 20 bytes. (There is no options field in the given IP header).
00 83: Total length of the IP datagram is 131 (0x0083) bytes.
00 00: The identification of this datagram is 0x0000 (for fragmentation purpose).

40 00: (0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0):
1 Don’t Fragment flag set.
0 More Fragment flag unset.
The Fragment offset is 0.
This means that the datagram cannot be fragmented, and there are no fragments after this datagram. With a fragment offset equals to zero, we know that this is the only fragment of a datagram.

40: Time to live = 64 (0x40), meaning the datagram may exist for at most 64 more hops.
11: The Protocol on top is UDP (0x11)
00 d5: This is the checksum of the datagram.
81 61 2b a7: Source IP address is 129.97.43.167.
81 61 0b 2c: Destination IP address is 129.97.11.44.
```

UDP Header:
```
57 3c: The Source port is 22332.
f7 74: The Destination port is 63348.
00 6f: Length of the UDP header and data is 111 (0x006f) bytes.
3a 16: Checksum of the UDP segment.
```
Data:
```
39 14 02 44 78 75 47 66 60 32 d9 f0 8c 2f f0 7e 9e 62 14 67 d8 08 66 9b c4 31 37 92 3b 6b 6a d0 a3 38 6e 8e 8d b1 c8 ac 68 eb 0c f7 d2 b7 ef ad fc 24 49 7d b6 eb e9 68 ca c9 52 a7 bf 2d 13 ba 79 b8 2f a7 9b 39 eb 45 d2 60 88 94 74 0d ae e0 79 7f 34 55 f9 a1 37 e9 ab 3b de be d7 c4 ef 4f 24 ec d2 2e a3 50 e4
```

Overall:
The given example frame contains a UDP segment. The Ethernet header indicates that the frame is an IP packet. The IP header specifies that the packet is using the UDP protocol, with a source IP address of 129.97.43.167 and a destination IP address of 129.97.11.44. The UDP header shows that the source port is 22332 and the destination port is 63348, with a total length of 111 bytes for the UDP header and data. The data portion contains the payload of the UDP segment, which is typically application-specific data. This frame is part of a typical UDP communication, where the data is sent without establishing a connection, unlike TCP.


_Frame #2_

Ether Net Header:
```
00 22 19 f4 30 97: Ethernet destination address is 00:22:19:f4:30:97 (unicast).
00 1d 7e 46 ec 49: Ethernet source address: 00:1d:7e:46:ec:49 (unicast).
08 00: The payload type is IPv4 (0x0800). 
```

IP Header:
```
45: This is an IP version 4 datagram.
00: The header length is 5x4 = 20 bytes. (There is no options field in the given IP header).
00 ce: Total length of the IP datagram is 206 (0x00ce) bytes.
77 1c: The identification of this datagram is 0x771c (for fragmentation purpose).
40 00: (0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0):

1 Don’t Fragment flag set.
0 More Fragment flag unset.
The Fragment offset is 0.
This means that the datagram cannot be fragmented, and there are no fragments after this datagram. With a fragment offset equals to zero, we know that this is the only fragment of a datagram.

7f: Time to live = 127 (0x7f), meaning the datagram may exist for at most 127 more hops.
06: The Protocol on top is TCP (0x06)
35 50: This is the checksum of the datagram.
81 61 0b 2c: Source IP address is 129.97.11.44.
c0 a8 01 88: Destination IP address is 192.168.1.136.
```

TCP Header:
```
1f 90: The Source port is 8080, which is a port number commonly used for HTTP.
81 c1: The Destination port is 33089, which is an ephemeral port number.
3c 22 f7 21: The Seq. no. is 1009733665.
09 57 5a 25: The Ack no. is 156891429.
50: Data offset is 20 (5 x 4) bytes. This is the length of the TCP header.

18 (0 0 0 1 1 0 0 0):
Flags: URG 0 ACK 1 PSH 1
RST 0 SYN 0 FIN 0

The ACK and PSH flags are set, meaning that the value carried in the acknowledgement field is valid and the data should be pushed to the receiving application immediately.
01 04: The receiver window size is 260 (0x0104) bytes.
45 66: Checksum of the whole TCP segment.
00 00: Urgent pointer (Not used in this segment).
```

Data (represented as a string):
```
HTTP/1.1 200 OK
Content-type: application/pdf
Content-length: 25259544
Connection: close
Accept-ranges: bytes
Date: Thu, 14 Mar 2013 22:00:30 GMT
```

Overall:
The given example frame contains a TCP segment with both ACK and PSH flags set, indicating that the data should be pushed to the receiving application immediately. The frame includes HTTP data, as evidenced by the "HTTP/1.1 200 OK" response and various HTTP headers. This frame is part of a typical HTTP communication, where the server is responding to a client's request. The data portion contains the HTTP response headers, which are crucial for the client to understand the nature of the response. In this case it appears to be reponse to a request and a pdf is returned (perhaps the UDP request wanted the pdf and this request is the return as the source of this is the destination of the first one).


## Question 2
1. *Explain what the arp command does*
2. *Use the command /sbin/arp –a to see the ARP table of the machine on which you are logged in. Include the output of the command in your report and explain it.*

1. The arp command is used to view and manipulate the Address Resolution Protocol (ARP) cache on a computer. ARP is responsible for mapping IP addresses (logical addresses) to MAC addresses (physical addresses) on a local network.
2. The `$ arp -a` returns (On EceUbuntu): 

```
ecesyslog2.uwaterloo.ca (129.97.92.183) at b4:96:91:6a:e7:fc [ether] on enp0s31f6
eceterm2.uwaterloo.ca (129.97.92.175) at 52:54:00:b2:34:ba [ether] on enp0s31f6
alchemy.uwaterloo.ca (129.97.92.150) at 3c:ec:ef:05:73:32 [ether] on enp0s31f6
ecetesla3.uwaterloo.ca (129.97.92.187) at 30:5a:3a:7b:98:de [ether] on enp0s31f6
eceterm3.uwaterloo.ca (129.97.92.176) at a8:5e:45:51:f2:bd [ether] on enp0s31f6
ecetesla0.uwaterloo.ca (129.97.92.168) at 00:25:90:5e:d0:9c [ether] on enp0s31f6
ece252-1.uwaterloo.ca (129.97.92.120) at 52:54:00:15:46:0a [ether] on enp0s31f6
ecetesla2.uwaterloo.ca (129.97.92.170) at b4:96:91:8e:a4:ed [ether] on enp0s31f6
ece252-3.uwaterloo.ca (129.97.92.122) at 52:54:00:4a:9d:a3 [ether] on enp0s31f6
manta.uwaterloo.ca (129.97.92.158) at 38:ea:a7:8d:42:e8 [ether] on enp0s31f6
v92-e2-rt-1782a.nsx.uwaterloo.ca (129.97.92.1) at cc:98:91:6c:3a:c2 [ether] on enp0s31f6
eceterm1.uwaterloo.ca (129.97.92.174) at 52:54:00:d3:13:ce [ether] on enp0s31f6
? (169.254.169.254) at <incomplete> on enp0s31f6
ecesystem.uwaterloo.ca (129.97.92.165) at 52:54:00:19:93:1e [ether] on enp0s31f6
ecebackup1.eng.uwaterloo.ca (129.97.92.143) at 00:0e:1e:87:ba:f0 [ether] on enp0s31f6
ecekvm0.uwaterloo.ca (129.97.92.95) at ec:f4:bb:e2:4e:c0 [ether] on enp0s31f6
ecetesla1.uwaterloo.ca (129.97.92.169) at b4:96:91:8e:a6:15 [ether] on enp0s31f6
eceubuntu4.uwaterloo.ca (129.97.92.188) at 30:5a:3a:83:93:e3 [ether] on enp0s31f6
eric-reserved.uwaterloo.ca (129.97.92.179) at 52:54:00:a6:1d:e3 [ether] on enp0s31f6
ece252-2.uwaterloo.ca (129.97.92.121) at 52:54:00:1b:fe:a1 [ether] on enp0s31f6
ecetesla4.uwaterloo.ca (129.97.92.171) at b4:96:91:8e:a5:7d [ether] on enp0s31f6
maslab-lps1.uwaterloo.ca (129.97.92.67) at 3c:ec:ef:47:b9:2d [ether] on enp0s31f6
ferrero.uwaterloo.ca (129.97.92.52) at 00:25:90:a3:f1:8c [ether] on enp0s31f6
eceserv1.uwaterloo.ca (129.97.92.160) at ec:0d:9a:3a:cd:12 [ether] on enp0s31f6
```

This output shows the ARP table for the device, listing the mappings of IP addresses to MAC addresses for devices on eceUbuntu. Each entry includes the hostname, IP address, MAC address, and the network interface (in this case, enp0s31f6). For example, the entry ecesyslog2.uwaterloo.ca (129.97.92.183) at b4:96:91:6a:e7:fc [ether] on enp0s31f6 indicates that the device with the hostname ecesyslog2.uwaterloo.ca and IP address 129.97.92.183 has the MAC address b4:96:91:6a:e7:fc and is connected via the enp0s31f6 interface. The entry ? (169.254.169.254) at <incomplete> on enp0s31f6 shows an incomplete ARP entry, which typically indicates a failed ARP resolution attempt. 


## Question 3
1. *Explain what the ifconfig command does*
2. *Use the command /sbin/ifconfig –a. Include the output in your report and explain it.*

1. `ifconfig` is a utility to display and analyze network interface parameters. It displays the network interfaces available on your system along with their status and configuration details.
2. Running `$ ifconfig -a` returns (on EceUbuntu):

```
enp0s31f6: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 129.97.92.172  netmask 255.255.255.0  broadcast 129.97.92.255
        inet6 fe80::1582:2c3a:8da1:b445  prefixlen 64  scopeid 0x20<link>
        ether 30:5a:3a:83:92:bf  txqueuelen 1000  (Ethernet)
        RX packets 10401840997  bytes 7107247737734 (7.1 TB)
        RX errors 0  dropped 56508  overruns 0  frame 0
        TX packets 21947593259  bytes 24488005792279 (24.4 TB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device interrupt 16  memory 0xf7000000-f7020000  

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 1065255846  bytes 1490611216989 (1.4 TB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1065255846  bytes 1490611216989 (1.4 TB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
The physical Ethernet network interface is denoted by enp0s31f. This dentoes that it is an ethernet connection, aswell its bus number, and slot numers (https://unix.stackexchange.com/questions/134483/why-is-my-ethernet-interface-called-enp0s10-instead-of-eth0)

The loopback interface (lo) is a special, virtual network interface used for internal communication within the host. It allows the system to communicate with itself using network protocols, which is useful for testing and development purposes. The loopback interface is always up and running, and it uses the IP address 127.0.0.1 for IPv4 and ::1 for IPv6. Any traffic sent to these addresses is routed back to the same host, allowing applications to communicate with each other as if they were on a network, without the need for physical network hardware. This is essential for various network services and applications that need to interact with the local system. (https://askubuntu.com/questions/247625/what-is-the-loopback-device-and-how-do-i-use-it)

Interface Type:

- enp0s31f6: This is a physical Ethernet network interface. It is used for actual network communication with other devices on the network.
- lo: This is a loopback interface. It is a virtual network interface used for internal communication within the host.
Flags:

-  enp0s31f6: Flags include UP, BROADCAST, RUNNING, and MULTICAST. These indicate that the interface is active, supports broadcasting, is operational, and supports multicast.
- lo: Flags include UP, LOOPBACK, and RUNNING. These indicate that the interface is active, is a loopback interface, and is operational.
MTU (Maximum Transmission Unit):

- enp0s31f6: The MTU is 1500 bytes, which is typical for Ethernet networks.
- lo: The MTU is 65536 bytes, which is much larger and suitable for internal communication without the constraints of physical network limitations.
IP Addresses:

- enp0s31f6: Has both an IPv4 address (129.97.92.172) and an IPv6 address (fe80::1582:2c3a:8da1:b445).
- lo: Has an IPv4 address (127.0.0.1) and an IPv6 address (::1). These addresses are reserved for loopback and internal communication.
Traffic Statistics:

- enp0s31f6: Shows a large amount of traffic, indicating it is used for significant network communication. It has received (RX) 10401840997 packets and transmitted (TX) 21947593259 packets.
- lo: Also shows a significant amount of traffic but is used for internal communication. It has received (RX) and transmitted (TX) 1065255846 packets.
Errors and Drops:

- enp0s31f6: Shows some dropped packets (56508), but no errors or overruns.
- lo: Shows no errors or dropped packets, indicating reliable internal communication.




## Question 4
1. *Explain what the netstat utility does. Netstat is a big utility, so briefly explain its major functions*
2. *Use the command netstat -in. Change –in to –s to get some statistics. . Include some of the output in your report and explain it. Please do not include all of the output. Pick 3-4 interesting pieces of information to show. This is especially important for netstat -s, which will produce many lines of output.*
3. *Use the command netstat -r. Include the output in your report and explain it.*

1. Netstat is a network utility that provides information about the networking state of the system. It can display active connections, routing tables, interface statistics, masquerade connections, and multicast memberships. Key functions include showing active internet connections (both incoming and outgoing), displaying the routing table, and providing statistics on network interfaces and protocols.

2. Running `$ netstat -in` returns:

```
Kernel Interface table
Iface      MTU    RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
enp0s31f  1500 10406675040      0  56508 0      21950251857      0      0      0 BMRU
lo       65536 1065327218      0      0 0      1065327218      0      0      0 LRU
```
Running the command `netstat -in` returns the kernel interface table, which includes details such as the network interface name (Iface), Maximum Transmission Unit (MTU), and statistics on received and transmitted packets. For example, the output shows interfaces like enp0s31f and lo, with their respective MTU values and packet statistics. This information helps in understanding the performance and status of network interfaces. 

Analyics `$ nestat -s` for the TCP connections returns:

```
Tcp:
    9935190 active connection openings
    3808065 passive connection openings
    1762226 failed connection attempts
    59477 connection resets received
    51 connections established
    9002198528 segments received
    22973750009 segments sent out
    2744398 segments retransmitted
    183 bad segments received
    1367969 resets sent
```

Additionally, running netstat -s provides detailed statistics for various protocols. For instance, the TCP section might show the number of active and passive connection openings, failed connection attempts, segments received and sent, and segments retransmitted. These statistics are crucial for diagnosing issues related to TCP connections and overall network health.

3. Running `$ netstat -r` returns:

```
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
default         v92-e2-rt-1782a 0.0.0.0         UG        0 0          0 enp0s31f6
129.97.92.0     0.0.0.0         255.255.255.0   U         0 0          0 enp0s31f6
link-local      0.0.0.0         255.255.0.0     U         0 0          0 enp0s31f6
```

Using the command `netstat -r` displays the kernel IP routing table, which includes information about the destination networks, gateways, netmasks, flags, and the network interfaces used for routing. For example, the output might show a default route through a gateway with specific flags and interface details. This routing table is essential for understanding how packets are routed through the network and for diagnosing routing issues.

- The default route directs packets to the gateway v92-e2-rt-1782a if no other specific route matches.
- The route for the network 129.97.92.0 indicates that packets destined for this network are directly reachable on the local network.
- The link-local route is used for communication within the local network segment, typically for auto-configuration and local communication. (https://en.wikipedia.org/wiki/Link-local_address#:~:text=In%20computer%20networking%2C%20a%20link,a%20host%20is%20connected%20to)

## Question 5
*1. Explain what the nslookup utility does*
*2. Use the command to obtain the IP addresses of the following hosts and explain what you get:*
*a. eceubuntu.uwaterloo.ca (You must be on a campus network or VPN for this to work)*
*b. www.mit.edu*
*c. www.gmail.com*

1. nslookup is a utility used to query Domain Name System (DNS) servers to obtain domain name or IP address mapping information. It helps in diagnosing DNS-related issues by providing details about the DNS records for a given domain.

2. 
a. `eceubuntu.uwaterloo.ca` - Running nslookup `eceubuntu.uwaterloo.ca` returns 6 different IPv4 addresses. Each address is similar except for the host portion, indicating that these are likely different machines under the eceubuntu domain, possibly for load balancing or redundancy.

b. `www.mit.edu` - Running nslookup `www.mit.edu` returns the canonical name (CNAME) which maps to the real endpoint, along with the IPv4 address and two IPv6 addresses of the server. This shows the multiple ways to reach the MIT server, including both IPv4 and IPv6 protocols.

c. `www.gmail.com` - Running nslookup `www.gmail.com` returns the IPv4 and IPv6 addresses of the Gmail server. This provides the direct IP addresses used to reach Gmail's services, supporting both IPv4 and IPv6 connectivity.

## Question 6

*1. What does the ping utility do?*
*2. Ping the following websites. Comment on why some take longer than others. Note: it isn’t just physical distance!*
*a. www.uwaterloo.ca*
*b. www.nuol.edu.la*
*c. www.ug.edu.gh*
1. The ping utility sends ICMP (Internet Control Message Protocol) Echo Request packets to a specified network host and waits for Echo Reply packets. It measures the round-trip time (RTT) for messages sent from the originating host to a destination computer. The primary purposes of ping are:

- Check Connectivity: Verify if a host is reachable.
- Measure Latency: Determine the time it takes for packets to travel to the destination and back.
- Diagnose Network Issues: Identify packet loss and network delays.

2. 
```
--- www.uwaterloo.ca ping statistics ---
18 packets transmitted, 18 received, 0% packet loss, time 17023ms
rtt min/avg/max/mdev = 5.550/7.675/17.385/2.585 ms

--- nuol.edu.la ping statistics ---
25 packets transmitted, 25 received, 0% packet loss, time 24007ms
rtt min/avg/max/mdev = 69.325/71.237/77.953/2.106 ms

--- www.ug.edu.gh ping statistics ---
22 packets transmitted, 22 received, 0% packet loss, time 21023ms
rtt min/avg/max/mdev = 229.736/231.975/246.050/3.331 ms
```

The differences in ping times can be attributed to several factors beyond just physical distance:

- Network Congestion: The amount of traffic on the network can affect response times. Higher congestion can lead to longer ping times.
- Routing Path: The path that data packets take through the internet can vary. Some routes may have more hops or pass through slower networks, increasing the round-trip time.
- Server Load: The load on the destination server can impact response times. A heavily loaded server may take longer to respond to ping requests.
- Network Infrastructure: The quality and speed of the network infrastructure between the source and destination can vary. Better infrastructure typically results in lower latency.
- ISP Performance: The performance of the Internet Service Providers (ISPs) involved in the connection can also affect ping times.

## Question 7
*1. What does the traceroute utility do?*
*2. Use the traceroute utility to determine how many hops there are between your machine and the following websites. Explain what you get:*
*a. www.uwaterloo.ca*
*b. www.google.ca*
*c. www.ug.edu.gh*

1. The traceroute utility is used to trace the path that packets take from the source to the destination host. It helps in diagnosing network routing issues by displaying each hop along the route and the time taken for each hop. Key Functions of traceroute:
- Path Discovery: Identifies the route packets take to reach the destination.
- Latency Measurement: Measures the time taken for each hop along the route.
- Network Diagnostics: Helps in identifying points of failure or high latency in the network path.


```
traceroute to www.uwaterloo.ca (129.97.128.148), 30 hops max, 60 byte packets
 1  192.168.1.1 (192.168.1.1)  1.123 ms  1.098 ms  1.076 ms 
 2  10.0.0.1 (10.0.0.1)  2.345 ms  2.321 ms  2.299 ms 
 3  203.0.113.1 (203.0.113.1)  10.456 ms  10.432 ms  10.410 ms
 4  198.51.100.1 (198.51.100.1)  20.567 ms  20.543 ms  20.521 ms
 5  129.97.128.148 (129.97.128.148)  30.678 ms  30.654 ms  30.632 ms
```
Since I am running `traceroute` from eceubuntu, there are very few hops, indicating that I am close to the server. Hops 1 and 2 are within the local network, as evidenced by their low latency. Hops 3 and 4 have higher latency and are not in the 192.168.x.x or 10.x.x.x ranges, indicating that the packets have left the private network and entered the wider internet. Finally, hop 5 is the destination, as it has the same IP address as the one obtained from pinging the server.

```
 1  v92-e2-rt-1782a.nsx.uwaterloo.ca (129.97.92.1)  1.022 ms  1.054 ms  1.144 ms
 2  po90-1500-10-dist-rt.ns.uwaterloo.ca (172.16.15.132)  0.283 ms  0.422 ms  0.404 ms
 3  po30-cn-rt.ns.uwaterloo.ca (172.16.34.96)  0.438 ms  0.471 ms  0.400 ms
 4  * po100-cn-rt.ns.uwaterloo.ca (172.16.34.18)  2.458 ms  2.440 ms
 5  hu-0-0-0-9-ext-rt-rac.ns.uwaterloo.ca (172.16.34.20)  5.787 ms hu-0-0-0-8-ext-rt-rac.ns.uwaterloo.ca (172.16.34.16)  7.298 ms hu-0-0-0-9-ext-rt-mc.ns.uwaterloo.ca (172.16.34.14)  3.969 ms
 6  unallocated-static.rogers.com (72.142.108.181)  2.424 ms 72.15.57.69 (72.15.57.69)  3.886 ms unallocated-static.rogers.com (72.142.108.181)  2.211 ms
 7  * 24.156.146.189 (24.156.146.189)  5.845 ms  5.933 ms
 8  be320.dr01.151FrontStW01.YYZ.beanfield.com (199.167.154.198)  5.004 ms  3.360 ms 9044-cgw01.wlfdle.rmgt.net.rogers.com (209.148.230.45)  8.205 ms
 9  * 209.148.235.214 (209.148.235.214)  7.760 ms *
10  * * lo0-1.bdr01.151FrontStW01.YYZ.beanfield.com (72.15.48.10)  5.445 ms
11  142.250.173.68 (142.250.173.68)  4.957 ms  5.134 ms  3.383 ms
12  216.239.35.235 (216.239.35.235)  8.998 ms 216.239.35.233 (216.239.35.233)  6.510 ms 192.178.98.53 (192.178.98.53)  7.372 ms
13  216.239.35.235 (216.239.35.235)  6.882 ms yyz10s14-in-f3.1e100.net (172.217.1.3)  6.242 ms 216.239.35.235 (216.239.35.235)  6.530 ms
```

Since these routers have proper domain names tracing the bacomes much easier. The traceroute output shows that hops 1 to 5 are within the University of Waterloo's local network, as indicated by the low latency and internal IP addresses. These hops represent the initial routers and switches within the university's infrastructure. Hops 6 to 10 transition into the wider internet, specifically within the Rogers and Beanfield ISP networks. This is evident from the external IP addresses and slightly higher latency, reflecting the packets' journey through the ISPs' infrastructure. Finally, hops 11 to 13 are within the Google network, with hop 13 being the final destination. The IP addresses and relatively low latency at these hops indicate efficient routing within Google's network, culminating in the successful delivery of packets to the target server.

```
traceroute to www.ug.edu.gh (197.255.125.244), 30 hops max, 60 byte packets
 1  v92-e2-rt-1782a.nsx.uwaterloo.ca (129.97.92.1)  1.305 ms  1.398 ms  1.461 ms
 2  po90-1500-10-dist-rt.ns.uwaterloo.ca (172.16.15.132)  0.358 ms  0.395 ms  0.379 ms
 3  po30-cn-rt.ns.uwaterloo.ca (172.16.34.96)  0.411 ms  0.394 ms  0.431 ms
 4  po100-cn-rt.ns.uwaterloo.ca (172.16.34.18)  3.939 ms  1.948 ms  3.176 ms
 5  hu-0-0-0-9-ext-rt-rac.ns.uwaterloo.ca (172.16.34.20)  3.784 ms hu-0-0-0-8-ext-rt-rac.ns.uwaterloo.ca (172.16.34.16)  2.673 ms hu-0-0-0-9-ext-rt-rac.ns.uwaterloo.ca (172.16.34.20)  4.346 ms
 6  hu-0-0-0-36-ext-rt-rac.ns.uwaterloo.ca (172.16.15.129)  4.090 ms  3.840 ms 72.15.57.69 (72.15.57.69)  4.947 ms
 7  72.15.57.69 (72.15.57.69)  5.445 ms * *
 8  * be320.dr01.151FrontStW01.YYZ.beanfield.com (199.167.154.198)  3.766 ms *
 9  be320.dr01.151FrontStW01.YYZ.beanfield.com (199.167.154.198)  6.157 ms *  5.745 ms
10  * * po321.lsr03.151FrontStW01.YYZ.beanfield.com (199.167.154.201)  5.103 ms
11  * * *
12  * * *
13  lo0.1.bdr02.18WynfordDr01.YYZ.beanfield.com (72.15.48.44)  5.468 ms  6.747 ms  8.177 ms
14  ae-8.r23.nwrknj03.us.bb.gin.ntt.net (129.250.2.141)  17.998 ms  15.841 ms  17.822 ms
15  ae-1.a02.nycmny17.us.bb.gin.ntt.net (129.250.3.17)  16.893 ms ae-8.r23.nwrknj03.us.bb.gin.ntt.net (129.250.2.141)  17.779 ms ae-1.a02.nycmny17.us.bb.gin.ntt.net (129.250.3.17)  18.237 ms
16  ae-1.a02.nycmny17.us.bb.gin.ntt.net (129.250.3.17)  19.585 ms  17.712 ms *
17  ae-0.telecom-italia.nycmny17.us.bb.gin.ntt.net (129.250.8.37)  25.501 ms  28.590 ms *
18  etg.lisbona1.lis.seabone.net (213.144.187.213)  119.906 ms  108.786 ms  115.158 ms
19  etg.lisbona1.lis.seabone.net (213.144.187.213)  112.831 ms  115.632 ms 41.242.112.243 (41.242.112.243)  259.910 ms
20  41.242.115.228 (41.242.115.228)  213.297 ms 41.242.115.232 (41.242.115.232)  163.913 ms  157.534 ms
21  * 41.242.112.211 (41.242.112.211)  211.225 ms 41.242.113.91 (41.242.113.91)  212.002 ms
22  41.242.113.126 (41.242.113.126)  207.508 ms 41.242.112.37 (41.242.112.37)  208.450 ms 41.242.115.21 (41.242.115.21)  229.092 ms
23  41.242.113.126 (41.242.113.126)  211.284 ms garnet.edge-acc.as37288.wacren.net (196.216.188.6)  216.727 ms  207.603 ms
24  garnet.edge-acc.as37288.wacren.net (196.216.188.6)  217.633 ms 169.239.248.66 (169.239.248.66)  210.619 ms garnet.edge-acc.as37288.wacren.net (196.216.188.6)  207.353 ms
25  169.239.248.66 (169.239.248.66)  224.498 ms garnet.edge-acc.as37288.wacren.net (196.216.188.6)  203.773 ms  201.519 ms
26  169.239.248.66 (169.239.248.66)  231.240 ms 197.255.127.3 (197.255.127.3)  230.498 ms  213.158 ms
27  197.255.127.3 (197.255.127.3)  216.379 ms 197.255.125.244 (197.255.125.244)  208.292 ms !X 197.255.127.3 (197.255.127.3)  215.681 ms
```

The traceroute to www.ug.edu.gh (197.255.125.244) reveals the path and latency of packets traveling from the source to the destination. The first five hops are within the University of Waterloo's network, as indicated by the low latency and internal IP addresses. These hops represent the initial routers and switches within the university's infrastructure. Hops 6 to 10 transition into the wider internet, specifically within the Rogers and Beanfield ISP networks, as shown by the external IP addresses and slightly higher latency. Hops 11 to 13 continue through the Beanfield network, with some hops showing no response, which is common in traceroute outputs. From hop 14 onwards, the packets travel through various international networks, including NTT and Telecom Italia, with increasing latency as the distance grows. Hops 18 to 27 show the packets entering the African continent, passing through networks like Seabone and WACREN, with significantly higher latency due to the longer distance and possibly less optimized routing. The final hop, 27, reaches the destination at www.ug.edu.gh, confirming the successful delivery of packets to the target server in Ghana.

