# Server Configuration

<!-- This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/4.0/.  -->

Also known as `Config.json`

## Browser Config

| Key              | Value                  | Description                                                   |
| ---------------- | ---------------------- | ------------------------------------------------------------- |
| Icon             | String                 | Direct URL for the server icon.                               |
| Thumbnail        | String                 | Direct URL for the server icon.                               |
| Desc_Hint        | String                 | Short server description.                                     |
| Desc_Server_List | String                 | Full server description.                                      |
| Login_Token      | String                 | Game Server Login Token. [See GSLT](GameServerLoginTokens.md) |
| Monetization     | EServerMonetizationTag | [See Monetization](Monetization.md). Defaults to unspecified  |
| Links            | Array                  |                                                               |

## Server Config

| Key                                | Value    | Default                                                                                                          | Description |
| ---------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------- | ----------- |
| VAC_Secure                         | boolean  | true                                                                                                             |             |
| BattlEye_Secure                    | boolean  | true                                                                                                             |             |
| Max_Ping_Milliseconds              | uint     | 750                                                                                                              |             |
| Timeout_Queue_Seconds              | float    | 15.0                                                                                                             |             |
| Timeout_Game_Seconds               | float    | 30.0                                                                                                             |             |
| Max_Packets_Per_Second             | float    | 50.0                                                                                                             |             |
| Rate_Limit_Kick_Threshold          | int      | 10                                                                                                               |             |
| Fake_Lag_Threshold_Seconds         | float    | 3                                                                                                                |             |
| Fake_Lag_Log_Warnings              | boolean  |                                                                                                                  |             |
| Fake_Lag_Damage_Penalty_Multiplier | float    | 0.1                                                                                                              |             |
| Enable_Kick_Input_Spam             | boolean  | false                                                                                                            |             |
| Enable_Kick_Input_Timeout          | boolean  | false                                                                                                            |             |
| Enable_Scheduled_Shutdown          | boolean  |                                                                                                                  |             |
| Scheduled_Shutdown_Time            | String   | "1:30 am"                                                                                                        |             |
| Scheduled_Shutdown_Warnings        | String[] | `{ "00:30:00", "00:15:00", "00:05:00", "00:01:00", "00:00:30", "00:00:15", "00:00:03", "00:00:02", "00:00:01" }` |             |
| Enable_Update_Shutdown             | boolean  |                                                                                                                  |             |
| Update_Steam_Beta_Name             | "public  |                                                                                                                  |             |
| Update_Shutdown_Warnings           | String[] | `{ "00:03:00", "00:01:00", "00:00:30", "00:00:15", "00:00:03", "00:00:02", "00:00:01" }`                         |             |
| Chat_Always_Use_Rich_Text          | boolean  |                                                                                                                  |             |
| Validate_EconInfo_Hash             | boolean  | true                                                                                                             |             |
| Validate_MasterBundle_Hashes       | boolean  | true                                                                                                             |             |

## Unity Event Config

| Key                   | Value   | Default | Description |
| --------------------- | ------- | ------- | ----------- |
| Allow_Server_Messages |         |         |             |
| Allow_Server_Commands | boolean |         |             |
| Allow_Client_Messages | boolean |         |             |
| Allow_Client_Commands | boolean |         |             |

## Mode Config

### Items Config

| Key                          | Value   | Default (Easy) | Default (Normal) | Default (Hard) | Default (Default) | Description |
| :--------------------------- | :------ | :------------- | :--------------- | :------------- | :---------------- | :---------- |
| Spawn_Chance                 | float   | 0.35           | 0.35             | 0.15           | 1                 |             |
| Despawn_Dropped_Time         | float   |                |                  |                |                   |             |
| Despawn_Natural_Time         | float   |                |                  |                |                   |             |
| Respawn_Time                 | float   | 50             | 100              | 150            | 1000000           |             |
| Quality_Full_Chance          | float   | 0.1            | 0.1              | 0.01           | 1                 |             |
| Quality_Multiplier           | float   | 1              | 1                | 1              | 1                 |             |
| Gun_Bullets_Full_Chance      | float   | 0.1            | 0.05             | 0.025          | 1                 |             |
| Gun_Bullets_Multiplier       | float   | 1              | 0.25             | 0.1            | 1                 |             |
| Magazine_Bullets_Full_Chance | float   | 0.1            | 0.05             | 0.025          | 1                 |             |
| Magazine_Bullets_Multiplier  | float   | 1              | 0.5              | 0.25           | 1                 |             |
| Crate_Bullets_Full_Chance    | float   | 0.1            | 0.05             | 0.025          | 1                 |             |
| Crate_Bullets_Multiplier     | float   | 1              | 1                | 0.75           | 1                 |             |
| Has_Durability               | boolean | FALSE          | TRUE             | TRUE           | TRUE              |             |

