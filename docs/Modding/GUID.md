# GUID

!!! info
    As of version [3.22.19.0]([https://store.steampowered.com/news/app/304930/view/3212766758952510190](https://store.steampowered.com/news/app/304930/view/5940838760381455590) "3.22.19.0"), there is appearent plans to switch from the legacy IDs to GUIDs.

Globally Unique Identifiers (**GUID**s) are 32 digit numbers used to identify assets. They are preferable to file names because the files can be moved without redirectors.

At the time of writing a useful tool for generating GUIDs is: https://www.guidgenerator.com/

Legacy IDs are unsigned 16 bit integers with a [0, 65535] range, whereas GUIDs are 128 bits with an unimaginably huge range. This allows them to be generated without coordination or registration between developers. The main goal was to replace the legacy ushort IDs with GUIDs, but that goal fell out of reach. It is quite important to note that while the legacy IDs are used mainly, asset conflicts can still occur with GUIDs.
