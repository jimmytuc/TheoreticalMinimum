# The Transport and Application Layers

* __Transport Layer__ the layer of the TCP/IP Model that allows traffic to be directed to specific network applications
* __Application Layer__ the layer of the TCP/IP Model that allows these applications to communicate in a way they understand

## The Transport Layer

* A __port__ is a 16-bit number that's used to direct traffic to specific services running on a networked computer
* Ports are normally denoted with a colon after the IP address (at least in IPv4)
    * Example, given an IP address of 192.168.0.1 and a port number of 80, we have 192.168.0.1:80
    * Written this way, it's known as a __socket address__ or __socket number__
    
### Dissection of a TCP Segment

* A __TCP Segment__ is made up of a TCP header and a data section

![tcp segment](../assets/course2_tcpsegment.png)

* The __destination port__ is the port the service the traffic is intended for
* The __source port__ is a high-numbered port chosen from a special section of ports known as ephemeral ports
* __Sequence number:__ is a 32-bit number that's used to keep track of where in a sequence of TCP segments this one is expected to be
* __Acknowledgement number:__ the number of the next expected segment
* __Data offset field:__ a 4-bit number that communicates how long the TCP header for this segment is
* __Control flags:__ is a 6-bit field for special TCP control flags
* The __TCP windows__ specifies the range of sequence numbers that might be sent before an acknowledgement is required
* The __TCP Checksum__ operates just like the checksum fields at the IP and ethernet level.
* __Urgent pointer field__ is used in conjunction with one ot the TCP control flags to point out particular segments that might be more important than others
* The __options field__ is sometimes used for more complicated flow control protocols
* We finally have __padding__ which is just a sequence of zeroes which ensure that the data payload being where expected

### TCP Control Flags and the Three-way Handshake

* A __buffer__ is a computing technique where data is held somewhere before being sent somewhere else

The TCP control flags are (not necessaraly in order):

1. __Urgent (URG):__ A value of one here indicates that the segment is considered urgent and that the urgent pointer field has more data about this
2. __Acknowledged (ACK):__ A value of one in this field means that the acknowledgement number field should be examined
3. __Push (PSH):__ The transmitting device wants the receiving device to push currently-buffered data to the application on the receiving end as soon as possible
4. __Reset (RST):__ one of the sides in a TCP connection hasn't been able to properly recover from a series of missing or malformed segments
5. __Synchronize (SYN):__ It's used when first establishing a TCP connection and makes sure the receiving end knows to examine the sequence number field
6. __Finish (FIN):__ When this flag is set to one, it means that the transmitting computer doesn't have any more data to send and the connection can be closed

* A __handshake__ is a way for two devices to ensure that they're speaking the same protocol and will be able to understand each other
   * Like the Three-way handshake for establishing connections, in where a a client sends a SYN packet, the server responds with SYN/ACK, and the client replies again with ACK
   * Or the Four-way handshake for closing connections, in where the computer ready to end a connection sends a FIN flag, the other computer will send an ACK flag, then a FIN flag, and finally the computer that initially sent the FIN flag responds with an ACK
   
### TCP Socket States

* A __socket__ is the instantation of an end-point in a potential TCP connection
* An __instantation__ is the actual implementation of something defined elsewhere

* Various TCP Socket States
    * __LISTEN__ means that a TCP socket is ready and listening for incoming connections
    * __SYN_SENT__ means that a synchronization request has been sent, but the connection hasn't been established yet
    * __SYN-RECEIVED__ means that a socket previously in a LISTEN state has recieved a synchronization request and sent a SYN/ACK back
    * __ESTABLISHED__ means that the TCP connection is in working order and both sides are free to send each other data
    * __FIN_WAIT__ means that a FIN has been sent, but the corresponding ACK from the other end hasn't been received yet
    * __CLOSE_WAIT__ means that the connection has been closed at the TCP layer, but that the application that opened the socket hasn't released its hold on the socket yet
    * __CLOSED__ means that the connection has been fully terminated and that no further communication is possible

### Connection-oriented and Connectionless Protocols

* A __connection-oriented protocol__ (like TCP) establishes a connection, and uses this to ensure that all data has been properly transmitted
* __Connectionless protocols__ (for example, UDP) simply sends packets to an IP address with its port number without any handshakes or much reliability
* Nice list of TCP and UDP port numbers: [https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)

### Firewalls

* A __firewall__ is a device that blocks traffic that meets certain criteria

## The Application Layer

### The Application Layer and the OSI Model

The __Open Systems Interconnection (OSI) Model__ has seven layers:

||Layer|
|-|----|
|7|Application|
|6|Presentation|
|5|Session|
|4|Transport|
|3|Network|
|2|Data link|
|1|Physical|

* The __Session Layer__ is responsible for facilitating the communication between actual applications and the transport layer; it takes application layer data and hands it off to the __presentation layer__
* The __Presentation Layer__ is responsible for making sure that the unencapsulated application layer data is able to be understood by the application in question

* It could be argued that the TCP/IP Five-layer model is more useful than the OSI model at least in everyday troubleshooting

### All the Layers Working in Unison

