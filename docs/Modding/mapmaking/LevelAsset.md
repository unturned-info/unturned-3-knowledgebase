# Level Asset

Each map can be associated with a **Level Asset**. These assets contain gameplay information not necessary for the main menus. Refer to [Level Config](LevelConfig.md) for information on linking a level asset to a map.

For examples check the `Assets/Levels` directory.

`Dropship` [Master Bundle Pointer](../MasterBundlePtr.md): Overrides the model seen flying over the map when a care package is dropped.

`Airdrop` [Asset Pointer](../AssetPtr.md): to an [Airdrop Asset](../AirdropAsset.md). Overrides the falling care package model.

`Crafting_Blacklists` array of [Asset Pointers](../AssetPtr.md) to [Crafting Blacklist(s)](../../Server-Hosting/Extending-Servers/CraftingBlacklistAsset.md). Prevents specific items or blueprints from being used while crafting in the level.

This is an [Asset v2](../AssetTypes/AssetsV2.md) class.

## Programmer Methods & Properties

`public static AssetReference<LevelAsset> defaultLevel` - The AssetReference to the default level asset.

`public TypeReference<GameMode> defaultGameMode` - The TypeReference to the default game mode.

`public InspectableList<TypeReference<GameMode>> supportedGameModes` - N/A

`public MasterBundleReference<GameObject> dropshipPrefab` - The MasterBundleReference to the dropship prefab specified using the Dropship asset property.

`public AssetReference<AirdropAsset> airdropRef` - The AssetReference to the airdrop asset specified using the Airdrop asset property.

`public float minStealthRadius` - No context needed.

`public float fallDamageSpeedThreshold` - No context needed.

`public bool enableAdminFasterSalvageDuration = true` - No context needed.

`public List<AssetReference<CraftingBlacklistAsset>> craftingBlacklists` - List of crafting blacklist assets.

`public LevelAsset.SchedulableWeather[] schedulableWeathers` - Array of SchedulableWeather.

`public struct SchedulableWeather { public AssetReference<WeatherAssetBase> assetRef; public float minFrequency; public float maxFrequency; public float minDuration; public float maxDuration; }` - A struct containing a AssetReference to the weather asset, a minimum weather frequency value, maximum weather frequency value, a minimum weather duration, and a maximum weather duration value.

`public AssetReference<WeatherAssetBase> perpetualWeatherRef` - N/A

`public LevelAsset.LoadingScreenMusic[] loadingScreenMusic` - Array of LoadingScreenMusic.

`public struct LoadingScreenMusic { public MasterBundleReference<AudioClip> loopRef; public MasterBundleReference<AudioClip> outroRef; public float loopVolume; public float outroVolume; }` - A struct containing a MasterBundleReference to the AudioClip that should loop while loading, a MasterBundleReference to the AudioClip that should play when fully loaded into the level, a volume value for how loud the loop music should be, and a volume value for how loud the outro music should be.

`public bool shouldAnimateBackgroundImage` - Specifies if the background image shown when loading into the map is animated or not.

`public uint globalWeatherMask` - No context needed.

`public LevelAsset.SkillRule[][] skillRules` - Array of SkillRule.

`public class SkillRule { public int defaultLevel; public int maxUnlockableLevel; public float costMultiplier; }` - A struct containing the default level value, the max level the skill can go up to, and the cost multiplier value.

`public bool hasClouds` - Specifies if the level has clouds.

`public bool isBlueprintBlacklisted(Blueprint blueprint)` - Returns true or false if the blueprint is blacklisted or not. Just note that it will return false if there is no crafting blacklists for the level asset or if the blueprint is null.