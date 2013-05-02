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


4.) Create your map! Tiled has some awesome tools available ranging from rectangular select, stamp, and a paint bucket.

Note: Enemy and character spawns should have an empty block between them and any other block (underneath). Portals require a 2x2 area free around them. Weapons with blue backgrounds are weapon spawners and require an empty block under them, and weapons with red backgrounds are AI spawners. The green block with a smiley face is the player spawner. You MUST have a player spawner in the map for it to work.


5.) After you are finished you can save your map. By default Tiled saves using a .tmx extension. After you save, export your file using a .lua extension. THIS is the file that you will be converting to our format.


6.) There is a python script in the "Custom Maps" folder. You may either copy this into the folder you saved your .lua map, or you can copy your file into the custom maps folder. Afterward, run "convert.py". It will prompt you for a file, simply enter the file name you exported to. Then enter the file name you wish to use for the output. The game will only load files beginning with level####.txt, so make sure the naming is appropriate. Levels are loaded in a sorted order numerically.


7.) Now when you start the game, make sure to select custom maps, and you will begin with the first custom level in the folder!


Note: If you run into issues after converting your file, make sure you did not export a map with multiple layers or tilesets. Also make sure your level is named appropriately, begins with "level" followed by a number, and is a .txt file.

Thanks to Thorbjørn Lindeijer and other contributors for their awesome software, Tiled!