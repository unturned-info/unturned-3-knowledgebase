# Foliage

## Upgrade Devkit Foliage from V1 to V2

!!! info
    Beginning in version [3.22.9.0](https://store.steampowered.com/news/app/304930/view/3212766758952510190 "3.22.9.0"), all foliage will be converted automatically to the devkit foliage. Additionally, devkit foliage can now be edited within the regular legacy map editor.

V1 of devkit foliage unfortunately saved small individual regions into their own files, which makes maps slow to copy, download and install. V2 fixes this by storing pointers for each region into a single file at the cost of RAM in editor.

1. Run game with the `-SaveFoliageUsingV2` command-line argument.
2. Open a foliage V1 level in the devkit editor.
3. Resave level.
4. Move the level's Foliage directory elsewhere as a backup just in case.
