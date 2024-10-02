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

This returns the arp table for my device. We can see the connections to different computers: `Hostname` (`Ip Address`) at `MAC Address` [ether] on (`Information on ethernet, bus number and slot number`)


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
2. TODO


## Question 4
1. *Explain what the netstat utility does. Netstat is a big utility, so briefly explain its major functions*
2. *Use the command netstat -in. Change –in to –s to get some statistics. . Include some of the output in your report and explain it. Please do not include all of the output. Pick 3-4 interesting pieces of information to show. This is especially important for netstat -s, which will produce many lines of output.*
3. *Use the command netstat -r. Include the output in your report and explain it.*

1. Prints information about the networking of the system. You can specify the routes, groups, interfaces, masquerade and stastics and it will return the Active Internet connections,Recv-Q, Send-Q, Local Address, Local Address,Local Address, User,  PID/Program name, and Timer of the sockets on your machine.

2. Running `$ netstat -in` returns:

```
Kernel Interface table
Iface      MTU    RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
enp0s31f  1500 10406675040      0  56508 0      21950251857      0      0      0 BMRU
lo       65536 1065327218      0      0 0      1065327218      0      0      0 LRU
```
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

3. Running `$ netstat -r` returns:

```
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
default         v92-e2-rt-1782a 0.0.0.0         UG        0 0          0 enp0s31f6
129.97.92.0     0.0.0.0         255.255.255.0   U         0 0          0 enp0s31f6
link-local      0.0.0.0         255.255.0.0     U         0 0          0 enp0s31f6
```


## Question 5
1. `nslookup` is a utility to lookup information on different DNS's on the internet. 
2. Running `$ nslookup (server)` returns:
- For `ecebuntu.uwaterloo.ca` it return 6 different IPv4 address's, each the same except for the host address (likely the 6 different machines under eceubuntu?)
- For `www.mit.edu` it returns the canonical name (a mapping to the real endpoint like tinyurl) as well the IPv4 and 2 IPv6 addresses of the server
- For `www.gmail.com` it just returns the Ipv4 and Ipv6 of the server


## Question 6
1. `ping` sends a echo request to network hosts. 
2. 


## Question 7
1. Trace Route print's the route packets trace to different hosts