### Vehicles Config

| Key                                | Value | Default (Easy) | Default (Normal) | Default (Hard) | Default (Default) | Description                                                                      |
| :--------------------------------- | :---- | :------------- | :--------------- | :------------- | :---------------- | :------------------------------------------------------------------------------- |
| Decay_Time                         | float | 604800         |                  |                | 604800            |                                                                                  |
| Decay_Damage_Per_Second            | float | 0.1            | 0.1              | 0.1            | 0.1               |                                                                                  |
| Has_Battery_Chance                 | float | 1              | 0.8              | 0.25           | 1                 | Chance the vehicle will spawn with a battery.                                    |
| Min_Battery_Charge                 | float | 0.8            | 0.5              | 0.1            | 1                 | Minumum battery charge the vehicle can spawn with.                               |
| Max_Battery_Charge                 | float | 1              | 0.75             | 0.3            | 1                 | Maximum battery charge the vehicle can spawn with.                               |
| Has_Tire_Chance                    | float | 1              | 0.85             | 0.7            | 1                 | Chance the vehicle will spawn with tires.                                        |
| Respawn_Time                       | float | 300            | 300              | 300            | 300               | Time taken before the game will respawn a vehicle.                               |
| Unlocked_After_Seconds_In_Safezone | float | 3600           | 3600             | 3600           | 3600              | Time in seconds after which a locked vehicle inside a safezone will be unlocked. |
| Armor_Multiplier                   | float | 1              | 1                | 1              | 1                 | Vehicle armor multiplier                                                         |
| Child_Explosion_Armor_Multiplier   | float | 1              | 1                | 1              | 1                 |                                                                                  |
| Gun_Lowcal_Damage_Multiplier       | float | 1              | 1                | 1              | 1                 |                                                                                  |
| Gun_Highcal_Damage_Multiplier      | float | 1              | 1                | 1              | 1                 |                                                                                  |
| Melee_Damage_Multiplier            | float | 1              | 1                | 1              | 1                 |                                                                                  |
| Melee_Repair_Multiplier            | float | 1              | 1                | 1              | 1                 |                                                                                  |
| Max_Instances_Tiny                 | uint  | 4              | 4                | 4              | 4                 | Amount of vehicles on a Tiny map above which vehicles will stop spawning         |
| Max_Instances_Small                | uint  | 8              | 8                | 8              | 8                 | Amount of vehicles on a Small map above which vehicles will stop spawning        |
| Max_Instances_Medium               | uint  | 16             | 16               | 16             | 16                | Amount of vehicles on a Medium map above which vehicles will stop spawning       |
| Max_Instances_Large                | uint  | 32             | 32               | 32             | 32                | Amount of vehicles on a Large map above which vehicles will stop spawning        |
| Max_Instances_Insane               | uint  | 64             | 64               | 64             | 64                | Amount of vehicles on a Insane map above which vehicles will stop spawning       |
|                                    |       |                |                  |                |                   |                                                                                  |
### Zombies Config

