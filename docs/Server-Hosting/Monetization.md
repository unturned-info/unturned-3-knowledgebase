# Server Monetization Policy

???+ Important
    Unturned servers must follow the [Server Hosting Rules](https://github.com/SmartlyDressedGames/U3-Docs/blob/master/ServerHostingRules.md)

    <iframe src="https://smartlydressedgames.github.io/U3-Docs/ServerHostingRules" title="U3 Server Hosting Rules webpage" height=500 width=900></iframe>

## Server Monetization Filter

To accompany the Server Monetization Policy, servers can now specify their level of Monetization in the `config.json` file. By default, your server will be set to `Unspecified`. Users will be able to filter out servers based on their monetization policy, so it is likely in your best interest to set it accurately.

!!! warning
    If you choose to set this field, ensure it is accurate.

### unspecified

The default value, leave this be if you're unsure which section your server falls under or don't care.

### None

If your server contains no form of monetization or only accepts donations, you should set Monetization to `None`.

### Non-Gameplay

If your server contains allowed forms of monetization, you should set Monetization to `NonGameplay`. Ensure your server meets the allowed forms of monetization by thoroughly reading [the server hosting rules.](https://github.com/SmartlyDressedGames/U3-Docs/blob/master/ServerHostingRules.md)
