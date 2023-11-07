# wow-rumble-clicker
Simple clicker for quests and PvP

Works with LDPlayer setup in this resolution
![image](https://github.com/bigos81/wow-rumble-clicker/assets/1384214/640c0a0c-71ef-43a3-8dd7-5cbc63550c63)

For other resolution you'd have to re-do all the images i'm searching for in resources/ folder

Files:

rc-loop.bat - runs quests untill questes are out, then runs pvp. In case of errors loops back again and logs some simple timestaps and events to log.txt
rc-pvp.py - runs loop for pvp (chooses weakest - leftmost hearo) not to spoil your pvp score, expect winning like 1/6th of the time
rc-quest.py - runs loop for quests (be susre to set your strongest hero in the army) - expect 60% win rate