| Key                             | Value | Default (Easy) | Default (Normal) | Default (Hard) | Default (Default) | Description |
| :------------------------------ | :---- | :------------- | :--------------- | :------------- | :---------------- | :---------- |
| Spawn_Chance                    | float | 0.2            | 0.25             | 0.3            | 1                 |             |
| Loot_Chance                     | float | 0.55           | 0.5              | 0.3            | 0                 |             |
| Crawler_Chance                  | float | 0              | 0.15             | 0.125          | 0                 |             |
| Sprinter_Chance                 | float | 0              | 0.15             | 0.175          | 0                 |             |
| Flanker_Chance                  | float | 0              | 0.025            | 0.05           | 0                 |             |
| Burner_Chance                   | float | 0              | 0.025            | 0.05           | 0                 |             |
| Acid_Chance                     | float | 0              | 0.025            | 0.05           | 0                 |             |
| Boss_Electric_Chance            | float | 0              | 0                | 0              | 0                 |             |
| Boss_Wind_Chance                | float | 0              | 0                | 0              | 0                 |             |
| Boss_Fire_Chance                | float | 0              | 0                | 0              | 0                 |             |
| Spirit_Chance                   | float | 0              | 0                | 0              | 0                 |             |
| DL_Red_Volatile_Chance          | float | 0              | 0                | 0              | 0                 |             |
| DL_Blue_Volatile_Chance         | float | 0              | 0                | 0              | 0                 |             |
| Boss_Elver_Stomper_Chance       | float | 0              | 0                | 0              | 0                 |             |
| Boss_Kuwait_Chance              | float | 0              | 0                | 0              | 0                 |             |
| Respawn_Day_Time                | float | 360            | 360              | 360            | 360               |             |
| Respawn_Night_Time              | float | 30             | 30               | 30             | 30                |             |
| Respawn_Beacon_Time             | float | 0              | 0                | 0              | 0                 |             |
| Quest_Boss_Respawn_Interval     | float | 600            | 600              | 600            | 600               |             |
| Damage_Multiplier               | float | 0.75           | 1                | 1.5            | 1                 |             |
| Armor_Multiplier                | float | 1.25           | 1                | 0.75           | 1                 |             |
| Backstab_Multiplier             | float | 1.25           | 1.25             | 1.25           | 1.25              |             |
| NonHeadshot_Armor_Multiplier    | float | 1              | 1                | 1              | 1                 |             |
| Beacon_Experience_Multiplier    | float | 1              | 1                | 1              | 1                 |             |
| Full_Moon_Experience_Multiplier | float | 2              | 2                | 2              | 2                 |             |
| Min_Drops                       | uint  | 1              | 1                | 1              | 1                 |             |
| Max_Drops                       | uint  | 1              | 1                | 1              | 1                 |             |
| Min_Mega_Drops                  | uint  | 5              | 5                | 5              | 5                 |             |
| Max_Mega_Drops                  | uint  | 5              | 5                | 5              | 5                 |             |
| Min_Boss_Drops                  | uint  | 8              | 8                | 8              | 8                 |             |
| Max_Boss_Drops                  | uint  | 10             | 10               | 10             | 10                |             |
| Slow_Movement                   | bool  | TRUE           | FALSE            | FALSE          | FALSE             |             |
| Can_Stun                        | bool  | TRUE           | TRUE             | FALSE          | TRUE              |             |
| Only_Critical_Stuns             | bool  | FALSE          | FALSE            | TRUE           | FALSE             |             |
| Weapons_Use_Player_Damage       | bool  | FALSE          | FALSE            | TRUE           | FALSE             |             |
| Can_Target_Barricades           | bool  | TRUE           | TRUE             | TRUE           | TRUE              |             |
| Can_Target_Structures           | bool  | TRUE           | TRUE             | TRUE           | TRUE              |             |
| Can_Target_Vehicles             | bool  | TRUE           | TRUE             | TRUE           | TRUE              |             |
| Beacon_Max_Rewards              | uint  | 0              | 0                | 0              | 0                 |             |
| Beacon_Max_Participants         | uint  | 0              | 0                | 0              | 0                 |             |
| Beacon_Rewards_Multiplier       | bool  | 1              | 1                | 1              | 1                 |             |

### Animals

| Key                       | Value | Default (Easy) | Default (Normal) | Default (Hard) | Default (Default) | Description |
| :------------------------ | :---- | :------------- | :--------------- | :------------- | :---------------- | :---------- |
| Respawn_Time              | float | 180            |                  |                |                   |             |
| Damage_Multiplier         | float | 0.75           | 1                | 1.5            | 1                 |             |
| Armor_Multiplier          | float | 1.25           | 1                | 0.75           | 1                 |             |
| Max_Instances_Tiny        | uint  | 4              | 4                | 4              | 4                 |             |
| Max_Instances_Small       | uint  | 8              | 8                | 8              | 8                 |             |
| Max_Instances_Medium      | uint  | 16             | 16               | 16             | 16                |             |
| Max_Instances_Large       | uint  | 32             | 32               | 32             | 32                |             |
| Max_Instances_Insane      | uint  | 64             | 64               | 64             | 64                |             |
| Weapons_Use_Player_Damage | bool  | FALSE          | FALSE            | TRUE           | FALSE             |             |

### Barricades

