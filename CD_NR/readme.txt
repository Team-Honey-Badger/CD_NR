Controls:
	Player:
		Walk using "A" and "D"
		Jump using "Space"
		Shoot and aim using mouse and left click
		Drop current weapon by tapping "Q"
	Dev:
		Run at 1 FPS while holding "G"
		View all non-AI related hitboxes by holding "H"
		Press "J" to skip level

======================CREATE YOUR OWN MAPS======================

How to Make Your Own Maps!

1.) Download Tiled. It can be found at http://www.mapeditor.org/


2.) Open tiled, when you create a new map make sure to choose "Orthogonal" view, 70 units heigh and 200 units wide. The blocks will be 32x32 pixels.


3.) Add a tileset. The tileset can be found in the custom maps labeled 'tileset.png'. 
WARNING: Make sure to only add one tileset, and only have one layer after your map is done before exporting.
Note: DO NOT click the check box about transparency!!!


4.) Create your map! Tiled has some awesome tools available ranging from rectangular select, stamp, and a paint bucket.

Note: Enemy and character spawns should have an empty block between them and any other block (underneath). Portals require a 2x2 area free around them (portal tile indicates top left of the 2x2 area). Weapons with blue backgrounds are weapon spawners and require an empty block under them, and weapons with red backgrounds are AI spawners. The green block with a smiley face is the player spawner. You MUST have a player spawner in the map for it to work.


5.) After you are finished you can save your map. By default Tiled saves using a .tmx extension. After you save, export your file using a .lua extension. THIS is the file that you will be converting to our format.


6.) There is a python script in the "Custom Maps" folder. You may either copy this into the folder you saved your .lua map, or you can copy your file into the custom maps folder. Afterward, run "convert.py". It will prompt you for a file, simply enter the file name you exported to. Then enter the file name you wish to use for the output. The game will only load files included in the regex "level*.txt", so make sure the naming is appropriate. Levels are loaded in a sorted order numerically.


7.) Now when you start the game, make sure to select custom maps, and you will begin with the first custom level in the folder!


Note: If you run into issues after converting your file, make sure you did not export a map with multiple layers or tilesets. Also make sure your level is named appropriately, begins with "level" followed by a number, and is a .txt file.

Thanks to Thorbjørn Lindeijer and other contributors for their awesome software, Tiled!

======================About the code======================
The game code was designed in a very basic way; There was a Land object(block), Player object(User), and a Weapon object(sword).
It was originally designed as a tech demo to try out a 100% collision based approach to a side scroller. The code proved to work
fine as long as there aren't too many blocks, so I scaled the block size up so they'd fit throughout the level. But then, since
my prototype was chosen for the final project and because of the limited time, I went ahead and modded my own "engine" in order
to convert it from a demo to a game. The demo was never designed to have the user falling off high heights, fighting A.I., blocks
to move, etc. All the new features added tricked the engine into making fancy features. Modding the engine caused various issues,
and I had to make clever work arounds for each of these. But because it was so challanging to get blocks to move and make the user
respawn, I wasted all my time on making the basics work, and polishing them so that players don't have to look as a extremely shaky
screen while riding a platform, nor have to make flat maps. So I had to remove Bosses and the "final level" from my schedule because
I wanted the game to be fun, since all that stuff would have taken a while to code for only 10% of the gameplay. The best feature
in my opinion was the .txt to game level converter, this allowed easy creation of maps and made the game feel more like a sandbox.
This greatly extends the game's life span, and makes it more fun to a creative audience since the actual game doesn't nessassarily
compare to the kinds of Indie games you buy online and Steam, so the more hardcore audience will just pass it by. 

=====================Known Bugs=========================

# *shell hitboxes aren't aligned with the images when facing backwards

# *middle resolution uses a float, causing issues while riding platforms that cannot be fixed

# *projectiles have a chance to go through a hitbox because they move several pixels at a time

# *platforms cannot be combined into larger platforms

# *can't play all sounds at once, some get skipped

======================How to play======================
The objective of the game is to make it to the portal in the map, which is usually at the end unless there is a creative twist.
This game teaches you to avoid story aspects just as good looking senory and norms just as "follow the hallway" to get to the end,
because doing so will only get you killed. It's essentually a trap! In this game, you have look at the world as a set of blocks
and A.I. and how they will act. You have to exploit their simplicity to your advantage! Another aspect is collateral damage, and
how there are actually regrets! (disreguard the manly title!) During the game, you will have to fight A.I. one way or the other,
and doing so can lead to some heavy destruction! So blasting your way through walls and showering them in bullets is not a good
apporach. That may lead to breaking the path to the portal, causing you to be trapped. Although, there are good times to destroy
blocks, such as to cause A.I. to fall off the map. (Just make sure the part is still passible from your direction) The game gives
you a set of armour that you regain after every respawn and new level, but you cannot get it back during a level. You also get
unlimited attemps to pass a level and win the game by reaching the last portal. Good luck, have fun, and remember that exploits
are part of the game... so don't keep walking into ambushes expecting to win. This isn't one of those AAA games where glitching
out of the boundaries takes away the fun, instead it adds to the fun!
Note: if you are unable to complete the story mode because you are stuck at a part, there is a pro walkthrough video in the archive
called "VideosAndScreens.rar"

===================Attributions=========================
Sounds:
	Sword Swing
		Recorded by Mike Koenig
	Spear Throw
		Recorded by Mike Koenig
	Shotgun Pump
		Recorded by Mike Koenig
	