# Creating Plugins

!!! note The following documentation is for RocketMod (LDM).
!!! info
    Creating plugins for Unturned requires a general knowledge of C#. If you currently do not have any knowledge behind C#, please check out [Microsoft's introduction to the language.](https://dotnet.microsoft.com/en-us/learntocode "dotnet.microsoft.com/en-us/learntocode")

All plugins normally begin with public class that inherits the `RocketPlugin` class. Below is an example of how to properly implement this:

```csharp
using Rocket.API;
using Rocket.Core.Plugins;

namespace ExamplePlugin
{
    public class ExamplePlugin : RocketPlugin
    {

    }
}
```

Notice how the `ExamplePlugin` class is public? This is so we can make it accessible to RocketMod.

Moving on, you can now override the `Load` and `Unload` methods contained within the `RocketPlugin` class to log the loading and unloading of your plugin:

```csharp
using Rocket.API;
using Rocket.Core.Plugins;
using Rocket.Unturned;
using Rocket.Unturned.Chat;
using Rocket.Unturned.Player;
using Rocket.Core.Logging;

namespace ExamplePlugin
{
    public class ExamplePlugin : RocketPlugin
    {
        protected override void Load()
        {
            Logger.Log("Example plugin loaded!");
        }

        protected override void Unload()
        {
            Logger.Log("Example plugin unloaded!");
        }
    }
}
```
The plugin will also now log in the server console that the plugin has been loaded and unloaded.

You can also subscribe and unsubscribe to events when the plugin loads and unloads:

```csharp
using Rocket.API;
using Rocket.Core.Plugins;
using Rocket.Unturned;
using Rocket.Core.Logging;

namespace ExamplePlugin
{
    public class ExamplePlugin : RocketPlugin
    {
        protected override void Load()
        {
            Logger.Log("Example plugin loaded!");

            U.Events.OnPlayerConnected += OnPlayerConnected;
        }

        protected override void Unload()
        {
            Logger.Log("Example plugin unloaded!");

            U.Events.OnPlayerConnected -= OnPlayerConnected;
        }

        public void OnPlayerConnected(UnturnedPlayer player)
        {
        }
    }
}
```

The plugin will subscribe and unsubscribe to the `U.Events.OnPlayerConnected`event on load and unload.

You can also now greet the player when they connect to the server:

```csharp
using Rocket.API;
using Rocket.Core.Plugins;
using Rocket.Unturned;
using Rocket.Core.Logging;

namespace ExamplePlugin
{
    public class ExamplePlugin : RocketPlugin
    {
        protected override void Load()
        {
            Logger.Log("Example plugin loaded!");

            U.Events.OnPlayerConnected += OnPlayerConnected;
        }

        protected override void Unload()
        {
            Logger.Log("Example plugin unloaded!");

            U.Events.OnPlayerConnected -= OnPlayerConnected;
        }

        public void OnPlayerConnected(UnturnedPlayer player)
        {
            // Do something when a player connects
            UnturnedChat.Say(player, "Welcome to the server!");
        }
    }
}
```

To conclude, This plugin will log a message when it is loaded and unloaded, and greet players when they connect to the server. Of course, you can customize the plugin to do whatever you want it to do.