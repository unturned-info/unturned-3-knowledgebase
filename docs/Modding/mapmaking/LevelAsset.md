# Level Asset

Each map can be associated with a **Level Asset**. These assets contain gameplay information not necessary for the main menus. Refer to [Level Config](LevelConfig.md) for information on linking a level asset to a map.

For examples check the `Assets/Levels` directory.

`Dropship` [Master Bundle Pointer](../MasterBundlePtr.md): Overrides the model seen flying over the map when a care package is dropped.

`Airdrop` [Asset Pointer](../AssetPtr.md): to an [Airdrop Asset](../AirdropAsset.md). Overrides the falling care package model.

`Crafting_Blacklists` array of [Asset Pointers](../AssetPtr.md) to [Crafting Blacklist(s)](../../Server-Hosting/Extending-Servers/CraftingBlacklistAsset.md). Prevents specific items or blueprints from being used while crafting in the level.

`Loading_Screen_Music`: contains `Loop` and `Outro` that are [Asset Pointers](../AssetPtr.md) to audio files for loading screen music.

This is an [Asset v2](../AssetTypes/AssetsV2.md) class.
