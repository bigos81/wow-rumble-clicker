

# WoW Rumble Clicker
Simple clicker for Warcraft Rumble mobile game quests and PvP  
https://play.google.com/store/apps/details?id=com.blizzard.arc


# Table of Contents  
1. [Files](#Files)
2. [Setup](#Setup)
3. [Debugging](#Debugging)
   1. [Explanation of output](#Explanation-of-output)
4. [Demo](#Demo)
5. [Disclaimer](#Disclaimer)
6. [Still Reading?](#Still-Reading)

## Files

**rc-loop.bat** - runs quests until quests are out, then runs pvp. In case of errors loops back again and logs some simple timestamps and events to log.txt  
**rc-pvp.py** - runs loop for pvp (chooses weakest - leftmost hero) not to spoil your pvp score, expect winning like 1/6th of the time  
**rc-quest.py** - runs loop for quests (be sure to set your strongest hero in the army) - expect 60% win rate  

## Setup
Works with LDPlayer (https://www.ldplayer.net/) setup in this resolution and make sure the whole game screen fits on your screen (or at lease the bottom part as it's the places the clicker will operate on)
![image](https://github.com/bigos81/wow-rumble-clicker/assets/1384214/640c0a0c-71ef-43a3-8dd7-5cbc63550c63)

For other resolution you'd have to re-do all the images I'm searching for in `resources/` folder

## Debugging
Well if it does not work for you and all you see is this on console:

`(F) effi: 0.00% played: 0 elapsed: 0:00:06.879641 cl: 0 lvl: 0 big: 0 e: 0 btn: none`
With elapsed time just going up this means the game graphics are not found, this means that:
- the resolution of the emulated game is different from the template images
- the emulated game is not run on a primary monitor (library I'm using only screenshots the primary monitor I think)

### Explanation of output
**rc-quest.py**: `(F) effi: 0.00% played: 0 elapsed: 0:00:06.879641 cl: 0 lvl: 0 big: 0 e: 0 btn: none`

(F) - is the script in combat: F - False, T- True  
effi - success %, namely how much % of games were won  
played - number of games played  
elapsed - time the script is running for so far  
cl - how many times claim was clicked (meaning we won a match)  
lvl - how many times a unit got a level up  
big - how many times your rumple account leveled up a collection level  
e - how many times error (rumble error) occurred  
btn - last found graphics from resources - 'none' means none was found, which is ok for loading screens and during battle, not so much in game interface  


## Demo
Small demo of the working script:  
<a href="https://imgur.com/JtSDwgD"><img src="https://imgur.com/JtSDwgD.gif" style="height: 300px"/></a>

## Disclaimer
Really, don't expect much, it's coded in a couple of hours scripts to just click on the game as I thought the quests are
unlimited, and it's free experience which turns out not to be the case. You can play 20 a day, and you should actually
want to win those :)

## Still Reading
Wow, I salute you :) If you want to give me a shout-out or just say thank you, feel free to buy me a coffe :)  
[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/black_img.png)](https://www.buymeacoffee.com/bigos81)
