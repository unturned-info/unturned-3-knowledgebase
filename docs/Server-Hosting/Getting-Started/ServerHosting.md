# Server Hosting

!!! Warning
    **New Unturned server hosting rules are in effect**

    Read [the Server Monetization Policy page](../../Explanations/Monetization) for more info.

All multiplayer servers are hosted using the Unturned Dedicated Server tool, which is installed and updated through Valve's [SteamCMD](https://developer.valvesoftware.com/wiki/SteamCMD) tool.

???+ Tip "Windows Server Hosting Tutorial Video"
    A video created by nelson that covers the basics of a windows server setup using the dedicated server app.
    The video does not cover Linux-based hosting or [**Port Forwarding**](PortForwarding.md) which is *required* for internet-accessible servers.
    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/8axVrnSLlx4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

__Multiplatform:__

- [How to Configure Server](#how-to-configure-a-server)
- [How to Host Curated Maps](#how-to-host-curated-maps)
- [How to Host Over Internet](#how-to-host-over-the-internet)
- [Port Forwarding](PortForwarding.md)
- [RocketMod](../../Modules-Plugins/Rocket)

__Windows:__

- [How to Install SteamCMD](#how-to-install-steamcmd-on-windows)
- [How to Launch Server](#how-to-launch-server-on-windows)

__Linux:__

- [How to Install SteamCMD](#how-to-install-steamcmd-on-linux)
- [How to Launch Server](#how-to-launch-server-on-linux)

## Installing SteamCMD

### How to Install SteamCMD on Windows

1. [Download From Here](https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip)
2. Extract the contents of the zip somewhere you can find it again.
3. Run `steamcmd.exe`

Continue to: [How to Install Server using SteamCMD](#how-to-install-server-using-steamcmd)

### How to Install SteamCMD on Linux

Installation on Linux varies by distribution and your admin preferences, so refer to [Valve's Linux Documentation](https://developer.valvesoftware.com/wiki/SteamCMD#Linux). Once downloaded, run the `steamcmd.sh` script.

Continue to: [How to Install Server using SteamCMD](#how-to-install-server-using-steamcmd)

## How to Install Server using SteamCMD

1. Log in to Steam anonymously:

        login anonymous

2. Download the server:

        app_update 1110390

    !!! note
        this command can also be used to update the server.

3. Close SteamCMD:

        quit

4. The server files are now in the SteamCMD > steamapps > common > U3DS directory.

Continue to: [How to Launch Server on Windows](#how-to-launch-server-on-windows) or [How to Launch Server on Linux](#how-to-launch-server-on-linux)

## Launching the server

### How to Launch Server on Windows

1. Navigate to the SteamCMD > steamapps > common > U3DS directory.
2. Right-click within the folder.
3. Select New > Text Document
4. Replace "New Text Document.txt" with "Tutorial.bat"
5. Right-click on the batch script (`Tutorial.bat`) and select Edit.
6. Insert the following text into the file:

    === "Internet"
        ```batch
        start %~dp0ServerHelper.bat +InternetServer/MyServer
        ```

    === "LAN"
        ```batch
        start %~dp0ServerHelper.bat +LanServer/MyServer
        ```

    !!! note
        In this example, MyServer is used as the ServerID for save data and configuration purposes.

7. Save your changes.
8. Double-click the batch script to launch the server.
9. Cleanly shutdown the server once it finishes loading:

        shutdown

    Running it will have created a "MyServer" directory in U3DS > Servers. This is where all save data and configuration files are kept. Changing the `MyServer` ServerID in the batch script can be done to run multiple servers at once, or to keep save data separately.

!!! example
    The included `ExampleServer.bat` serves as an example script

### How to Launch Server on Linux

1. Navigate to the SteamCMD > steamapps > common > U3DS directory.
2. For an internet server run the following command:

    === "Internet"
        ```bash
        ./ServerHelper.sh +InternetServer/MyServer
        ```

    === "LAN"
        ```bash
        ./ServerHelper.sh +LanServer/MyServer
        ```

    !!! note
        In this example, MyServer is used as the ServerID for save data and configuration purposes.

3. Cleanly shutdown the server once it finishes loading:

        shutdown

    Running it will have created a "MyServer" directory in U3DS > Servers. This is where all save data and configuration files are kept. Changing the `MyServer` ServerID in the launch arguments can be done to run multiple servers at once, or to keep save data separately.

For an example script, open the built-in `ExampleServer.sh` file.
!!! example
    The included `ExampleServer.sh` serves as an example script

## How to Configure a Server

!!! note 
    ServerID is the name after the `+InternetServer/` or `+LanServer/` command. For example `+InternetServer/TestServer` will cause server folder named TestServer in the Servers folder.
    Navigate to U3DS > Servers > ServerID.
    See also the [Server Configuration](../../Server-Configuration/Commands.dat) sections.

ServerID differentiates multiple servers ([Ports](PortForwarding.md) can't be same) running from the same installation, and a directory for each server's savedata and configuration wil be created in the `Servers > ServerID` directory.

Meaning the each individual ServerID has its own save data and configuration.

Startup commands can be specified in the 
`ServerID > Server >` [`Commands.dat`](../../Server-Configuration/Commands.dat) file, or on the command-line (script) with [`-CommandName/Argument`](../../Server-Configuration/Commands.dat).

### Launch Commands
 Launch Commands was moved to the [`Commands.dat`](../../Server-Configuration/Commands.dat) file.
 
## How to Host Curated Maps
 This explanation was moved to the [Curated Maps](../../Explanations/CuratedMaps) site.
 
### Workshop add-ons
 Workshop add-ons was moved to the [`WorkshopDownloadConfig.json`](../../Server-Configuration/WorkshopDownloadConfig.json) file.

## How to Host Over the Internet

Hosting a publicly-accessible internet server requires an extra step compared to a LAN server. When on a home network [Port Forwarding](PortForwarding.md) is required to direct traffic to the host computer.

One way to think of it is that when there are multiple devices (e.g. computers and phones) connected to the LAN, the outside internet does not know which device is the Unturned server. In this case, port forwarding specifies which LAN device is the host.

For port ranges and other details: [Port Forwarding](PortForwarding.md)
