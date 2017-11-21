/*--------------------------------------------------------------------------------------------
 * Author Lukas Wenzl
 * 
 * Solution for the first implementation homework. 
 * Finds convex Hull for a set of points
 *-------------------------------------------------------------------------------------------*/



import static java.lang.Math.sqrt;


//Buttons
Button readFileButton;
Button restartButton;
Button sortButton;
Button grahamButton;
Button convexhullButton;
Button quitButton;
Button buildheapButton;
Button funButton;

//to check how far we are in the process
boolean simplepolyexists;
boolean connectPointsInOrder;
boolean convexHullExists;
int grahamStep;
//BONUS
boolean displayHeap;
boolean heapCreated;
int startTime;
boolean fun;

//DataStructure
Point[] A;
int A_size;
Stack S;
Heap heap;
GrahamScan grahamScan;

ReadFile readFile;
String filename;
boolean fileexists;



void setup() {
  size(800, 500);
  smooth();
  textSize(16);
  frameRate(30);
  
  //Create Clickable Buttons
  restartButton = new Button("Restart", 15, 450, 115, 35);
  readFileButton = new Button("Read File", 145, 450, 115, 35);
  sortButton = new Button("Sort", 275, 450, 115, 35);
  grahamButton = new Button("Graham Scan", 405, 450, 115, 35);
  convexhullButton = new Button("Convex Hull", 535, 450, 115, 35);
  quitButton = new Button("Quit", 665, 450, 115, 35);
  buildheapButton = new Button("Build Heap",  665, 410, 115, 35);
  funButton = new Button("FUN",  535, 410, 115, 35);
  
  
  resetVariables();
  loop();
} //END setup

void draw() {
  smooth();
  fill(256,256,256);
  rect(0, 0, 799, 399);
  
  fill(0);
  rect(0, 400, 800, 100);
  fill(256,256,256);
  drawButtons();
  fill(256,256,256);
  if (fileexists==false) {
   fill(256,0,0); 
  }
  textAlign(LEFT, TOP);
  text("Filename: " + filename, 10, 410, width, height);
  fill(250,0,0);
  
  if (!displayHeap) {
    //draw all the points
    for(int i=0; i<A_size; i++) {
      A[i].drawPnt(0);
    }
    
    //Draws current Polygon
    if (connectPointsInOrder && A_size>1) { //if A_size 1 or smaler then no lines have to be drawn
      int start = grahamStep;
      if(grahamStep>0) start--;
      for (int i=start; i<A_size-1; i++) {
        line(A[i].x, A[i].y, A[i+1].x, A[i+1].y);
      }
      line (A[0].x, A[0].y, A[A_size-1].x, A[A_size-1].y);
    }
    
    //draw convex Hull
    if(grahamStep > 0 ) {
      S.drawStack();
      if(convexHullExists){
        S.finishHull();
      }
    }
  } else { //BONUS display Heap
    int doubleseconds = (int) (System.currentTimeMillis() - startTime)/2000;
    if (doubleseconds >0 && doubleseconds < heap.heap_size) {
      heap.HeapHighlight(doubleseconds);
    }
    heap.displayHeap();
  }
  
  
  //FUN
  if (fun)  {
    for(int i=0; i<A_size; i++) {
      int up = round(random(10)-5);
      int right = (int)(random(10)-4.99);
      A[i].x = A[i].x +right;
      A[i].y = A[i].y + up;
    }
  }
  
   
} //END draw

/*******************************************************************************
 * restart()
 *
 * Description: clears all global variables so that the user can restart the
 *              program without stopping the entire thing.
 *******************************************************************************/
void restart() {
  resetVariables();
  redraw();
} //END restart


/*******************************************************************************
 * mousePressed()
 *
 * Description: Handles logic for mouse presses.
 *              A single mouse click could be hitting any of the buttons.
 *******************************************************************************/
void mousePressed() {
  // user presses "Restart"
  if (restartButton.mouseOver()) {
    restart();
  }
  // user presses "Read File" or "Read New File"
  else if (readFileButton.mouseOver()) {
    
    if (A_size == 0 ) {
      //DataStructure
      fileexists = true;
      try {
        readFile = new ReadFile(filename + ".in");
        A = readFile.getArray(filename);
        A_size = readFile.size;
      } catch (NullPointerException e) {
        fileexists = false;
      }
      
      loop();
    }
  }
  // user presses "Quit"
  else if (quitButton.mouseOver()) {
      //javax.swing.JOptionPane.showMessageDialog(null, "Quit Button Pressed ");
    exit();
  }
  // user presses "Sort"
  else if (sortButton.mouseOver() ) {
    if (A_size > 0 && !simplepolyexists) {
     simplePoly();
    }
    
  }
  // user presses "Graham Scan"
  else if (grahamButton.mouseOver()) {
       if(simplepolyexists) {
         oneStepGrahamScan();
       }
  
    }
  // user presses "Convex Hull"
  else if (convexhullButton.mouseOver() ) {
    if(simplepolyexists) {
      while(!convexHullExists) {
        oneStepGrahamScan();
      }
    }
  }
  // user presses "Build Heap"
  else if (buildheapButton.mouseOver() ) {
    if (A_size >0) {
      if (displayHeap) displayHeap = false;
      else {
        if (!heapCreated) {
          heap = new Heap(A, A_size, findBottomPoint());
          heap.buildMaxHeap();
          heapCreated = true;
        }
        displayHeap = true;
        startTime= (int) System.currentTimeMillis();
        //A[1].highlight();
        
      }
    }
  }
    // user presses "FUN"
    else if (funButton.mouseOver() ) {
      if(fun) fun=false;
      else fun=true;
      println("FUN");
    }

      
  
} //END mousePressed


