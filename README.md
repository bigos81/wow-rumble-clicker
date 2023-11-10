# wow-rumble-clicker
Simple clicker for Warcraft Rumble mobile game quests and PvP

https://play.google.com/store/apps/details?id=com.blizzard.arc

Files:

rc-loop.bat - runs quests untill questes are out, then runs pvp. In case of errors loops back again and logs some simple timestamps and events to log.txt
rc-pvp.py - runs loop for pvp (chooses weakest - leftmost hearo) not to spoil your pvp score, expect winning like 1/6th of the time
rc-quest.py - runs loop for quests (be susre to set your strongest hero in the army) - expect 60% win rate

Works with LDPlayer (https://www.ldplayer.net/) setup in this resolution and make sure the whole game screen fits on your screen (or at lease the bottom part as it's the places the clicker will operate on)
![image](https://github.com/bigos81/wow-rumble-clicker/assets/1384214/640c0a0c-71ef-43a3-8dd7-5cbc63550c63)

For other resolution you'd have to re-do all the images i'm searching for in resources/ folder

Small demo of the working script: https://imgur.com/JtSDwgD.gif

Really, don't expect much, it's coded in couple of hours scripts to just click on the game as I thought the quests are
unlimited and it's free experience which turns out not to be the case. You can play 20 a day and you should actually
want to win those :)
