# Objects

Objects are models that can be placed onto maps. Some objects can be traveled through, interacted with, or just be there for aesthetic value. Objects can be spawned in with the `E` key by default. These objects can then be translated, scaled, and rotated; they can also be snapped to a grid-like placement system by holding `Ctrl`.

!!! warning
    Player-made structures and barricades can be placed via the map editor, but these SHOULD NOT be used (i.e. people can salvage them and world savedata has to be reset for ones added in updates).

## Favorite Searches

The objects editor supports __Favorite Searches__ which allows lists of objects to be quickly looked up.

Entering "fv:xyz" in the search bar loads xyz.txt from the game folder, and will match any of the lines in the file. Empty lines and lines starting with "//" (comments) are ignored. The .txt file extension was chosen because it is the notepad default.

For example this matches anything with "fire" in the name or Road Line Cap #1:

    // Fire related props
    Fire

    // Specific road prop
    Cap #1 Road Line

Recursive usage of filters is supported, so multiple favorite searches can be nested, or other filter types e.g. "Tunnel mb:core" includes tunnels from the vanilla objects.

## Editor Asset Redirectors

If many objects need to be replaced on a map the old object guid can be redirected to a new guid rather than manually replacing them. This works similarly to the automatic holiday object replacements, but applies while loading a map in the editor, and changes are kept when the map is saved.

The game looks for a file named "EditorAssetRedirectors.txt" in the Unturned folder. Empty lines and lines starting with `//` or `#` (comments) are ignored. The .txt file extension was chosen because it is the notepad default. Each line contains two guids separated by an arrow `->`.

For example:

	// Replace Boulder_00 with Boulder_01
	6125b4de591b44359237f6d7191dd919 -> ee402fc9debe4f03bffb31a49eb04fb7

	// Replace Grass_1 with Grass_France_1
	9a9655656f704b3caf717cea5a3b3cc2 -> d6dc5cc36f43429da668525e6ad174da