| Key                             | Value   | Default (Easy) | Default (Normal) | Default (Hard) | Default (Default) | Description |
| :------------------------------ | :------ | :------------- | :--------------- | :------------- | :---------------- | :---------- |
| Decay_Time                      | uint    | 604800         | 604800           | 604800         | 604800            |             |
| Armor_Lowtier_Multiplier        | float   | 1              | 1                | 1              | 1                 |             |
| Armor_Hightier_Multiplier       | float   | 0.5            | 0.5              | 0.5            | 0.5               |             |
| Gun_Lowcal_Damage_Multiplier    | float   | 1              | 1                | 1              | 1                 |             |
| Gun_Highcal_Damage_Multiplier   | float   | 1              | 1                | 1              | 1                 |             |
| Melee_Damage_Multiplier         | float   | 1              | 1                | 1              | 1                 |             |
| Melee_Repair_Multiplier         | float   | 1              | 1                | 1              | 1                 |             |
| Allow_Item_Placement_On_Vehicle | boolean | TRUE           | TRUE             | TRUE           | TRUE              |             |
| Allow_Trap_Placement_On_Vehicle | boolean | TRUE           | TRUE             | TRUE           | TRUE              |             |
| Max_Item_Distance_From_Hull     | float   | 64             | 64               | 64             | 64                |             |
| Max_Trap_Distance_From_Hull     | float   | 16             | 16               | 16             | 16                |             |

### Structures

| Key                           | Value | Default (Easy) | Default (Normal) | Default (Hard) | Default (Default) | Description |
| :---------------------------- | :---- | :------------- | :--------------- | :------------- | :---------------- | :---------- |
| Decay_Time                    | uint  | 604800         | 604800           | 604800         | 604800            |             |
| Armor_Lowtier_Multiplier      | float | 1              | 1                | 1              | 1                 |             |
| Armor_Hightier_Multiplier     | float | 0.5            | 0.5              | 0.5            | 0.5               |             |
| Gun_Lowcal_Damage_Multiplier  | float | 1              | 1                | 1              | 1                 |             |
| Gun_Highcal_Damage_Multiplier | float | 1              | 1                | 1              | 1                 |             |
| Melee_Damage_Multiplier       | float | 1              | 1                | 1              | 1                 |             |
| Melee_Repair_Multiplier       | float | 1              | 1                | 1              | 1                 |             |

### Players

| Key                       | Value   | Default (Easy) | Default (Normal) | Default (Hard) | Default (Default) | Description                                                        |
| :------------------------ | :------ | :------------- | :--------------- | :------------- | :---------------- | :----------------------------------------------------------------- |
| Health_Default            | uint    | 100            | 100              | 100            | 100               |                                                                    |
| Health_Regen_Min_Food     | uint    | 90             | 90               | 90             | 90                |                                                                    |
| Health_Regen_Min_Water    | uint    | 90             | 90               | 90             | 90                |                                                                    |
| Health_Regen_Ticks        | uint    | 60             | 60               | 60             | 60                |                                                                    |
| Food_Default              | uint    | 100            | 100              | 85             | 100               |                                                                    |
| Food_Use_Ticks            | uint    | 350            | 300              | 250            | 300               |                                                                    |
| Food_Damage_Ticks         | uint    | 15             | 15               | 15             | 15                |                                                                    |
| Water_Default             | uint    | 100            | 100              | 85             |                   |                                                                    |
| Water_Use_Ticks           | uint    | 320            | 270              | 220            | 270               |                                                                    |
| Water_Damage_Ticks        | uint    | 20             | 20               | 20             | 20                |                                                                    |
| Virus_Default             | uint    | 100            | 100              | 100            | 100               |                                                                    |
| Virus_Infect              | uint    | 50             | 50               | 50             | 50                |                                                                    |
| Virus_Use_Ticks           | uint    | 125            | 125              | 125            | 125               |                                                                    |
| Virus_Damage_Ticks        | uint    | 25             | 25               | 25             | 25                |                                                                    |
| Leg_Regen_Ticks           | uint    | 750            | 750              | 750            | 750               |                                                                    |
| Bleed_Damage_Ticks        | uint    | 10             | 10               | 10             | 10                |                                                                    |
| Bleed_Regen_Ticks         | uint    | 750            | 750              | 750            | 750               |                                                                    |
| Armor_Multiplier          | float   | 1              | 1                | 1              | 1                 |                                                                    |
| Experience_Multiplier     | float   | 1.5            | 1                | 1.5            | 10                |                                                                    |
| Detect_Radius_Multiplier  | float   | 0.5            | 1                | 1.25           | 1                 |                                                                    |
| Ray_Aggressor_Distance    | float   | 8              | 8                | 8              | 8                 |                                                                    |
| Lose_Skills_PvP           | float   | 0.75           | 0.75             | 0.75           | 0.75              | Percentage of skills kept after death                              |
| Lose_Skills_PvE           | float   | 0.75           | 0.75             | 0.75           | 0.75              | Percentage of skills kept after death                              |
| Lose_Items_PvP            | float   | 1              | 1                | 1              | 1                 | Percentage of items kept after death                               |
| Lose_Items_PvE            | float   | 1              | 1                | 1              | 1                 | Percentage of items kept after death                               |
| Lose_Clothes_PvP          | boolean | TRUE           | TRUE             | TRUE           | TRUE              | If Clothes will drop when killed by a player.                      |
| Lose_Clothes_PvE          | boolean | TRUE           | TRUE             | TRUE           | TRUE              | If Clothes will drop when killed.                                  |
| Lose_Weapons_PvP          | boolean | TRUE           | TRUE             | TRUE           | TRUE              | If Weapons will drop when killed by a player.                      |
| Lose_Weapons_PvE          | boolean | TRUE           | TRUE             | TRUE           | TRUE              | If Weapons will drop when killed.                                  |
| Can_Hurt_Legs             | boolean | TRUE           | TRUE             | TRUE           | TRUE              |                                                                    |
| Can_Break_Legs            | boolean | FALSE          | TRUE             | TRUE           | TRUE              | If a players legs can break                                        |
| Can_Fix_Legs              | boolean | TRUE           | TRUE             | FALSE          | TRUE              | If broken legs heal without a splint.                              |
| Can_Start_Bleeding        | boolean | FALSE          | TRUE             | TRUE           | TRUE              | If a player can start bleeding                                     |
| Can_Stop_Bleeding         | boolean | TRUE           | TRUE             | FALSE          | TRUE              | If bleeding will stop without a bandage                            |
| Spawn_With_Max_Skills     | boolean | FALSE          | FALSE            | FALSE          | FALSE             | Players spawn with all skills maxed (does not apply retroactively) |
| Spawn_With_Stamina_Skills | boolean | FALSE          | FALSE            | FALSE          | FALSE             | Players spawn with all stamina related skills maxed                |
| Allow_Instakill_Headshots | boolean | FALSE          | FALSE            | TRUE           | FALSE             |                                                                    |
| Allow_Per_Character_Saves | boolean | TRUE           | TRUE             | TRUE           | TRUE              | Server allows each indvidual saves per player character            |

