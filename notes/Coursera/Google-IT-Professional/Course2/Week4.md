# Networking Services (Week 4)

## Name Resolution

### Why do we need DNS?

* __Domain Name System (DNS)__ is a global and highly distributed network service that resolves strings of letters into IP addresses for you
* A __Domain Name__ is the term we use for something that can be resolved by DNS
* DNS is useful because it allows us to only have to memorise domain names instead of IP addresses
    * They're also useful in the event that the IP address of the service changes, the domain name can just be reconfigured to "point" to the new IP address
    * DNS also allows us to distribute web servers across the globe, so that users can access services quicker by geographical location
    
### The Many Steps of Name Resolution

* __Time to Live (TTL):__ is a value, in seconds, that can be configured by the owner of a domain name for how long a name server is allowed to cache an entry before it should discard it and perform a full resolution again
* __Anycast__ is a technique that's used to route traffic to different destinations depending on factors like location, congestion, or link health

* There are five primary types of DNS Servers:
    1. __Caching name servers__ - purpose is to store known domain name lookups for a certain amount of time, stores them in cache
    2. __Recursive name servers__ - purpose is to store known domain name lookups for a certain amount of time, this one specifically performs full DNS resolution requests
    3. __Root name servers__ - these are 13 authorative name servers that redirects DNS requests to the appopriate TLD name server
    4. __TLD name servers__ - name servers that redirect to .com, .org, .net, .edu, .gov, .horse, etc.
    5. __Authoritative name servers__ these are the DNS servers that hold the records for a particular domain name
    
* DNS works like this:
    1. The User makes a DNS request to the Caching/Recursive Name server
    2. If the domain name is not cached in the DNS server, then forward the request to one of the 13 root servers and get a TLD server, the caching/recursive server will then request information from a TLD name server, and finally will request information from the name server in charge of the domain name.

### DNS and UDP

* Remember that UDP is connectionless, ergo data can be transmitted quicker
* A single DNS request and response can fit inside a single datagram
* With UDP, DNS requests and responses go from an average of 44 datagram transfers to eight datagram transfers
* It should be noted that there are DNS implementations that use TCP

## Name Resolution in Practice

### Resource Record Types

* Kinds of DNS Resource Records:

|Record Name|Description|
|-----------|-----------|
|A record|used to point a certain domain name to a certain IPv4 IP address. Typically, single A records are configured for IP addresses, but single domain names can have multiple A records, allowing for DNS round robin which is used to balance traffic|
|AAAA record|similar to the A record, but returns a IPv6 address instead of an IPv4 one|
|CNAME record|used to redirect traffic from one domain name to another|
|MX record|or "Mail Exchange", is used in order to deliever email to the correct company|
|SRV record|or "Service Record", is used to define the location of various specific services, similar to MX but for many different service types|
|TXT record|leave notes or messages in the DNS entry, can also be read by other computer programs for specific configs, etc.|

### Anatomy of a Domain Name

* A __Top Level Domain (TLD)__ is the last part of a domain name
* The __Internet Corporation for Assigned Names and Numbers (ICAAN)__ is a non-profit organization, sister to the IANA, that both control the IP address spaces and the TLD systems.
* __Domains__ are used to demarcate where control moves from a TLD name server to an authoritative name server
* A __Fully qualified domain name (FQDN)__ is what we call URLs that have both a subdomain name, a domain name, and a TLD. 
* DNS can technically support up to 127 levels of domain in total for a single fully qualified domain name

### DNS Zones

* __DNS Zones__ are a hierarchical concept, they don't overlap, they allow for easier control over multiple levels of a domain
* __Zone files__ are simple configuration files that declare all resource records for a particular zone
* __Start of authority (SOA)__ is a declaration that the zone and the name of the name server that is authoritative for it
* __NS Records__ indicate other name servers that might also be responsible for this zone
* __Reverse lookup zone files__ let DNS resolvers ask for an IP and get the FQDN associated with it returned
* A __Pointer resource record (PTR)__ resolves an IP to a name

## Dynamic Host Configuration Protocol

### Overview of DHCP

* Networks need four primary things configured to work properly
    1. An IP address
    2. A subnet mask
    3. A gateway
    4. A name server
    
* The subnet mask, gateway, and name server usually have the same configuration
* The IP address, however, has to be different for every network
* __Dynamic Host Configuration Protocol (DHCP)__ is an application layer protocol that automates the configuration process of hosts on a network
* You should "hard code" core servers (like DNS or HTTP) servers to that it will be easier to connect to and diagnose it if problems arise
* __Dynamic allocation__ is a range of IP addresses that is set aside for client devices and one of these IPs is issued to these devices when they request one
* __Automatic allocation__ is a range of IP addresses set asside for assignment purposes
* __Fixed allocation__ requires a manually specified list of MAC addresses and their corresponding IPs
* __Network time protocol (NTP) servers__ are used to keep all computers on a network synchronized in time

### DHCP in Action

DHCP is accomplished in the following steps:

1. __DHCP discovery__ is the request by which a client configured to use DHCP attempts to get network configuration information by broadcasting a "discovery" request to all computers. It should be caught by the DHCP server.
    * This is done through a specially crafter broadcast message, the DHCP server listens on port 67 and the DHCP discover message always comes from source port 68.
2. __DHCP offer__ is a broadcast that will hopefully reach the client and tells the client that it is "offering" its DHCP services
3. __DHCP request__ is the client's response to DHCP offer asking for an IP address
4. __DHCP ack__ is an "acknowledgement" from the DHCP server 

* This is called "DHCP lease" since the IP address assigned to the computer might expire in the future

## Network Address Translation

### Basics of NAT

* __Network Address Translation (NAT)__ is a technique rather than a universal standard, it literally takes an IP address and translates it into another. This is useful for security safeguards and when IP addresses need to be allocated; it is a techology that allows a gateway, usually a router or firewall, to rewrite the source IP of an outgoing IP datagram while retaining the original IP in order to rewrite it into the response
* __IP masquerading__ is a security concept that allows a client to hide their source IP address

### NAT and the Transport Layer

* __Port preservation__ is a technique where the source port chosen by a client is the same port used by the router
* __Port forwarding__ is a technique where specific destination ports can be configured to always be delievered to specific nodes

### NAT, Non-Routable Address Space and the Limits of IPv4

* __Regional Internet Registries (RIRs)__ are registries to assign IP address blocks to certain regions. They are:
    1. AFRINIC
    2. ARIN
    3. APNIC
    4. LACNIC
    5. RIPE

## VPNs and Proxies

### Virtual Private Networks

* __Virtual Private Networks (VPNs)__ are a technology that allows for the extension of a private or local network to hosts that might not be on that local network
* __Two-factor authentication__ is a technique where more than just a username and password are required to authenticate
* VPNs are not a strictly defined protocol, but, like NAT, are more varied

### Proxy Services

* A __Proxy Service__ is a server that acts on behalf of a client in order to access another service
* Proxy Services can provide:
    * Anonymity
    * Security
    * Content Filtering
    * Increased Performance
    
* Gateway routers are an example of proxy service
* It is a concept or abstraction, proxies exist on almost every layer of the TCP/IP networking model
* Proxies usually refer to __web proxies__
    * Web proxies were used originally used for increased performance, by caching websites.
    * Web proxies are now used as content filters
    
* A __reverse proxy__ is a service that might appear to be a single server to external clients, but actually represents many servers living behind it
    * Reverse proxies are useful for handling large amounts of web traffic and for load balancing
    * Reverse proxies can also be used for decryption services
