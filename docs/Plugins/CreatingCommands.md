# Creating Commands

!!! note The following documentation is for RocketMod (LDM).

In order to make a command, you'll need to make your command class implement the `IRocketCommand` interface. Comments within the example explain each member implementation.

```csharp
using Rocket.API;
using Rocket.Unturned.Chat;
using Rocket.Unturned.Player;
using System.Collections.Generic;

namespace MyAwesomePlugin
{
    public class CommandHello : IRocketCommand
    {
        //Decides if someone can execute the command in the server console and/or in-game. In this case, in-game.
        public AllowedCaller AllowedCaller => AllowedCaller.Player;

        //Name of the command that the caller will have to specify in order to execute.
        public string Name => "hello";

        //String that describes the command.
        public string Help => "Says hello to the player.";

        //String that describes proper usage of the command.
        public string Syntax => "/hello";

        //Different names that could be used to execute the command.
        public List<string> Aliases => new List<string>() { "hi" };

        public List<string> Permissions => new List<string>() { "myawesomeplugin.hello" };

        //Method that is executed when the caller uses /hello or /hi while having the
        //myawesomeplugin.hello permission.
        public void Execute(IRocketPlayer caller, string[] command)
        {
            
        }
    }
}
```

Once you implement everything, you can start work on a proper command execution.

For this example, the command will say hello to the player by grabbing their display name using the `UnturnedPlayer` class and sending a message using the `UnturnedChat.Say` method:

```csharp
using Rocket.API;
using Rocket.Unturned.Chat;
using Rocket.Unturned.Player;
using System.Collections.Generic;

namespace MyAwesomePlugin
{
    public class CommandHello : IRocketCommand
    {
        public AllowedCaller AllowedCaller => AllowedCaller.Player;

        public string Name => "hello";

        public string Help => "Says hello to the player";

        public string Syntax => "/hello";

        public List<string> Aliases => new List<string>() { "hi" };

        public List<string> Permissions => new List<string>() { "myawesomeplugin.hello" };

        public void Execute(IRocketPlayer caller, string[] command)
        {
            //Uses an explicit conversion to change the IRocketPlayer to an UnturnedPlayer.
            UnturnedPlayer player = (UnturnedPlayer)caller;

            //Uses $ for string interpolation. Much better than using traditional +.
            UnturnedChat.Say(caller, $"Hello {player.DisplayName}!");
        }
    }
}
```

This command will now properly work in-game, but what if we change the color of the message?

Here is an modified version of the example using the `Color` class within `UnityEngine`. Be sure to add the proper usings the top (specifically `UnityEngine`).

```csharp
using Rocket.API;
using Rocket.Unturned.Chat;
using Rocket.Unturned.Player;
using System.Collections.Generic;
using UnityEngine;

namespace MyAwesomePlugin
{
    public class CommandHello : IRocketCommand
    {
        public AllowedCaller AllowedCaller => AllowedCaller.Player;

        public string Name => "hello";

        public string Help => "Says hello to the player";

        public string Syntax => "/hello";

        public List<string> Aliases => new List<string>() { "hi" };

        public List<string> Permissions => new List<string>() { "myawesomeplugin.hello" };

        public void Execute(IRocketPlayer caller, string[] command)
        {
            UnturnedPlayer player = (UnturnedPlayer)caller;

            //Uses Color.red to change the message color to red.
            UnturnedChat.Say(caller, $"Hello {player.DisplayName}!", Color.red);
        }
    }
}
```

That is all, a proper command that messages the player a hello message that is red. Check out [Creating Plugins](CreatingPlugins.md "Creating Plugins") for an example of how to send a welcome message to a player when they connect.