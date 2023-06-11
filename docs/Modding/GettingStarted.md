# Getting Started with Modding

!!! info
    Looking for plugin documentation? visit [ldmcommunity.net](https://ldmcommunity.net/docs/ "https://ldmcommunity.net/docs/")

Installing the Unity Editor is required for exporting custom content into the game. 2020.3.38f1 (or 2019.4, if still installed) LTS version should be compatible. [View Download Links](https://unity.com/releases/editor/qa/lts-releases?version=2020.3)

Once Unity is installed a project can be created to house custom content. At this point it is recommended to import Unturned's provided source packages:

1. Inside Unity open the Assets > Import Package > Custom Package... wizard.
2. Find the Unturned installation directory.
3. Navigate to the Bundles/Sources directory.
4. Import the Project.unitypackage, and optionally the ExampleAssets.unitypackage.

## Project.unitypackage

This package contains the barebones required to export custom content:

- [Asset Bundling Tools](AssetBundles.md)
- Default Project Settings
- [(Optional) Mod Hooks](ModHooks.md)

## ExampleAssets.unitypackage

This package contains vanilla content examples, and several useful prefabs:

- CoreMasterBundle directory has at least one example of each piece of vanilla content.
- Animations directory has all of the vanilla item animations for re-use.
- Assets/Resources/Characters/Preview.prefab is helpful for previewing clothes.

!!! warning
    Custom content should NOT be placed into the CoreMasterBundle, instead create a separate directory or place your custom content in the Sandbox folder located in your local game files.
