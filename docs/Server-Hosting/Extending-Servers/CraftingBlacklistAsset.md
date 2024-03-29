# Crafting Blacklist Asset

!!! note "This is an [Asset v2](../../Modding/AssetTypes/AssetsV2.md) class."

Prevents specific items or blueprints from being used while crafting. They are hidden from the item quick actions menu and recipe list.

`Input_Items` array of Item [Asset Pointers](../../Modding/AssetPtr.md): Any blueprints consuming these items are cannot be crafted.

```json
"Input_Items"
[
    "### this is a GUID number ###"
    "### guid ###"
    {
        "NoteToSelf" "eaglefire"
        "GUID" "b03d581a5c1a490f995f8deba57b0f17"
    }
    "### another GUID number ###"
]
```

`Output_Items` array of Item [Asset Pointers](../../Modding/AssetPtr.md): Any blueprints generating these items cannot be crafted.

`Blueprints` array: Prevent specific individual blueprints from being crafted. Each entry has an `Item` [Asset Pointer](../../Modding/AssetPtr.md) and `Blueprint` index. For example to prevent the Chef Hat from being salvaged:

```json
"Blueprints"
[
    {
        "Item" "a6099002318e4d58b8e59d431bcf1b8a"
        "Blueprint" "0"
    }
]
```
