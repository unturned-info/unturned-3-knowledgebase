# Spawntables 101

***Tutorial on how to make your item/vehicle/whatever spawn naturally***

*Created by* **Genestic12**

*Special thanks to* **khakers** and **Renaxon**

- [Spawntables 101](#spawntables-101)
  - [Intro](#intro)
  - [The basics](#the-basics)
  - [What does 'weight' mean?](#what-does-weight-mean)
  - [What are Roots?](#what-are-roots)
  - [Advanced applications](#advanced-applications)

## Intro

So, you want to ~~run around attempting to find your vehicle for 2
hours~~ make your new modded thing spawn naturally instead of you having
to use cheats to spawn it in, huh?

No problem! With the help of this tutorial, you'll soon be running
around maps trying to search for your modded thing because you have to
manually check if your spawn tables worked.

Understood? Great! Let's begin.

## The basics

!!! note
    This tutorial requires that you read at least the basics of UM101, otherwise you will have no idea what I am talking about when I say things like 'go back to the **Bundles** folder' or 'you will need to copy+paste then edit this DAT file'. If you didn't, that's your problem.

Here we go!

In the **Bundles** folder(`Steam/steamapps/common/Unturned/Bundles`) there
is a folder named **Spawns**. Navigate into this folder.

You should see this

![ Folders: Animals Beacon Carepackage Fish Items Vehicles](.\/media/image14.png)

If your modded thing is an item(this includes clothing, guns, melee weapons, foodstuffs, etc etc... generally, anything you can drop on the ground and then pick up(and see it in your inventory) is an item), go for **Items.** If it's a vehicle, go for **Vehicles.** Since I'm using my recent Huey mod for this tutorial, I'm going for **Vehicles.**

![](.\/media/image9.png)

And now we have all these folders in here. What do all of them mean?

For a straight-up answer, my response is : **I don't know either.** I
still do not fully know how exactly the spawntable system works in
Unturned. What I am about to show you is my own understanding of the
system, using pictures of various DAT files and how they are linked to
each other. If you believe this guide is not a reliable one because of
this, you are welcome to find a different one or make your own.

Moving on!

For an example, let's take a look at the folder for the vanilla Huey.

But wait! There's multiple folders for that.

![](.\/media/image6.png){width="2.625in" height="1.71875in"}

What do those even mean?

~~**Huey_America** is the 'topmost' spawn for this spawn~~\*, if you can
comprehend that sentence. What that means is that this spawn contains
the **Huey_America_Hummingbird** and the **Huey_America_Tier** spawn.

\*no it isn't, I found another folder named **Washington_Huey_America**
that contains this spawn, doesn't really matter

Still don't understand?

That's alright; I didn't either and I don't expect you to get it right
off the bat. Let's take a closer look.

+--------------------------+-----------------------+
| Name                     | DAT                   |
+==========================+=======================+
| Huey_America             | ID 426                |
|                          |                       |
|                          | Tables 2              |
|                          |                       |
|                          | Table_0\_Spawn_ID 427 |
|                          |                       |
|                          | Table_0\_Weight 83    |
|                          |                       |
|                          | Table_1\_Spawn_ID 428 |
|                          |                       |
|                          | Table_1\_Weight 10    |
+--------------------------+-----------------------+
| Huey_America_Hummingbird | ID 428                |
|                          |                       |
| (HAH for short)          | Tables 1              |
|                          |                       |
|                          | Table_0\_Asset_ID 107 |
|                          |                       |
|                          | Table_0\_Weight 10    |
+--------------------------+-----------------------+
| Huey_America_Tier        | ID 427                |
|                          |                       |
| (HAT for short)          | Tables 1              |
|                          |                       |
|                          | Table_0\_Asset_ID 94  |
|                          |                       |
|                          | Table_0\_Weight 10    |
+--------------------------+-----------------------+

To make things easier for you, 107 is the ID for the Hummingbird. 94 is
the ID for the Desert Military Huey.

So to sum it up, the DAT for HAH means this:

ID 428 - The ID of this spawn is 428.

Tables 1 - This spawn has one spawn table.

Table_0\_**Asset**\_ID 107 - This spawn table will output an **Asset**,
and that asset's ID is 107.

Table_0\_Weight 10 - This spawn table has a weight of 10 within this
spawn.

## What does 'weight' mean?

Good question. It's actually important that I get this across before I
do anything further, so allow me to branch off a bit.

A spawn table's **Weight** defines how much of the total spawn that this
spawn table will take up. The percentage is calculated by dividing the
spawn table's weight with the total of all weights in the spawn.

As an example, here's a fake spawn I wrote up.

```
ID 420

Tables 5

Table_0\_Asset_ID 69

Table_0\_Weight 69

Table_1\_Asset_ID 1337

Table_1\_Weight 17

Table_2\_Asset_ID 124

Table_2\_Weight 14

Table_3\_Asset_ID 570

Table_3\_Weight 60

Table_4\_Asset_ID 135

Table_4\_Weight 47
```

The total of all weights within this spawn is **207**. The weight for
the asset ID 69 is **69.** This means that the asset ID 69 takes
one-third of the total spawn. Asset ID 570 has a weight of **60** and
takes about 30%, asset ID 135 has a weight of **47** and takes about 23%
and so on.

Since we've covered weights, we can move on to **Huey_America.**

Tables 2 - This spawn has two tables.

Table_0\_**Spawn**\_ID 427 - This table outputs another **Spawn**, and
that spawn's ID is 427.

Table_0\_Weight 83 - This table has a weight of 83.

Table_1\_**Spawn**\_ID 428 - This table outputs another **Spawn**, and
that spawn's ID is 428.

Table_1\_Weight 10 - This table has a weight of 10.

If you have a keen eye, you may have noticed that **427** and **428**
are the ID numbers of **HAH** and **HAT.** These spawns are,
respectively, the spawns for the Desert Military Huey and the
Hummingbird. So overall, **Huey_America** is a spawn table that gives a
weight of **83** to the Desert Military Huey and a weight of **10** to
the Hummingbird. In other words, the Desert Huey is about eight times
more likely to spawn than the Hummingbird.

"But Gen," you might say, "Why go through all that hassle? Why not just
make a single DAT with two tables containing the Huey and Hummingbird?"

That is a very good question. I don't know either. Go ask **NolsoN**.

Now that we've covered the basics of spawntables, we can move on to
actually making your modded thing spawn naturally.

Since my Huey is the Forest Military version, I'll copy the
**Huey_Canada** folder to edit. (In case you haven't already noticed,
America means Washington and Canada means PEI.)

![](.\/media/image8.png)

Delete the GUID line, change the ID to something else that's lower than
65535, then delete everything under the ID line.

![](.\/media/image7.png)

You might be wondering why I deleted pretty much the entire DAT; well,
this process is, in a nutshell, rewriting the entire DAT. So there you
go.

I have two helicopters in the forest military green color. So that means
I need two **Tables**, and **Weights** for each of those.

![](.\/media/image13.png)
To elaborate, **20000** is a normal Huey and **20001** is a Huey with
two M60 door gunners. To balance the armed version, I gave it a weight
of **2** while the unarmed version has a weight of **8.** This means the
normal version is four times more likely to spawn.

Now we're going to add something called **Roots.**

## What are Roots?

**Roots** are basically a way of telling the game that you are going to
connect your new spawn table to a vanilla spawn table. In this case, I
want to connect the spawn table I made for my Huey to the vanilla Huey's
spawn table, which if you can still remember, had the ID **426**. So to
do this, I add this line to the DAT.

![](.\/media/image4.png)

You probably understand what **Root_0\_Spawn_ID 426** means. But what
does **Root_0\_Weight 10000** mean?

(addition. I forgot that 426 is for the Washington spawn and not PEI.)

This line is what determines how much weight this spawn will have within
the spawn that it is being connected to. Since we just gave it a weight
of 10000, this spawn will have a weight of 10000 in the **Huey_America**
spawn.

Remember how in this spawn, the spawn for the Huey had 83 weight and the
Hummingbird had 10?

![](.\/media/image1.png)

Well, our new Huey spawn has a weight of **10000** and will now simply
crush the two original tables out of existence. To put it simply, if a
heli does spawn in a helipad in Summerside Military Base, it will most
likely be the new Huey and not the vanilla one(or a Hummingbird, for
that matter)

This is only for cases where you want to completely replace the vanilla
spawns with your own or you want to test your new spawn table. If you
want a nice mix, adjust your spawn's weight accordingly. (In this case,
I'd give it **Root_0\_Weight 50**)

At this point, save and then launch the game to see if it generates a
GUID for your new spawn table. If it does, it means the game at least
recognizes it as a new file. If it doesn't, it usually means ID
conflicts. You can check **Workshop-\>Error Logs** in the main menu of
the game to see what caused this.

![](.\/media/image2.png)

So the game has indeed generated a new GUID for us. Let's check if the
spawns actually work. Since this helicopter is meant to spawn only on
PEI, I'll be using that map. (again, I forgot that 426 is for the
Washington spawn and not PEI. Because of this the picture is taken in
Olympia Military Base.)

![](.\/media/image15.png)

Taken after about four tries. In the case of vehicles with rare spawn
locations (like helicopters and planes), if nothing spawns, reset the
world and try again.

Congratulations, you now understand how to make a *single* vehicle spawn
naturally on a *single* map. Let's move on to more general things, like
making cars spawn on all vanilla maps. Recently I accidentally deleted
the spawns for my Lada mod, so let's remake those for this tutorial.

## Advanced applications

Make a new folder in **Spawns** named **\[Lada\]** (do not literally
type this, use your own mod's name), then copy+paste a random spawn's
DAT file into it(rename it to \[Lada.dat\], btw)

As before, leave the second and third lines and delete everything else.

![](.\/media/image10.png)(This used to be the Roadster.dat btw)

Now, to begin constructing our new DAT we need to take some things into
consideration. How many assets do we want this spawn to have? Are there
any assets that should be rarer than others?

I have ten vehicles for this spawn, and two of them need to be a bit
rare. In DAT file form, that looks like
this:![](.\/media/image12.png)

*You should get what this means by now, you know*

Now we need to add **Roots.**

Since this is a civilian car, these are what you want to look at

![](.\/media/image5.png)

Let's open them up and take a look at the contents. Before that, though,
a brief note on the nomenclature of the folders - **Arctic** is for
Yukon. **Peaks** is for Germany. **Russia** is for Russia, obviously. I
have no idea why **NolsoN** decided to name locations like this instead
of the actual names, but he did and I'm explaining them to you right
now.

**Civilian.dat**

```
Type Spawn

ID 296

Tables 8

Table_0\_Spawn_ID 40

Table_0\_Weight 34

Table_1\_Spawn_ID 297

Table_1\_Weight 32

Table_2\_Spawn_ID 298

Table_2\_Weight 31

Table_3\_Spawn_ID 299

Table_3\_Weight 28

Table_4\_Spawn_ID 300

Table_4\_Weight 30

Table_5\_Spawn_ID 301

Table_5\_Weight 10

Table_6\_Asset_ID 185

Table_6\_Weight 50

Table_7\_Asset_ID 950

Table_7\_Weight 10
```

Using what we've learned so far, we can easily identify that this spawn
outputs six **Spawns** (40, 297,298,299,300,301) and two **Assets** (185,
950).

185 is the Bicycle and I don't know what 950 is. But what are those six
spawns?

If you scroll a bit down from the **Civilian** folder, you'll notice
folders named **Hatchback, Offroader, Roadster, Truck, Sedan,** and
**Van,** in that order. If you open these up and check their contents,
you'll see that they are spawn tables for their corresponding vehicles.

| Name      | ID  |
|-----------|-----|
| Offroader | 40  |
| Hatchback | 297 |
| Truck     | 298 |
| Sedan     |299  |
| Van       |200  |
| Roadster  |301  |

Overall, we can see that the **Civilian** spawn is a spawn table that
outputs the spawns for six types of civilian vehicles, a bicycle, and
whatever ID 950 is. You can go check that this is the same for the
**Civilian\_\[map\]** spawns.

Now, if you have a sharp mind you might have already realized that we
need **Roots** that link to those four spawns. This is correct, and the
IDs for those spawns are as follow :

  Name              ID
  ----------------- -----
  Civilian          296
  Civilian_Arctic   497
  Civilian_Peaks    735
  Civilian_Russia   597

That translates into these new lines:

![](.\/media/image3.png)

As a placeholder, I set all weights to 50.

Now, for the **Civilian** spawn, the total weight is **225.** Because of
this, I'll set **Root_0\_Weight** as 75, making the grand total 300 and
giving 25% to the Lada's spawn in this spawn(25% of 300 is 75). **Normal
cars are the most common type of vehicle and thus do not require that
you crush the vanilla spawns out of existence for you to test if your
spawn works.**

Adjust all the remaining weights correspondingly and we have this

![](.\/media/image16.png)

*If you take the total weight of the spawns(shown in above pics) and the
map of those spawns, you'll see why I set those weights as such*

Just like the Huey spawn, by this point our DAT is fully structured and
ready for testing. Save, then launch the game to see if it generates a
new GUID, then open up a map to test your spawn.

![](.\/media/image11.png)

Picture taken in Moscow, because it's a Russian car. My laptop sucks at
running Unturned, don't whine about the quality. But hey, at least it
works.

That's all for creating your own spawn tables! Maybe in the future I'll
bother to add a section on Items, but those work pretty much the same
way anyway.

I hope this guide was helpful to you.

Genestic12, out.
