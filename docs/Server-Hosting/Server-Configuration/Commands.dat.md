# Commands.dat

##Startup command-line
!!! Note
    Startup commands can be used as a launch commands in the command-line (launch script). But you will propably use only `commands.dat` file.
	
    Examples: `-Map/Washington` `-Port/27015` `-Perspective/Both` `-CommandName/Argument`
---

Launch commands are set up in the Server > `Commands.dat` file. Each line should have only one command.
Some commands can be used as well in console while running.
---

## Useful commands

### Name

	Name of the server on the server list; set as "Unturned" by default.
	Example: "Name My super pvp server"

---
### Port
About [Port ranges](../../Getting-Started/PortForwarding/#port-range)
   
	Sets the server's port; set as "27015" by default.
	Example: "Port 27015"
---
### Map

	Specify the map to load by name (Washington, Russia, PEI).
	If the server does not find the map; set as PEI by default.
	Example: "Map Washington"
---
### Password

	Requires password to join the server.
	Example: "Password mysupers3cr3tp4ssw8rd"
---
### Perspective

	Can be set to "First", "Third", "Both", or "Vehicle" to change camera options.
	Example: "Perspective First"
---
### Cheats

	Allows admins to invoke cheat commands like spawning items or vehicles from the chat.
	Example: "Cheats"
---
### Maxplayers

	Sets the max amount of players the server will allow.
	Example: "Maxplayers 24"
---
### Mode

Advanced Game rules you can change in [Config.json](../Config.json)
	Sets the difficulty mode. Available difficulties (Easy, Normal, Hard).
	Example: "Mode Normal"
---
## Another Commands

### Whitelisted

	This makes only permited players allowed to join the server.

	For manage whitelisted players see information below.
	For add player to whitelist use /permit <SteamID64>/tag (Tag is useful for show name of the player when you list whitelisted players.)

	For remove player from whitelist /unpermit <SteamID64>. Or /unpermit <tag_name>

	To display all players who are on the whitelist use command /permits
	Example: "Whitelisted"
---
### Gold

	Restricts the server only for Gold players
	Example: "Gold"
---
### Chatrate

	Assigns the minimum amount of time (in seconds) between chat messages.
	This is good for spam protect.
	Example: "Chatrate 2"
---
### Cycle

	Assigns the day/night cycle in seconds.
	Example: "Cycle 1800"
---
### Log

	Enables/Disables logging
	Thats mean in the log/console you will have join & leave & death & anticheat messages.
	Format [chat]/[join&leave]/[death]/[anticheat]
	(Y = Yes, N = No)
	Example: "Log Y/Y/N/Y" (Only death messages won't logged.)
---
### Timeout

	Sets the max ping for players before they time out. (From 50 to 10000)  (400~600 is recommended)
	Example: "Timeout 400"
---
### Bind

	Binds your internal IP. This you can use if you have 2 or more ip addresses on the same server.
	Example: "Bind 127.0.0.1"
---
### Filter

	Enables the old name filter
	This will block players with unknown characters in the name.
	Example: "Filter"
---
### Loadout

	Assigns what all players spawn with. The first number value in the loadout is the Skillset ID.
	Example: "Loadout 255/15/15/81/81/18/20/20/121"
	This gives all skillsets 2 Medkits, 2 MREs, a Timberwolf, 2 Timberwolf Magazines, and a Military Knife.
---
### Owner

	Sets the server's owner, which gives them administrator commands. The Owner looks like normal blue administrator, but owner can't be removed with /unadmin command.
	Placeable structures/barricades placed in map editor on the map will be bounded to the owner.
---
### Sync

	This allows players to share savedata between your servers.
	Example: "Sync"
---
### Welcome

	Sets the welcome message.
	On the end, you can specify the color using the RGB code. (Red Green Blue)
	Example: "Welcome Welcome on my awesome server/255/0/0" This will show text when you join "Welcome on my awesome server" in Red text.
---
### Hide_admins

	This will hide the admin blue names.
---
### Votify

	Sets up voting. Pass/fail cooldown specifies the amount of time that players must wait after a successful/failed vote before initiating another vote.
	"Vote duration" specifies the amount of time for each vote to remain active.
	"Vote percentage" indicates the percentage of "yes" votes required for a successful vote and must be expressed in decimals (e.g., 0.6 for 60%).
	Required "Players" specifies the minimum number of connected players in order to initiate a vote.
	
	Format [Vote Allowed Y/N]/[Pass Cooldown]/[Fail Cooldown]/[Vote Duration]/[Vote Percentage]/[Players]
	(Y = Yes, N = No)
	Example: "Votify Y/300/300/30/0.6/5"
---
### Queue_size

	Sets the maximum number of player that can be in queue.
	Example: "Queue_size 10"
---
### GSLT
About [GSLT](../../Explanations/GameServerLoginTokens)

	Example: "GSLT 45GB94HDF654HFDDFHD6546FD" (45GB94HDF654HFDDFHD6546FD=Login Token changed it to your own Token)
---


Game rules, listing display, and many other options for server are available in the [Config.json](../Config.json) file.
