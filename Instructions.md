# Instructions

**Disclaimer :** This tool is only used to import trainers to an hg-engine project. Not every move, item or ability that is valid in this tool has been implemented in hg-engine. You might have to check the [advancement of hg-engine](https://github.com/BluRosie/hg-engine/projects) before using a gen 5+ feature.

## Config File

The [configuration file](config.py) contains many useful default settings. It is recommended that you have a look at it before starting editing the Sheets.

## Structure of the Spreadsheet

Once you created a copy of the spreadsheet you can start editing it.
It is composed of 4 different sheets :
- Pokémon
- Trainers
- Example
- Blank Sheet

### Pokémon Sheet

It contains the sprites of every Pokémon (including forms and shinies).
When typing a species in a Trainers Sheet, the formula will look for the same species name, but capitalized. If the species name ends with an asterisk *\**, it will instead look for its shiny sprite.

If the way a Pokémon or a Pokémon is called doesn't suit you, feel free to edit the A column of the sheet. You will also have to edit *ResolvePokemon* function in [resolve.py](resolve.py).

### Trainers Sheet

It contains the sprites of every trainer class. To determine the trainer class, the formula uses a three-step process:

- The bracketed tags are removed (you can write every useful information you want there). It is therefore very important that you **do not use brackets** in the Trainer Class Name.

```Ace Trainer Mark [Boss] [Double] [Gives you an Oran Berry]``` becomes ```Ace Trainer Mark```.

- The formula then determines the trainer name and trainer class. If the remaining string doesn't contain the word ``` & ```, it assumes the trainer is a single battle class and select the last word as the Trainer Name. If it contains the word  ``` & ```, the last three words are determined to be the Trainer Name.

```Ace Trainer Mark``` is split into ```Ace Trainer``` and ```Mark``` but ```Twins Teri & Tia``` is split into ```Twins``` and ```Teri & Tia```.

- The formula finally looks for the sprite. If it finds a trainer class corresponding to the Trainer Name, it will choose it. If it doesn't find one, it will look for a sprite corresponding to the Trainer Class.

```Ace Trainer♀ Whitney``` and ```Miltank Fan Whitney``` will return the Whitney Sprite.
```Ace Trainer♀ Carole``` will return the Female Ace Trainer Sprite.

You can freely add new classes and sprites on the Sheet. You might also have to edit the *ResolveTrainerClass* function in [resolve.py](resolve.py).

### Example Sheet

This sheet contains some examples of working trainers you can already export to your game. It showcases everything you can do using the tool. It can be useful to have a look at it if you do not know how to write some Pokémon parameter.

### Blank Sheet

This Sheet can be the starting point of your project. This sheet is already correctly formatted and every formula is already present. You should always keep a backup of in case you remove the formulas or mess up the formatting or editing.

## Editing Trainers

The full [hg-engine Trainer Structure](https://github.com/BluRosie/hg-engine/wiki/Trainer-Pok%C3%A9mon-Structure-Documentation) is explained thorougly in the official wiki. There might be some answers there that you might not find here, since the instructions are mostly focused on the RnB-Style Spreadsheets.

To know what each row does, the parser looks at the first cell of each row.
If the first cell starts with ```Name - ``` it will create a new trainer. It will create a new trainer each time the cell starts with ```Name - ```. The parser will ignore every row with an empty first column (with the exception of Pokémon and Moves as explained below).

Here is a list of every supported first cell :
- ```Name - <TrainerID>```
- ```DV```
- ```Ability Slot```
- ```Level```
- ```Pokémon```
- ```Held Item```
- ```Moves```
- ```Ability```
- ```Ball Type```
- ```IVs```
- ```EVs```
- ```Nature```
- ```Status```
- ```Stats```
- ```Nickname```
- ```Ball Seal```

### Trainer Customization

#### Trainer ID

This parameter is mandatory and starts the trainer creation procedure. The first cell of the first row of a trainer should always contain ```Name - ID```. The Trainer ID can be found in *armips/data/trainers/trainers.s*. If the ID is 0 the tool will not print the trainer. If the ID is not 0, the tool will replace the existing trainer with that ID with the one written in the Sheet.

If many imported trainers have the same ID, only the last imported trainer with that ID will be in the game.

#### Trainer Name & Trainer Class

The Trainer Name and Trainer Class are determined in the same row as the Trainer ID. The tool uses [the same procedure as the Spreadsheets](#trainers-sheet).

#### Trainer Mon Type

This field in invisible in the Spreadsheets and you will not have to worry about it because it is automatically determined by the tool based on the rows you added. For example adding a shiny Pokémon will automatically add ```TRAINER_DATA_TYPE_SHINY_LOCK``` to the Trainer Mon Type.

#### Number of Mons

This field is invisible in the Spreadsheets and determined by the number of non-empty cells in the 2nd *Pokémon* Row.

#### Trainer Items

The Trainer Items are currently only editable in the [configuration file](config.py). More support for Trainer Items Customization is planned.

#### AI Flags

The Trainer AI Flags are currently only editable in the [configuration file](config.py). The default options correpond to the best AI settings in the Vanilla Game. More support for Trainer AI Customization is planned.

#### Battle Type

The Battle Type (Single Battle/Double Battle) is determined by the trainer tags in the *Name* row. By default the Battle Type is Single but it will switch to Double if the *[Double]* tag is present in the Trainer Name.

### Pokémon Customization

The tool parses every column where the *Pokémon* row is not empty. You should **always fill out every cell of an existing Pokémon**. Simply type '-' in the cell to make the tool work accordingly and replace that value with the empty value present in hg-engine ('MOVE_NONE', Ball Seal 0, etc.).

#### Species

The Species of the Pokémon is determined in the second Pokémon row. The first Pokémon row will simply load the sprite according to the value below.

##### Alternate Forms

Alternate forms are usually determined using the ```-``` character. A full list forms can be accessed in the *Pokémon* Sheet and in the *ResolvePokemon* function in [resolve.py](resolve.py).

##### Megas

If a Mega Pokémon is holding its Mega Stone, the tool will instead write the normal form of the Pokémon. The Pokémon will Mega Evolve before its first move.
If the Pokémon is not holding its Mega Stone the Pokémon will instead permanently be in Mega Form.
A list of every Mega Stone can be found in the *ResolveItemForm* function of [resolve.py](resolve.py).

#### Level

The Level of the Pokémon is determined by a row starting by a *Level* cell.

#### IVs and EVs

There are two methods for determining IVs and EVs : DV or custom spreads.

If [USE_IV_EV](config.py) is set to True, the *DEFAULT_IVS* and *DEFAULT_EVS* will be attributed if there are no *IVs* or *EVs* rows.

- If there is no *DV*, *IVs* or *EVs* row, the tool will attribute the [default DV value](config.py) to the Pokémon. IVs will be DV/255*31 and EVs will be 0 in every statistic.
- If there is a *DV* row, the game will use that DV value.
- If there is an *IVs* row, the game will set the IVs of the Pokémon to the value of the corresponding cell.
- If there is an *EVs* row, the game will set the EVs of the Pokémon to the value of the corresponding cell.

IVs/EVs formatting : ```hp, atk, def, spe, spa, spd```

#### Abilities

There are two methods of determing a Pokémon's ability :

- Using *AbilitySlot* in the first row will use the Pokémon's two abilities just like in the vanilla game
- Using *Ability* in the first row will use any specified Ability

Note: For Mega Pokémon holding their keystone, the specified ability should be the one **before** Mega Evolving.

#### Nature

If there is no *Nature* row, the Pokémon's nature will be determined using a complex formula including the Species of the Pokémon, the Trainer ID, the Trainer Class and many more parameters.

If there is a *Nature* row, the Pokémon will have the specified nature.

#### Items

If an *Item* row is present, the Pokémon will hold the specified item.

#### Moves

If no *Moves* row is present, the game will use the Pokémon's Learnset up to its level.

If a *Moves* row is present, the Pokémon's four moves will be the Moves specified in the next four rows. If you want a Pokémon to only have three moves, write '-' in the rest of the cells.

If you want a Move to have a specific PP Count, add ``` - <PPCount> ``` at the end of the move. If you specify a PP Count for a move, you will have to specify it for all the Pokémon's moves, otherwise the PP Count will be set to 0.

#### Ball Customization

##### Ball Type

By default, the Pokémon will be sent out using the [DEFAULT_BALL](config.py).

If a *Ball Type* row is present, the Pokémon will be sent out using that Ball.

##### Ball Seal

If a *Ball Seal* row is present, the Pokémon will be sent out using that Ball Seal.

Here is a list of every Vanilla Ball Seal (research by Drayano):
```
0 - No ball seal
1 - Red petals
2 - Music notes
3 - Confetti
4 - Lightning bolts
5 - Black smoke clouds
6 - Big red hearts and stars
7 - Red hearts
8 - Blue bubbles
9 - Pink bubbles
10 - Yellow stars
11 - Cyan and yellow stars
12 - Black and white smoke clouds
13 - Orange flame clouds
14 - Blue flame clouds
15 - Pink and blue bubbles
16 - Black and white smoke clouds, blue bubbles, orange flame clouds and confetti
17 - Orange flame clouds, blue flame clouds, blue stars and yellow stars
18 - Music notes and lightning bolts
19 - Lots of red petals
20 - Only a few red petals and a little confetti
21 - Red petal spirals
22 - Three bits of confetti symbolising a roar
23 - Blue stars
24 - Blue and yellow stars
25 - Black smoke clouds from the ground
26 - Dark purple petal spirals
27 - Lots of red petals (again?)
```

#### Shinies

If the Pokémon's name in the second *Pokémon* row ends with the character ```*```, the Pokémon will be shiny and its Sprite will automatically update.

#### Pré-Status

If a *Status* row is specified, the Pokémon will have that status initially.

Here is a list of supported Status Conditions :
- Poisoned
- Badly Poisoned
- Burned
- Paralyzed
- Frozen
- Asleep
- Asleep (1 Turn)
- Asleep (2 Turns)
- Asleep (3 Turns)
- Asleep (4 Turns)
- Asleep (5 Turns)
- Asleep (6 Turns)
- Asleep (7 Turns)

#### Custom Statistics

If a *Stats* row is present, the Pokémon will have the specified statistics.

Statistics formatting : ```hp, atk, def, spe, spa, spd```

#### Nickname

If a *Nickname* row is present, the Pokémon will have the specified nickname. The nickname can be up to 10 characters long. It can only contain the characters present in Pokémon Heartgold.

### Additional Customization

#### Area Name

You can freely add Area Names to the Sheets. As long as the cell of the first column is empty, the cell will be disregarded by the parser.

#### Splits

If you want to split the documentation into different parts, just duplicate an already formatted Sheet. The tool will convert every csv file in the [csv folder](csv/), it is therefore perfectly compatible with a split documentation.

### Formatting

The Sheets are already formatted "correctly" and the Blank Sheet should be more than enough to write everything you want.

You should never delete the formulas in the Pokémon and Trainer Cells. In case you accidentally deleted them, you can simply click on another cell of that type and Copy-Paste the value.

If you want to add rows for parameters of a trainer, select the row above or below, right-click and insert a new row. You can then copy/paste the formatting of a cell of the correct color. (The colors alternate every row).

Here are some useful shortcuts you might have to use :
- CTRL+Shift+V to paste the values only (not the formatting)
- CTRL+Alt+V to paste the formatting only (not the values)

## Inserting Trainers into the Game

Download the Sheet you want in .csv format in place it in the .csv folder of rnbstyle-hge-editor. The file you get should be quite similar to the [Example File](csv/Example.csv). The tool will read **every CSV file in that folder**.

Run main.py in the *rnbstyle-hge-editor* folder. The tool will do a validity check for these parameters and tell you if anything is wrong :
- Trainer Mon Type
- Trainer Class
- Trainer Items
- Pokémon Species
- Pokémon Held Item
- Pokémon Moves
- Pokémon Ability
- Pokémon Ball
- Pokémon Nature
- Pokémon Additional Tags

If everything went fine, you should see the message ```Inserted trainer : <trainerName> with ID <trainerID>```.

Build the ROM using hg-engine, you should see the updated trainers in the game. You might have to ```make clean``` before building the ROM in some cases.