### Objects

| Key                           | Value   | Default (Easy) | Default (Normal) | Default (Hard) | Default (Default) | Description |
| :---------------------------- | :------ | :------------- | :--------------- | :------------- | :---------------- | :---------- |
| Binary_State_Reset_Multiplier | float   |                |                  |                | 1                 |             |
| Fuel_Reset_Multiplier         | float   |                |                  |                | 1                 |             |
| Water_Reset_Multiplier        | float   |                |                  |                | 1                 |             |
| Resource_Reset_Multiplier     | float   |                |                  |                | 1                 |             |
| Resource_Drops_Multiplier     | float   |                |                  |                | 1                 |             |
| Rubble_Reset_Multiplier       | float   |                |                  |                | 1                 |             |
| Allow_Holiday_Drops           | boolean |                |                  |                | TRUE              |             |
| Items_Obstruct_Tree_Respawns  | boolean |                |                  |                | TRUE              |             |

### Events

| Key                                     | Value   | Default (Easy) | Default (Normal) | Default (Hard) | Default (Default) | Description                      |
| :-------------------------------------- | :------ | :------------- | :--------------- | :------------- | :---------------- | :------------------------------- |
| Rain_Frequency_Min                      | float   |                |                  |                | 2.3               |                                  |
| Rain_Frequency_Max                      | float   |                |                  |                | 5.6               |                                  |
| Rain_Duration_Min                       | float   |                |                  |                | 0.05              | Set Min and Max to 0 to disable. |
| Rain_Duration_Max                       | float   |                |                  |                | 0.15              | Set Min and Max to 0 to disable. |
| Snow_Frequency_Min                      | float   |                |                  |                | 1.3               |                                  |
| Snow_Frequency_Max                      | float   |                |                  |                | 4.5               |                                  |
| Snow_Duration_Min                       | float   |                |                  |                | 0.2               | Set Min and Max to 0 to disable. |
| Snow_Duration_Max                       | float   |                |                  |                | 0.5               | Set Min and Max to 0 to disable. |
| Weather_Frequency_Multiplier            | float   |                |                  |                | 1                 |                                  |
| Weather_Duration_Multiplier             | float   |                |                  |                | 1                 |                                  |
| Airdrop_Frequency_Min                   | float   |                |                  |                | 0.8               |                                  |
| Airdrop_Frequency_Max                   | float   |                |                  |                | 6.5               |                                  |
| Airdrop_Speed                           | float   |                |                  |                | 128               |                                  |
| Airdrop_Force                           | float   |                |                  |                | 9.5               |                                  |
| Arena_Min_Players                       | uint    |                |                  |                | 2                 |                                  |
| Arena_Compactor_Damage                  | uint    |                |                  |                | 9                 |                                  |
| Arena_Compactor_Extra_Damage_Per_Second | float   |                |                  |                | 1                 |                                  |
| Arena_Clear_Timer                       | uint    |                |                  |                | 5                 |                                  |
| Arena_Finale_Timer                      | uint    |                |                  |                | 10                |                                  |
| Arena_Restart_Timer                     | uint    |                |                  |                | 15                |                                  |
| Arena_Compactor_Delay_Timer             | uint    |                |                  |                | 1                 |                                  |
| Arena_Compactor_Pause_Timer             | uint    |                |                  |                | 5                 |                                  |
| Use_Airdrops                            | boolean |                |                  |                | TRUE              |                                  |
| Arena_Use_Compactor_Pause               | boolean |                |                  |                | TRUE              |                                  |
| Arena_Compactor_Speed_Tiny              | float   |                |                  |                | 0.5               |                                  |
| Arena_Compactor_Speed_Small             | float   |                |                  |                | 1.5               |                                  |
| Arena_Compactor_Speed_Medium            | float   |                |                  |                | 3                 |                                  |
| Arena_Compactor_Speed_Large             | float   |                |                  |                | 4.5               |                                  |
| Arena_Compactor_Speed_Insane            | float   |                |                  |                | 6                 |                                  |
| Arena_Compactor_Shrink_Factor           | float   |                |                  |                | 0.5               |                                  |

