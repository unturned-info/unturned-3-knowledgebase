# Resource Data

**Resources** in Unturned allow for players to receive experience or items by destroying or foraging nodes (i.e. trees, ore deposits).

!!! tip
    Properties are formatted as **Property_Key** \&lt;data_type&gt;\: description

__Auto_Skybox__: Specifies if the game should generate its own skybox for the resource.

__BladeID__: Similar to caliber for items. Allows the resource to be destroyed only by an item with the same BladeID.

__Bypass_ID_Limit__ &lt;flag&gt;: Allows you to use an ID that is within the space reserved for vanilla content, the game will throw an exception if you use an ID below 50 otherwise.

__Chart__ &lt;enum&gt;: `NONE`, `GROUND`, `IGNORE`, `HIGHWAY`, `ROAD`, `STREET`, `PATH`, `LARGE`, `MEDIUM`, `WATER`, `CLIFF`. Specifies what chart color should be used for the resource.

__Christmas_Redirect__ &lt;guid&gt;: Asset used during Christmas.

__Exclude_From_Level_Batching__ &lt;boolean&gt;: Specifies if the resource should be included in level batching.

__Explosion__ &lt;guidOrLegacy&gt;: The effect spawned when the resource is destroyed.

__Forage__ &lt;flag&gt;: Specifies if the resource can be foraged.

__Forage_Reward_Experience__ &lt;uint32&gt;: The amount of experience given after being foraged.

__Has_Clip_Prefab__ &lt;boolean&gt;: Specifies if the resource has its clip prefabs.

__Health__ &lt;uint16&gt;: How much health the resource should spawn with.

__Holiday_Restriction__ &lt;enum&gt;: `NONE`, `HALLOWEEN`, `CHRISTMAS`, `APRIL_FOOLS`, `VALENTINES`, `PRIDE_MONTH`, `MAX`. Restricts resource visibility to the specified holiday.

__Halloween_Redirect__ &lt;guid&gt;: Asset used during Halloween.

__Log__ &lt;uint16&gt;: The log item spawned when destroyed.

__No_Debris__ &lt;flag&gt;: Specifies if the resource has debris.

__Radius__ &lt;float&gt;: Radius checked when baking resources on a map.

__Reset__ &lt;float&gt;: Amount of time it takes for the resource to respawn.

__Reward_ID__ &lt;uint16&gt;: The item that should be spawned when destroyed.

__Reward_Max__ &lt;uint8&gt;: Maximum amount of items spawned when destroyed.

__Reward_Min__ &lt;uint8&gt;: Minimum amount of items spawned when destroyed.

__Reward_XP__ &lt;uint32&gt;: The amount of experience that should be given when destroyed.

__Scale__ &lt;float&gt;: How much the resource can be scaled when being spawned in.

__SpeedTree__ &lt;flag&gt;: Specifies if the resource uses speed tree models.

__SpeedTree_Default_LOD_Weights__ &lt;flag&gt;: Specifies if the LOD weights should default for the speed tree model.

__Stick__ &lt;uint16&gt;: The stick item spawned when destroyed.

__Vulnerable_To_All_Melee_Weapons__ &lt;boolean&gt;: Specifies if all melee weapons can damage the resource.

__Vulnerable_To_Fists__ &lt;boolean&gt;: Specifies if players can damage the resource with their fists.

__Vertical_Offset__ &lt;float&gt;: How much the resource should be offset vertically when being spawned in.
