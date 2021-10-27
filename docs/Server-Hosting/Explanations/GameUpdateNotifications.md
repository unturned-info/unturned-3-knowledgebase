# Server Update Notifications

## Steam News Hub

### User facing

The latest major patch notes can be found on the Steam News Hub.  Minor patch notes are generally published in the steam forums, if at all.

### REST API (JSON)

Programmatic access can be gained using [the GetNewsForApp endpoint](https://steamapi.xpaw.me/#ISteamNews/GetNewsForApp) on the Steam web API. You do not need an API key for this endpoint.

### RSS (XML)

All Unturned Steam news is pushed to its RSS feed. You can find it [here](https://store.steampowered.com/feeds/news/app/304930/). It's formatted as a standard RSS feed with past posts included.

### Latest update RSS

The latest game version is posted [here](https://smartlydressedgames.com/rss/unturned-steam-dedicated-server-updates.xml) along with the Steam Build id, and published date. The SDG RSS feed only contains the most recent update.

## Discord

### Unturned Official announcements

Game updates are pushed to the Unturned Official Discord #steam-dedicated-server-updates announcement channel. You can subscribe a channel in your discord server to it to see updates in your server.

### Unturned.info Discord announcements

!!! caution
    This system is still a work in progress and subject to change at the time of publishing.

Unturned.info maintains a channel in our discord server that parses Steam News Hub patch notes to discord readable markdown formatting instead of an external, allowing them to be read at a glance. You can subscribe to it in the same manner as other discord announcement channels.
