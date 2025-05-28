# RPRH-Converter
A tool to manipulate New Super Mario Bros. U (Wii U) level replay files.

This is a little script I made to automate the process of converting NSMBU challenge replays as a way of creating custom title replays of sorts.
(Said title replays can found under `content/Common/replay/title`).

In order to do so, you need to create a custom challenge that contains the level you want to make a custom replay for. Unfortunately, the selection of levels that the game randomly picks one to play a replay for is hardcoded, so you can only replace these levels:

```title000: 1-1
title001: 1-4
title002: 4-2
title003: 5-20
title004: 1-5
title005: 6-1
title006: 8-1
title007: 5-1
title008: 2-1
```
Creating custom challenges can be done using [NSMBU-Challenge-Data-Editor by TheGrop](https://github.com/TheGrop/NSMBU-Challenge-Data-Editor). I'd recommend making a custom Time Attack challenge for the level you'd like to make a replay for, then beat the challenge ingame so you can save your replay.
