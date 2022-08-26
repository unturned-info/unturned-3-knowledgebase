# Master Bundle Pointer

Identifies a Unity asset like a prefab, material or audio clip within a master bundle.

## In \*.asset files

`MasterBundle`: File name of the asset bundle exported from Unity. Should match the `Asset_Bundle_Name` configured in the `MasterBundle.dat` file.

`AssetPath`: File path of the Unity asset e.g. \*.prefab, \*.mat, \*.png, \*.ogg, etc. Relative to the `Asset_Prefix` path configured in the `MasterBundle.dat` file.

"MyMasterBundlePtr"
{
    "MasterBundle" "core.masterbundle"
    "AssetPath" "path/to/file.extension"
}

If the asset default master bundle should be used then the path can be specified inline:

```"MyMasterBundlePtr" "path/to/file.extension"```

## in \*.dat files

For .dat files, you'll want to put the masterbundle name and its extension behind a `:` in the front of your file path. For example, if I want to get an AudioClip from the core masterbundle:

```core.masterbundle:Sounds/DrinkSwallow.mp3```

This works for .dat lines like ConsumeAudioClip and HornAudioClip.
