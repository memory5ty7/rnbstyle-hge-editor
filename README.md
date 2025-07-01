# Pokémon Run and Bun-Style Documentation with hg-engine Compatibility
## About
An easy-to-master and fast tool to edit hg-engine trainers using spreadsheets.

![Sample Team](png/Sample%20Team.PNG)

## Requirements

- hg-engine
- Python 3.10 or higher

## Installation

1. Install hg-engine by following the [installation instructions](https://github.com/BluRosie/hg-engine?tab=readme-ov-file#setup-instructions-linux-with-apt).

2. In the same directory where you cloned hg-engine, clone rnbstyle-hge-editor.
- ```git clone https://github.com/Memory5ty7/rnbstyle-hge-editor.git```

You should now have ```folder/hg-engine``` and ```folder/rnbstyle-hge-editor```

3. Create a copy of the [Run and Bun-Style Sample Sheet](https://docs.google.com/spreadsheets/d/1QQ9A7cZD-ivIZ9QNOgbUV2toyaC7QJ42lxEYZk_odos/edit?usp=sharing) on your Google Drive account.

4. Customize the trainers the way you want following the [Editing Instructions](Instructions.md)

5. Once the modifications are done, download the Sheet you want as a .csv and place it in the [csv subfolder](csv) of rnbstyle-hge-editor.

6. Run [main.py](main.py) to transfer the changes to the assembly file used by hg-engine

7. Build your ROM using hg-engine, the modified trainers are now in the game.

## Features

This tool supports every trainer customization parameter included in hg-engine :

**Trainer Customization:**
- Trainer ID
- Trainer Name
- Trainer Class
- Number of Party Mons
- Trainer Items
- AI Flags
- Battle Type (Single/Double)

**Pokémon Customization:**
- Species (including Forms and Megas)
- Level
- Ability (Ability Slot or Custom Ability)
- Item
- Moveset (Level-up or Custom Moveset)
- IVs/EVs (using DVs or Custom IV/EV Spreads)
- Statistics
- Ball (Ball Type and Ball Seal)
- Shiny
- Status (Pré-Status)
- PP Counts
- Nickname

More details about the customization in the [Instructions](Instructions.md).

## Configuration

Configure the tool via the [Config file](config.py).

## Future Development

- More Customization of AI Flags
- More Customization of Trainer Items
- Wild Encounters Editor

# Credits

* [Memory5ty7](https://github.com/Memory5ty7/)
* [hg-engine](https://github.com/BluRosie/hg-engine/blob/main/CREDITS.md)
* [dekzeh](https://x.com/dekzeh) : Pokémon Run and Bun
* [Caruban](https://www.pokecommunity.com/members/caruban.726868/) : Compilation of Pokémon Sprites
* **Gen 1-5 Pokemon Sprites** - veekun
* **Gen 6 Pokemon Sprites** - All Contributors To Smogon X/Y Sprite Project
* **Gen 7 Pokemon Sprites** - All Contributors To Smogon Sun/Moon Sprite Project
* **Gen 8 Pokemon Sprites** - All Contributors To Smogon Sword/Shield Sprite Project
* **PLA Pokemon Sprites** - Smogon Sprite Project
Blaquaza, KingOfThe-X-Roads, KattenK, Travis, G.E.Z., SpheX, Hematite, SelenaArmorclaw
* **Gen 9 Pokemon Sprites** - KingOfThe-X-Roads, Mak, Caruban, jinxed, leParagon, Sopita_Yorita, Azria, Mashirosakura,
JordanosArt, Abnayami, OldSoulja, Katten, Divaruta 666, Clara, Skyflyer, AshnixsLaw, ace_stryfe
* **Gen 9 Vanilla style sprites** - KingOfThe-X-Roads, Mak, Caruban, jinxed, leParagon, Sopita_Yorita, Azria, Mashirosakura, JordanosArt, Scept, NanaelJustice, SoyChim, KRLW890, AnonAlpaca, PokeJminer, Red7246, Carmanekko, Eduar, Lykeron, GriloKapu10, Mesayas, Erkey830, QDylm, PorousMist, OldSoulja, AlexandreV2.0, Z-nogyroP, lennybitao, Ruben1986, GRAFAIAIMX
Blaquaza, KattenK, Travis, G.E.Z., SpheX, Hematite