### Gameplay

| Key                                 | Value | Default (Easy) | Default (Normal) | Default (Hard) | Default (Default) | Description                      |
| :---------------------------------- | :---- | :------------- | :--------------- | :------------- | :---------------- | :------------------------------- |
| Repair_Level_Max                    | uint  |                |                  |                | 3                 |                                  |
| Hitmarkers                          | bool  | TRUE           | TRUE             | FALSE          | TRUE              |                                  |
| Crosshair                           | bool  | TRUE           | TRUE             | FALSE          | TRUE              |                                  |
| Ballistics                          | bool  | FALSE          | TRUE             | TRUE           | TRUE              |                                  |
| Chart                               | bool  | TRUE           |                  |                | FALSE             |                                  |
| Satellite                           | bool  |                |                  |                | FALSE             |                                  |
| Compass                             | bool  |                |                  |                | FALSE             |                                  |
| Group_Map                           | bool  |                |                  | FALSE          | TRUE              |                                  |
| Group_HUD                           | bool  |                |                  |                | TRUE              |                                  |
| Group_Player_List                   | bool  |                |                  |                | TRUE              |                                  |
| Allow_Static_Groups                 | bool  |                |                  |                | TRUE              |                                  |
| Allow_Dynamic_Groups                | bool  |                |                  |                | TRUE              |                                  |
| Allow_Shoulder_Camera               | bool  |                |                  |                | TRUE              |                                  |
| Can_Suicide                         | bool  |                |                  |                | TRUE              |                                  |
| Friendly_Fire                       | bool  |                |                  |                | FALSE             |                                  |
| Bypass_Buildable_Mobility           | bool  |                |                  |                | FALSE             | Defaults to True on singleplayer |
| Allow_Holidays                      | bool  | TRUE           |                  |                |                   |                                  |
| MAX_TIMER_EXIT                      |       |                |                  |                |                   |                                  |
| Timer_Exit                          | uint  |                |                  |                | 10                |                                  |
| Timer_Respawn                       | uint  |                |                  |                | 10                |                                  |
| Timer_Home                          | uint  |                |                  |                | 30                |                                  |
| Timer_Leave_Group                   | uint  |                |                  |                | 30                |                                  |
| Max_Group_Members                   | uint  |                |                  |                | 0                 |                                  |
| Explosion_Launch_Speed_Multiplier   | float | 1              |                  |                |                   |                                  |
| AirStrafing_Acceleration_Multiplier | float | 1              |                  |                |                   |                                  |
| AirStrafing_Deceleration_Multiplier | float | 1              |                  |                |                   |                                  |