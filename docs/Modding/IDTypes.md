# ID Types

!!! info
    As of version [3.22.19.0](https://store.steampowered.com/news/app/304930/view/5940838760381455590), there are plans to switch from the legacy IDs to GUIDs.

## GUIDs

Globally Unique Identifiers (**GUID**s) are 32 digit numbers used to identify assets. They are preferable to file names because the files can be moved without redirectors.

At the time of writing a useful tool for generating GUIDs is: https://www.guidgenerator.com/

## IDs

Legacy IDs are unsigned 16 bit integers with a [0, 65535] range, whereas GUIDs are 128 bits with an unimaginably huge range. This allows them to be generated without coordination or registration between developers. The main goal is to replace the legacy ushort IDs with GUIDs. For instance, in future versions past [3.23.4.0](https://store.steampowered.com/news/app/304930/view/3712694972139442648), Object asset types will no longer need legacy ushort IDs to function properly. It is quite important to note that while the legacy IDs are used mainly, asset conflicts can still occur with GUIDs.
