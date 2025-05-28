# RPRH-Converter
A tool for handling and manipulating New Super Mario Bros. U (Wii U) level replay files.
This tool will not work for New Super Mario Bros. U Deluxe replay files. Perhaps support could be added in a later release if there's enough interest.

This is a little script I made to automate the process of converting NSMBU challenge replays as a way of creating custom title replays of sorts.
(Said title replays can found under `content/Common/replay/title`).

In order to do so, you need to create a custom challenge that contains the level you want to make a custom replay for. Unfortunately, the selection of levels that the game randomly picks one to play a replay for is hardcoded, so you can only replace these levels:

```
title000.dat: 1-1
title001.dat: 1-4
title002.dat: 4-2
title003.dat: 5-20
title004.dat: 1-5
title005.dat: 6-1
title006.dat: 8-1
title007.dat: 5-1
title008.dat: 2-1
```
Creating custom challenges can be done using [NSMBU-Challenge-Data-Editor by TheGrop](https://github.com/TheGrop/NSMBU-Challenge-Data-Editor). I'd recommend making a custom Time Attack challenge for the level you'd like to make a replay for, then beat the challenge ingame so you can save your replay. Saved challenge replays can be found by extracting your "common" NSMBU savedata, then from there you can find your challenge replays named `rp_challenge_replayXX.dat`, with XX being the current replay file count.

## Usage
  [Python 3](https://www.python.org/downloads/) is required in order to run this script.
  
- `RPRH-Converter.py inputreplay outputreplay [-L]`
  - inputreplay: The challenge replay file to be converted.
  - outputreplay: The title replay file to be output.
  - -L: (Optional): Outputs the level that this challenge replay is for. The argument `outputreplay` is not required if `-L` is to be used.

After the replay file has been converted, rename the converted replay to your designated title replay slot listed above, replace the designated title replay, then you should have a custom title screen replay in game!

## Credits
- techmuse (myself) - Main developer
- Kinnay - Creating the documentation for NSMBU's replay format that was used as a reference for developing this tool. A link to the documentation can be found [here.](https://nintendo-formats.com/games/nsmbu/replay.html)


