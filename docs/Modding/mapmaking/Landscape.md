# Landscape

## Considerations

Upgrading terrain from the legacy editor to the devkit editor is not necessarily recommended.

Pros:

- Height sculpting and material painting tools are better.
- Each 1km x 1km tile has its own set of 8 materials rather than 8 for the entire level.

Cons:

- Devkit is not user-friendly, and improvements to it have been voted low priority.
- Not all legacy editor features have been ported.

## Upgrade Legacy Terrain to Landscape


!!! info
    Beginning in version [3.22.9.0](https://store.steampowered.com/news/app/304930/view/3212766758952510190 "3.22.9.0"), all legacy terrain will be converted automatically to the devkit landscape terrain. Additionally, devkit landscape terrain can now be edited within the regular legacy map editor.

1. Level should have only one Landscape instance spawned from the Type Browser.
2. Open the Ground Upgrade Wizard.
3. Assign materials in the same order as in the original map editor. For example, if dirt is top of the list in the legacy editor then assign dirt to material slot #0.
4. Click upgrade and wait for the data to transfer. This may take a while.
5. Save the level.
6. Change `Use_Legacy_Ground` to false in the [Level Config](LevelConfig.md) file.
