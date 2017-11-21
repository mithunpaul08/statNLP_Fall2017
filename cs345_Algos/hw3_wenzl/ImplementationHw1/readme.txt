Author: Lukas Wenzl

functionality:
Restart Button: resets program
Load File Button: Loads file (.in) with filename given above, the filenmae can be changed at all times
		  by typing on the keyboard. The program can handle nonexistant files and ignores points outside of the canvas
Sort: Finds 'lowerst' (in processing highest) Point and sorts all points CCW around it
Graham Scan: Performs one step of Graham Scan
Convex Hull: Performs all steps of Graham Scan and saves file with suffix "_convex_hull.out" into the data folder
Quit: Closes the program
FUN: Press at any time when there are points on screen and see what happens

//Bonus
BuildHeap Button: After Loading a file this can be pressed. It creates the heap from the datapoints and displays them on screen. 
		Then an animation goes through all the subtrees (including the leaves) and highlights them. 
		Pressing BuildHeap again brings you back to the normal view.
