# WorkshopDownloadConfig.json

Steam Workshop add-ons (e.g., maps, items, vehicles) are set up in the `WorkshopDownloadConfig.json` file.
To include a Workshop file on your server:

1. Browse to its web page, for example: [Hawaii](https://steamcommunity.com/sharedfiles/filedetails/?id=1753134636)
2. Copy the file ID from the end of the URL.

        URL: https://steamcommunity.com/sharedfiles/filedetails/?id=1753134636
        ID: 1753134636

3. Insert the file ID into the File_IDs list:

        "File_IDs":
        [
            1753134636
        ],

    Multiple file IDs should be separated by commas:

        "File_IDs":
        [
            1753134636,
            1702240229
        ],

4. During startup the files will be updated, and any dependencies detected. Players will have the files downloaded while connecting to the server.
