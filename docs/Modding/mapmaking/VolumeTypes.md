# Volume Types

!!! note
    This document is a work in progress. Some information may be incorrect or outdated.

In Unturned, there are several volume types that assist map creators. Volumes are used for applying specific conditions to players, improving optimization, and preventing unintended glitches.

### Ambiance Volume
Adds ambiance effects within volume bounds. Useful for underground environments.

__Effect ID:__ GUID or legacy ushort ID for an ambiance effect.

__No Water:__ Toggles water effects.

__No Lighting:__ Toggles atmospheric lighting.

__Weather Mask:__ Integer value for the weather mask within the volume.

__Override Fog:__ Toggles if the volume's fog settings should override that of the map.

__Fog Intensity:__ Value determining fog intensity within the volume.

__Override Atmospheric Fog:__ Toggles if atmospheric fog should affect those within the volume.

### Arena Compactor Volume
Designates a location for the 'Arena' gamemode compactor to close on. Several of these volumes can be placed to randomize locations reach arena round. Does not support box sizing.

### Cartography Volume
Used to position the satellite and chart baking camera. Does not support sphere sizing.

### Culling Volume

__Cull Distance:__ Modifies the culling distance.

__Include Large Objects:__ Toggles if the Culling Volume should cull 'Large' objects within it.

### Deadzone Volume
Applies deadzone status/conditions to players that enter the volume.

__Deadzone Type:__ `Default Radiation`, `Full Suit Radiation`. Specifies required deadzone protection (i.e. Gasmask).

### Effect Volume
Used for placing visual effects on maps.

__Effect ID:__ GUID or legacy ushort ID for an effect.

__Emission Rate:__ Multipler determining the emission rate of the effect.

__Audio Range:__ Determines how far audio should travel. Used for effects with audio sources.

### Foliage Volume
Used to determine the bounds of foliage placement.

__Mode:__ `Additive`, `Subtractive`. Specifies volume logic.

__Instanced Meshes:__ Toggles instanced mesh placement.

__Resources:__ Toggles resource placement.

__Objects:__ Toggles object placement.

### Horde Purchase Volume
Originally used in the horde gamemode. Allows the player to purchase items using experience points.

__Item ID:__ Legacy ushort ID specifying the purchasable item.

__Cost:__ Cost of purchasing the item.

### Kill Volume
Kills an entity on collision.

__Kill Players:__ Toggles if the volume should affect players.

__Kill Zombies:__ Toggles if the volume should affect zombies.

__Kill Animals:__ Toggles if the volume should affect animals.

__Kill Vehicles:__ Toggles if the volume should affect vehicles.

__Death Cause:__ `BLEEDING`, `BONES`, `FREEZING`, `BURNING`, `FOOD`, `WATER`, `GUN`, `MELEE`, `ZOMBIE`, `ANIMAL`, `SUICIDE`, `KILL`, `INFECTION`, `PUNCH`, `BREATH`, `ROADKILL`, `VEHICLE`, `GRENADE`, `SHRED`, `LANDMINE`, `ARENA`, `MISSILE`, `CHARGE`, `SPLASH`, `SENTRY`, `ACID`, `BOULDER`, `BURNER`, `SPIT`, `SPARK`. Specifies the death cause displayed when a player is affected. Defaults to `BLEEDING`.

### Nav Volume
Blocks pathfinding.

### Oxygen Volume
Modifies oxygen requirements for players within the volume.

__Is Breathable:__ Toggles if the volume makes it breathable or unbreathable.

### Player Clip Volume
Used to block players from entering certain areas. Can also be used to prevent building.

__Block Player:__ Toggles if players should be blocked by the volume.

### Safezone Volume
Applies safezone status/conditions to players that enter the volume. Used for quest locations.

__No Weapons:__ Toggles if weapons should be usable while within the volume.

__No Buildables:__ Toggles if players should be able to build within the volume.

### Teleporter Entrance Volume
Allows players to teleport to the position of the paired Teleporter Exit Volume on collision. Does not support sphere sizing.

__Pair ID:__ Value that specifies an identifier that should match with a Teleporter Exit Volume. Volumes with the same Pair ID are considered paired and will work together to teleport the player.

### Teleporter Exit Volume
Marks the teleport position and angle for a Teleporter Entrance Volume. Does not support sizing.

__Pair ID:__ Value that specifies an identifier that should match with a Teleporter Entrance Volume. Volumes with the same Pair ID are considered paired and will work together to teleport the player.

### Underground Whitelist Volume
Designates areas where players are able to go underground. Set `Use_Underground_Whitelist` to true in the map Config.json.

### Water Volume
As the name implies, the Water Volume allows map creators to position water above the selected elevation of the main water volume on the map. Does not support sphere sizing.

__Sea Level:__ Toggles the water volume as the main water volume. Allows the volume to be positioned by the water elevation settings within the map editor lighting tab.

__Surface Visible:__ Toggles if the surface of the water volume is visible.

__Reflection Visible:__ Toggles if reflections caused by the volume are visible.