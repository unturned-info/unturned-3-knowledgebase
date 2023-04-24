# Changing Chat Color

!!! note The following documentation is for RocketMod (LDM).

By listening for `UnturnedPlayerEvents.OnPlayerChatted` within `Rocket.Unturned.Events`, you can change the chat color of a player's messages to pink:

```csharp
using Rocket.Core.Plugins;
using Rocket.Unturned.Player;
using Rocket.Unturned.Chat;
using Rocket.Unturned.Events;
using UnityEngine;

namespace MyAwesomePlugins
{
    public class ChatColor : RocketPlugin
    {
        protected override void Load()
        {
            UnturnedPlayerEvents.OnPlayerChatted += OnPlayerChatted;
        }

        private void OnPlayerChatted(UnturnedPlayer player, ref Color color, string message, EChatMode chatMode, ref bool cancel)
        {
            // Change the color of the player's chat messages to pink
            color = Color.pink;
        }
    }
}
```

In this example, the plugin listens for when a player chats and then changes the color of their chat message to pink using the `Color` class.