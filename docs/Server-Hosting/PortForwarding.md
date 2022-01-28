# Port Forwarding

When hosting a server on a home network __port forwarding__ is required to direct traffic to the host computer. One way to think of it is that when there are multiple devices (e.g. computers and phones) connected to the LAN, the outside internet does not know which device is the Unturned server. In this case, port forwarding specifies which LAN device is the host.

Two pieces of information: the [port range](#port-range) and [local device address](#local-device-address) are required before port forwarding, and are described in detail below.

!!! caution
    Depending on your ISP and other factors, it may not be possible for you to port forward in any capacity. Additionally, many ISPs block certain ports for security and network management purposes.

## Port Range

Each Unturned server uses three consecutive ports while running. The first is used for game traffic, the second for server list queries, and the third for communicating with the Steam backend services.

By default 27015 and 27016 are used. Setting a different value with the `Port` command uses that value and value + 1. Recommended `Port` command settings are 27015 for the first server, 27017 for the second server, 27020 for the third server, so on and so forth.

## Local Device Address

Forwarding the ports directs them to a LAN address, i.e. the computer hosting the server. To determine the local IP:

=== "Windows"
    1. Press Windows + R to open the Run dialog.
    2. Type `cmd` and press enter.
    3. Type `ipconfig` in the command prompt and press enter.
    4. Find the `Wireless LAN adapter Wi-Fi` or `Ethernet adapter Ethernet` header.
    5. Look for the `IPv4 Address` value and make note of it. This is the internal IP you will forward the ports to. It likely looks something like `192.168.0.6`.

=== "Ubuntu"
    1. Open a terminal of your choice.
    2. Run the command `hostname -i` in your terminal.
    3. Note the outputted IP addresses. The first one is likely your localhost address.

!!! note
    You can also find your localhost address under the networking menu within the GUI.

## Forwarding Ports

Instructions vary by router but should be doable from the web browser without any extra tools or software. This third-party website has a thorough list of routers with simple steps for each model: <https://portforward.com/router.htm>

!!! Note
    Before you begin, you'll need administrator access to your router.

In general, the steps are along the lines of:

1. Connect to the router via a web browser.

    !!! tip
        The addresses for these are often either `192.168.0.1`, `10.0.0.1`, or `172.16.0.1`.

2. Login with home admin credentials.
3. Find the Port Forwarding menu.
4. Find the option to add a new rule.
5. Use a name that will help you identify it in the future.
6. Input 27015 as the starting port(s), and 27016 as the ending port(s).

    !!! Note
        On some routers, it may not be possible to input multiple ports within a single rule. In that case, multiple rules can be set up; one for each of the three ports.

7. Enable TCP **and** UDP protocols.
8. Set destination internal IP to the localhost address. In the previous example, our localhost address was `192.168.0.6`
9. Save the new rule.

!!! Important
    Other players outside of your LAN will need to use your public IP to direct connect to your server.
