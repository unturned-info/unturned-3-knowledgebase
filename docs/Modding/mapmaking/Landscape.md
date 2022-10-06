# Landscape

## Upgrade Legacy Terrain to Landscape

!!! info
    Beginning in version [3.22.9.0](https://store.steampowered.com/news/app/304930/view/3212766758952510190 "3.22.9.0"), all legacy terrain will be converted automatically to the devkit landscape terrain. Additionally, devkit landscape terrain can now be edited within the regular legacy map editor.

1. Level should have only one Landscape instance spawned from the Type Browser.
2. Open the Ground Upgrade Wizard.
3. Assign materials in the same order as in the original map editor. For example, if dirt is top of the list in the legacy editor then assign dirt to material slot #0.
4. Click upgrade and wait for the data to transfer. This may take a while.
5. Save the level.
6. Change `Use_Legacy_Ground` to false in the [Level Config](LevelConfig.md) file.

## Landscape Hole Volume

!!! info
    Beginning in version [3.22.9.0](https://store.steampowered.com/news/app/304930/view/3212766758952510190 "3.22.9.0"), all landscape hole volumes will be automatically converted to the new cut tool feature.
    
1. Open your map in the DevKit and navigate to your type browser.
2. Click on core and then on landscape hole volume, then using the selection tool press `E` to place a landscape hole volume.
3. You can cycle between different types of tools using `Q`, `W`, and `R`, which allow you to transform, rotate, and scale the volume.

## Underground Whitelist Volume

To make sure that people don't glitch under your map, you can use underground whitelist volumes. These will teleport players under the map outside of any whitelist volume to the surface.

1. To enable this feature, go to your map's Config.json and set the `Use_Underground_Whitelist` line to `true`.
2. Open your map in the legacy map editor and navigate to the Volumes tab within the Level tab.
3. Click on underground whitelist volume, then press `E` to place a underground whitelist volume.
4. You can cycle between different types of tools using `Q`, `W`, and `R`, which allow you to transform, rotate, and scale the volume.