/*******************************************************************************
 * keyPressed()
 *
 * Description: Handles logic for key presses.
 *              Here it is used to put in the file name.
 *******************************************************************************/
void keyPressed() {
  if (keyCode == BACKSPACE) {
    if (filename.length() > 0) {
      filename = filename.substring(0, filename.length()-1);
    }
  } else if (keyCode == DELETE) {
    filename = "";
  } else if (keyCode != SHIFT && keyCode != CONTROL && keyCode != ALT) {
    filename = filename + key;
  }
}


/*******************************************************************************
 * drawButtons()
 *
 * Description: Draws all program buttons (defined as global variables)
 *******************************************************************************/
void drawButtons() {
  
  readFileButton.setText("Read File");
  restartButton.drawButton();
  readFileButton.drawButton();
  grahamButton.drawButton();
  convexhullButton.drawButton();
  sortButton.drawButton();
  quitButton.drawButton();
  buildheapButton.drawButton();
  funButton.drawButton();
 
}

/*******************************************************************************
 * resetVariables()
 *
 * Description: rests all the global variables
 *******************************************************************************/
void resetVariables()
{
  filename="points_in";
  simplepolyexists=false;
  fileexists = true;
  //A = null;
  A_size = 0;
  connectPointsInOrder = false;
  convexHullExists = false;
  grahamStep = 0;
  displayHeap = false;
  heapCreated = false;
  startTime = 0;
  fun = false;
}

/*******************************************************************************
 * simplePoly()
 *
 * Description: sorts the points into a simple Polygon and displays the Polygon
 *******************************************************************************/
void simplePoly() {
  
  int start = findBottomPoint();
  
  
  /**********************
  ** first try with simple sorting algorithm and use of angles **/ /*
  //find smalest point to the left (take first one if multiple)
  A[start].setNumber(0);
  A[start].setAngle(2);

  //calculate Angles
  for (int i=0; i<A_size; i++) {
    if(A[start].x != A[i].x || A[start].y != A[i].y) {
      int xvar = A[i].x - A[start].x;
      int yvar = A[i].y - A[start].y;
      int lensquare = xvar*xvar + yvar*yvar;
      A[i].setAngle(-xvar/sqrt(lensquare)); //using cos(angle) instead of angle not need to use arccos, minus for ccw
      //println(A[i].angle); //test
    
    } else { //in case point lies on top of startin point
      A[i].setAngle(2);
    }
  }
  
  SimpleSort simpleSort = new SimpleSort(A, A_size);
  simpleSort.sort();
  
  for (int i=0; i< A_size; i++) {
    A[i].setNumber(i);
  }
  
  
  connectPointsInOrder = true;
  simplepolyexists = true;
  *//***********************************************/
  
  if (!heapCreated) {
    heap = new Heap(A, A_size, start);
    heap.buildMaxHeap();
    heapCreated = true;
  }
  heap.sort_CCW();
  
  for (int i=0; i< A_size; i++) {
    A[i].setNumber(i);
  }
  
  connectPointsInOrder = true;
  simplepolyexists = true;
  
  
}

/*******************************************************************************
 * findBottomPoint()
 *
 * Description: Finds the bottom (leftmost) point. We need this point to sort all 
               other points CCW around it
 *******************************************************************************/
int findBottomPoint() {
  int start = 0;
  int xmin = 800;
  int ymin = 500;
  for (int i=0; i<A_size; i++) {
    if (A[i].y < ymin || (A[i].y == ymin && A[i].x < xmin)) {
      xmin = A[i].x;
      ymin = A[i].y;
      start = i;
    }
  }
  return start;
}


/*******************************************************************************
 * oneStepGrahamScan()
 *
 * Description: does one step of Graham Scan
 *******************************************************************************/
void oneStepGrahamScan() {
  //if not yet startet initiate Graham Alg
  if (!convexHullExists) { //if convex hull exists already there is nothing to do
    
    if (grahamStep==0) {
      S = new Stack();
      grahamScan = new GrahamScan(A, A_size, S);
      grahamStep=2;
      if (S.SA.size() == 1) { //in case of only one point
        grahamStep=1;
        convexHullExists = true;
      }
    } else {
    //do one step
    grahamScan.doStep(grahamStep);
    grahamStep++;
    }
    
    
    
    if (grahamStep == A_size) {
      convexHullExists = true;
    }
    
    if(convexHullExists) {
      WriteFile writeFile = new WriteFile("data/" + filename + "_convex_hull.out");
      writeFile.saveData(S.SA);
      writeFile.closeWriter();
      
      
      
    }
  }
}