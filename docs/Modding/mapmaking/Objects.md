# Objects

Objects are models that can be placed onto maps. Some objects can be travled through, interacted with, or just be there for aesthetic value. Objects can be spawned in with the `E` key by default. These objects can then be tranlated, scaled, and rotated; they can also be snapped to a grid-like placement system by holding `Ctrl`.

!!! warning
    Player-made structures and barricades can be placed via the map editor, but these SHOULD NOT be used (i.e. people can salvage them and world savedata has to be reset for ones added in updates).

### Favorite Searches

The objects editor supports __Favorite Searches__ which allows lists of objects to be quickly looked up.

Entering "fv:xyz" in the search bar loads xyz.txt from the game folder, and will match any of the lines in the file. Empty lines and lines starting with "//" (comments) are ignored. The .txt file extension was chosen because it is the notepad default.

For example this matches anything with "fire" in the name or Road Line Cap #1:

    // Fire related props
    Fire

    // Specific road prop
    Cap #1 Road Line

Recursive usage of filters is supported, so multiple favorite searches can be nested, or other filter types e.g. "Tunnel mb:core" includes tunnels from the vanilla objects.
