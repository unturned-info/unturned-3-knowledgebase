# Resource Data

**Resources** in Unturned allow for players to receive experience or items by destroying or foraging nodes (i.e. trees, ore deposits).

!!! tip
    Properties are formatted as **Property_Key** \<data_type>\: description

__Auto_Skybox__: Specifies if the game should generate its own skybox for the resource.

__BladeID__: Similar to caliber for items. Allows the resource to be destroyed only by an item with the same BladeID.

__Bypass_ID_Limit__ <<abbr title="a value that is either present or not.">flag</abbr>>: Allows you to use an ID that is within the space reserved for vanilla content, the game will throw an exception if you use an ID below 50 otherwise.

__Chart__ &lt;enum&gt;: `NONE`, `GROUND`, `IGNORE`, `HIGHWAY`, `ROAD`, `STREET`, `PATH`, `LARGE`, `MEDIUM`, `WATER`, `CLIFF`. Specifies what chart color should be used for the resource.

__Christmas_Redirect__ &lt;guid&gt;: Asset used during Christmas.

__Exclude_From_Level_Batching__ <<abbr title="a simple true/false value.">boolean</abbr>>: Specifies if the resource should be included in level batching.

__Explosion__ <<abbr title="Either a uint16 id or a GUID.">guidOrLegacy</abbr>>: The effect spawned when the resource is destroyed.

__Forage__ <<abbr title="a value that is either present or not.">flag</abbr>>: Specifies if the resource can be foraged.

__Forage_Reward_Experience__ <<abbr title="unsigned 32 bit integer from 0 to 65,535">uint32</abbr>>: The amount of experience given after being foraged.

__Has_Clip_Prefab__ <<abbr title="a simple true/false value.">boolean</abbr>>: Specifies if the resource has its clip prefabs.

__Health__ <<abbr title="unsigned 16 bit integer from 0 to 65,535.">uint16</abbr>>: How much health the resource should spawn with.

__Holiday_Restriction__ &lt;enum&gt;: `NONE`, `HALLOWEEN`, `CHRISTMAS`, `APRIL_FOOLS`, `VALENTINES`, `PRIDE_MONTH`, `MAX`. Restricts resource visibility to the specified holiday.

__Halloween_Redirect__ &lt;guid&gt;: Asset used during Halloween.

__Ignore_Solid_Foundation__ <<abbr title="a simple true/false value.">boolean</abbr>>: Specifies if the resource should ignore solid foundations.

__Log__ <<abbr title="unsigned 16 bit integer from 0 to 65,535.">uint16</abbr>>: The log item spawned when destroyed.

__No_Debris__ <<abbr title="a value that is either present or not.">flag</abbr>>: Specifies if the resource has debris.

__Radius__ <<abbr title="32 bit floating point number from ±1.5 x 10−45 to ±3.4 x 1038 including decimal values.">float</abbr>>: Radius checked when baking resources on a map.

__Reset__ <<abbr title="32 bit floating point number from ±1.5 x 10−45 to ±3.4 x 1038 including decimal values.">float</abbr>>: Amount of time it takes for the resource to respawn.

__Reward_ID__ <<abbr title="unsigned 16 bit integer from 0 to 65,535.">uint16</abbr>>: The item that should be spawned when destroyed.

__Reward_Max__ <<abbr title="unsigned 8 bit integer from 0 to 255">uint8</abbr>>: Maximum amount of items spawned when destroyed.

__Reward_Min__ <<abbr title="unsigned 8 bit integer from 0 to 255">uint8</abbr>>: Minimum amount of items spawned when destroyed.

__Reward_XP__ <<abbr title="unsigned 32 bit integer from 0 to 65,535">uint32</abbr>>: The amount of experience that should be given when destroyed.

__Scale__ <<abbr title="32 bit floating point number from ±1.5 x 10−45 to ±3.4 x 1038 including decimal values.">float</abbr>>: How much the resource can be scaled when being spawned in.

__SpeedTree__ <<abbr title="a value that is either present or not.">flag</abbr>>: Specifies if the resource uses speed tree models.

__SpeedTree_Default_LOD_Weights__ <<abbr title="a value that is either present or not.">flag</abbr>>: Specifies if the LOD weights should default for the speed tree model.

__Stick__ <<abbr title="unsigned 16 bit integer from 0 to 65,535.">uint16</abbr>>: The stick item spawned when destroyed.

__Vulnerable_To_All_Melee_Weapons__ <<abbr title="a simple true/false value.">boolean</abbr>>: Specifies if all melee weapons can damage the resource.

__Vulnerable_To_Fists__ <<abbr title="a simple true/false value.">boolean</abbr>>: Specifies if players can damage the resource with their fists.

__Vertical_Offset__ <<abbr title="32 bit floating point number from ±1.5 x 10−45 to ±3.4 x 1038 including decimal values.">float</abbr>>: How much the resource should be offset vertically when being spawned in.
