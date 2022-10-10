# Upgrading Unity

!!! attention
    Unturned is now running on Unity 2020.3 LTS.

## Asset Bundles

!!! info
    Old .content files no longer work beginning in version [3.22.4.0](https://store.steampowered.com/news/app/304930/view/3128317225029095852 "3.22.4.0"). It is recommended that developers switch to supported .masterbundle files.

Older .unity3d/.masterbundle files should work properly without needing any update unless they use custom shaders. The game automatically tries to consolidate their shaders with the latest versions during loading. Once re-exported, Asset_Bundle_Version can be set to 3 for 2018.4/2019.4 LTS and 4 for 2020.3 LTS in MasterBundle.dat or individual .dat files to disable this shader consolidation step.

Some of the slower asset checks like finding missing meshes have been made optional. Running the game with the "-ValidateAssets" command-line option enables them, and is recommended while working on new content.

## Unity Packages

All example content has been updated since 2018.4 LTS, and now has a consistent export process to ensure the contents are kept valid. What were once individual packages (e.g. All_Shaders.unitypackage) have been merged into a single ExampleAssets.unitypackage in the Bundles/Sources/Examples directory.

## Logging / Server Console

Usage of Unity's built-in Debug.Log has been replaced with logging to the Client.log or Server_XYZ.log files in the Logs folder. This works around conflict with standard output on the Linux server, so -logfile redirect workarounds should no longer be necessary. -ThreadedConsole implementation has been made the default, but can be disabled by -LegacyConsole.

## Workshop

Uploads from the latest version of Unity are incompatible with game versions using earlier versions, and a warning message is shown when loading newer content into older versions.

## Past Version Availability

For archival purposes the 2017.4, 2018.4, and 2019.4 LTS versions of the game will remain in the "unity-2017.4", "unity-2018.4", and "unity-2019.4" beta branches.

## Platforms

!!! info
    Unturned no longer supports any 32-bit systems beginning after version [3.22.14.0](https://store.steampowered.com/news/app/304930/view/3398548424201939049 "3.22.14.0").

Linux 32-bit and MacOS 32-bit have been removed in favor of the 64-bit versions. Servers that were still using the outdated Linux 32-bit depot should update to the 64-bit Linux dedicated server.

Headless server files have been removed from the player Linux depot, and are instead only in the dedicated server Linux depot. Windows headless mode is now supported in 2018.4 LTS and later versions, and is enabled for the Windows dedicated server depot.
