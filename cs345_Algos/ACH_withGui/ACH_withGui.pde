int n = 0;  //<>// //<>// //<>// //<>// //<>// //<>// //<>// //<>// //<>// //<>// //<>// //<>// //<>// //<>// //<>// //<>//
PrintWriter output;
/*-------------------------------IMPORTS--------------------------------------*/
import java.util.Random;
import java.io.*;
import java.util.Random;
import java.lang.Math;
import java.util.concurrent.TimeUnit;

//import controlP5.*;

//ControlP5 textfield; // this doesn't work for some reason... for now we'll have to hardcode in the filename in mousePressed()

int  xs=10;   //where to start printing on the panel
int  ys=20;
int heapCounter=10;
int heaparray=100;
//int arrA [] = {3, 2, 1, 7, 8, 55, 10,23,45,78, 16, 12};
int arr[] = new int[ heaparray];
String filename = "";
PVector[] q = {};
PVector[] Stack = {};
int top = 0;
int indexForStack = 3;
boolean closeConvexHull = false;
String userText = "";
String fileName = "";
String errorText = "";
//Buttons
Button readFileButton;
Button restartButton;
Button convexHull;
Button quitButton;
Button sortButton;
Button showGH;
Button heapSort;
Button heapHighlight;

boolean flagDrawHeapManual=false;
boolean flagheapHighlight=false;
boolean showpoints = false;
boolean showpoly = false;
boolean showminmax = false;
boolean showHeap=false;

int heapRootX=520;
int heapRootY=50;
MyTree t = new MyTree();

void setup() {
  size(1200, 700);

  int width = 1200;
  int height = 700;


  output = createWriter("positions.txt"); 
  smooth();
  textSize(16);

  background(255);


  //Create Clickable Buttons
  restartButton = new Button("Restart", 15, height-50, 115, 35);
  readFileButton = new Button("Read File", 145, height-50, 115, 35);
  sortButton = new Button("Sort", 275, height-50, 115, 35);
  showGH = new Button("Graham Scan", 405, height-50, 115, 35);
  convexHull = new Button("Show Convex Hull", 535, height-50, 145, 35);
  quitButton = new Button("Quit!", 685, height-50, 115, 35);
  heapSort = new Button("Build Heap!", 800, height-50, 115, 35);
  heapHighlight= new Button("Heap Highlight!", 920, height-50, 125, 35);

  Heap<Integer> tmp = new Heap<Integer>();


  Integer[] a = {0, 1, 2, 5, 3, 7, 4, 7, 5, 7 };
  for (int i=0; i<a.length; i++) {
    tmp.insert(a[i]);
  }
  //  System.out.println(tmp.toString());
  // tmp.heapSort(a);
  // t.totalnodes=a.length;
  heapSort(a);
}

void draw() {
  smooth();
  fill(255, 255, 255);
  rect(0, 0, 1200, 800);
  fill(0);
  rect(0, height-100, 1200, 100);
  fill(255, 255, 255);
  drawButtons();
  fill(256, 256, 256);
  textAlign(LEFT, TOP);
  //text("Type Filename: " + userText, 10, 410, width, height);
  text("Type Filename: " + userText, 0, height -80);
  // fill(250, 0, 0);
  text(errorText, width-200, height -80, width, height);
  //text(errorText, 10, 410, width, height);

  if (flagDrawHeapManual)
  {
    int counter=1;
    drawHeapManual(heapRootX, heapRootY, counter, 0);
  }

  if (flagheapHighlight)
  {
    int counter=1;
    //heapHighlight(heapRootX, heapRootY, counter,false,false, false);
    heapHighlight(heapRootX, heapRootY, counter, true, true, true);
  }
  if (showpoints)
  {
    drawPoints();
    for (int i=0; i<q.length; i++ ) text("  "+i, q[i].x, q[i].y);
  }

  if (showHeap)
  {


    drawTree(t.root);
  }
  stroke(100, 30, 30);
  if (top > 0) {
    drawCH();
  }
}

/*******************************************************************************
 * keyPressed()
 *
 * Description: Handles all user input from the keyboard
 *
 *******************************************************************************/
void keyPressed() {
  //errorText = key+"key pressed";
  errorText = "";
  if ((key == 'R')||(key == 'r')) {
    errorText = "restarted";
    restart();
  } else if (keyCode == BACKSPACE) {
    if (userText.length() > 0) {
      userText = userText.substring(0, userText.length()-1);
    }
  } else if (keyCode == DELETE) {
    userText = "";
  } else if (key == ENTER) {

    if (userText!="")
    {
      String temp = userText;
      restart();
      fileName = temp;
      userText = temp;


      try
      {
        readFile(fileName);
      }
      catch(Exception e) {
        errorText="File Not Found";
        //e.printStackTrace();
      }
    } else
    {
      errorText="File Not Found";
    }
  } else if (keyCode != SHIFT && keyCode != CONTROL && keyCode != ALT) {
    userText = userText + key;
  }
}//END keyPressed


void drawCH() {
  for (int j = 1; j <= top; j++) { 
    line(Stack[j-1].x, Stack[j-1].y, Stack[j].x, Stack[j].y);
  }
  if (closeConvexHull) {
    line(Stack[top].x, Stack[top].y, Stack[0].x, Stack[0].y);
  }
}

void drawHeap(int arr[]) {
  //javax.swing.JOptionPane.showMessageDialog(null, "inside drawHeap!");
  int i ;
  for (i=0; i<arr.length; i++) {
    fill(i*3, i*3, 255 ); 
    ellipse(arr[i], arr[i], 10, 10 );
  }
}

int cycleCounter=1;

void drawHeapManual2(int x, int y)
{
  //cycleCounter=cycleCounter+1;

  //if (cycleCounter==3)
  //{
  //  return;
  //}

  x=x+10;
  y=y+10;
  //draw root
  fill(212, 12, 23);
  ellipse(x, y, 10, 10);

  int xl=x-30;
  int yl=y+30;


  int xr=x+30;
  int yr=y+30;


  for (int i=0; i<10; i++) {

    ////draw root
    //x=x+10;
    //y=y+10;
    //fill(212, 12, 23);
    //ellipse(x, y, 10, 10);

    //draw left child
    xl=xl-30;
    yl=yl+30;
    fill(212, 12, 23);
    ellipse(xl, yl, 10, 10);


    //draw right child
    xr=xr+30;
    yr=yr+30;
    fill(212, 12, 23);
    ellipse(xr, yr, 10, 10);
  }


  // drawHeapManual(x-10, y-10);
}


void heapHighlight(int x, int y, int cycleCounter, boolean left, boolean right, boolean root)
{
  try
  {

    boolean lHighlight=true;
    double len=(double)q.length;

    double levels=Math.log(len);
    if (cycleCounter<(levels+1))
    {


      //draw root

      if (root)
      {
        fill(0, 0, 0);
        //  fill(212, 12, 23);
        ellipse(x, y, 20, 20);
        // stroke(255, 255, 255); 
        // strokeWeight(40);
      } else
      {
        fill(212, 12, 23);
        ellipse(x, y, 20, 20);
      }

      int xl=x-100;
      int yl=y+100;
      line(x, y, xl, yl);

      if (left)
      {

        //    //draw left child
        fill(0, 0, 0);
        ellipse(xl, yl, 20, 20);
        // TimeUnit.SECONDS.sleep(3);
        heapHighlight(xl, yl, cycleCounter+1, true, false, false);
      } else
      {
        //    //draw left child
        fill(212, 12, 23);
        ellipse(xl, yl, 20, 20);
        heapHighlight(xl, yl, cycleCounter+1, false, false, false);
        //TimeUnit.SECONDS.sleep(1);
      }

      int xr=x+100;
      int yr=y+100;
      line(x, y, xr, yr);

      if (right)
      {
        //draw right child
        fill(0, 0, 0);
        ellipse(xr, yr, 20, 20);
        //stroke(255, 0, 255); 
        //strokeWeight(100);
        heapHighlight(xr, yr, cycleCounter+1, false, true, false);
      } else
      {
        //draw right child
        fill(212, 12, 23);
        ellipse(xr, yr, 20, 20);
        //stroke(255, 0, 255); 
        //strokeWeight(100);
        heapHighlight(xr, yr, cycleCounter+1, false, false, false);
      }
    }
  }
  catch(Exception e) {
    errorText="File Not Found";
    //e.printStackTrace();
  }
}



void drawHeapManual(int x, int y, int cycleCounter, int nodeCounter)
{
  double len=(double)q.length;

  double levels=Math.log(len);
  if (cycleCounter<(levels+1))
  {


    //draw root
    fill(212, 12, 23);
    ellipse(x, y, 20, 20);
    fill(0, 0, 0);
    if (nodeCounter==0)
    {
      text(q[nodeCounter].x+","+q[nodeCounter].y, x+30, y);
    }

    int xl=x-100;
    int yl=y+100;

    line(x, y, xl, yl);
    //    //draw left child
    fill(212, 12, 23);
    ellipse(xl, yl, 20, 20);


    text(q[nodeCounter+1].x+","+q[nodeCounter+1].y, xl+30, yl);

    drawHeapManual(xl, yl, cycleCounter+1, nodeCounter+1);



    int xr=x+100;
    int yr=y+100;
    line(x, y, xr, yr);

    //draw right child
    fill(212, 12, 23);
    ellipse(xr, yr, 20, 20);
    text(q[nodeCounter+2].x+","+q[nodeCounter+2].y, xr+30, yr);
    drawHeapManual(xr, yr, cycleCounter+1, nodeCounter+2);
    //text(q[nodeCounter+1].x+","+q[nodeCounter+1].y, xr+30, yr);
  }
}



void drawPoints() {

  int i ;
  for (i=0; i<q.length; i++) {
    fill(i*3, i*3, 255 ); 
    ellipse(q[i].x, q[i].y, 10, 10 );
  }




  //ab code

  //  for(int i = 0; i < q.length; i++) {
  //    fill(i*3, i*3, 255); 
  //    ellipse(q[i].x, q[i].y, 10, 10);
  //  }

  if (showpoly) {
    strokeWeight(2 );
    stroke(250, 0, 0); 
    for (i=0; i<99; i++) {
      line(q[i].x, q[i].y, q[i+1].x, q[i+1].y) ;
    }
    stroke(0, 0, 255); 
    line(q[99].x, q[99].y, q[0].x, q[0].y) ;
  }

  /*if(showpoly) {
   strokeWeight(2);
   stroke(250, 0, 0); 
   for(int i = 0; i < q.length-1; i++) {
   line(q[i].x, q[i].y, q[i+1].x, q[i+1].y) ;
   }
   stroke(0, 0, 255);
   if(q.length > 0) {
   line(q[q.length-1].x, q[q.length-1].y, q[0].x, q[0].y);
   }
   }*/
  stroke(0, 0, 255); 
  fill(0, 102, 153, 204);

  //ab code
  //for(int i = 0; i < q.length; i++) {
  //  text("  " + i, q[i].x, q[i].y);
  //}
}

void sort2 () {
  background(255); 
  PVector tmp; 
  for (int i = 0; i < q.length - 1; i++)
    for (int j = i+1; j < q.length; j++)
      if ((i > 0 && 0 > det3(q[i].x, q[i].y, q[0].x, q[0].y, q[j].x, q[j].y)) || (i == 0 && q[i].y > q[j].y)) {
        tmp = q[i].copy();
        q[i] = q[j].copy();
        q[j] = tmp.copy();
      }
  fill(0, 102, 153, 204);
}

float det3(float x1, float y1, float x2, float y2, float x3, float y3) {
  float z = (x2 * y3  - y2 * x3) - (x1 * y3 - y1 * x3) + (x1 * y2 - y1 * x2); 
  if (z == 0) println("z = 0"); 
  return z;
}

void readFile(String filename) {
  //javax.swing.JOptionPane.showMessageDialog(null, "inside readFile!");
  //  javax.swing.JOptionPane.showMessageDialog(null, "filename!"+filename);
  try
  {


    String str= null;
    ArrayList<Integer> xl = new ArrayList();
    ArrayList<Integer> yl = new ArrayList();
    ArrayList<Integer> indicesl = new ArrayList();

    BufferedReader read;


    //float[] x = {};
    //float[] y = {};
    //int[] indices = {};
    int index = 0;
    read = createReader(filename);

    int lineCounter=0;
    n=100;


    while ((str = read.readLine()) != null) {
      if (lineCounter==0)
      {
        n = Integer.parseInt(str);
        lineCounter=lineCounter+1;
      } else
      {
        //javax.swing.JOptionPane.showMessageDialog(null, "inside counter>1 value of str is!"+str);   
        String[] words = str.split("\\s+");
        // javax.swing.JOptionPane.showMessageDialog(null, " words[0] is !"+words[0]); 

        if (words.length>2)
        {

          xl.add(Integer.parseInt(words[0]));
          yl.add(Integer.parseInt(words[1]));
          indicesl.add(Integer.parseInt(words[2]));

          //xl.add(Math.round(Float.parseFloat(words[0])));
          //yl.add(Math.round(Float.parseFloat(words[1])));
          //indicesl.add(Math.round(Float.parseFloat(words[2])));
          index++;  
          lineCounter=lineCounter+1;
        }
      }
    }
    Integer[] x = new Integer [n];
    x = xl.toArray(x);
    Integer[] y= new Integer [n];
    y = yl.toArray(y);
    Integer[] indices = new Integer [n];
    indices = indicesl.toArray(indices);

    q = new PVector[n]; // initialize points
    for (int i = 0; i < n; i++) {
      q[i] = new PVector(x[i], y[i], indices[i]);
    }

    Stack = new PVector[q.length];
    for (int i=0; i < q.length; i++) {
      Stack[i] = new PVector(0, 0, 0);
    }
    top = 0;
    indexForStack = 3;
    closeConvexHull = false;

    //write the points to a file
    //output.println(n);
    //for(int lc=0;lc<n;lc++)
    //{
    //output.println(x[lc]+" "+y[lc]+" "+lc);
    //}
    //output.flush(); // Writes the remaining data to the file
    //output.close(); // Finishes the file
    showpoints = true;
  }
  catch(Exception e) {
    errorText="File Not Found";
    //e.printStackTrace();
    showpoints = false;
  }
}

//public boolean fileExists(String fileName) {
//  File file=new File(fileName);
//  boolean exists = file.exists();
//  if (!exists) {
//    return false;
//  } else {
//    return true;
//  }
//} 

void restart() { // need to fix so stuff isn't hard-coded


 flagDrawHeapManual=false;
 flagheapHighlight=false;

  n = 0;
  showHeap=false;
  userText = "";
  errorText = "";
  fileName = "";
  showpoints=false;
  showpoly=false;
  showminmax=false;
  closeConvexHull=false;
  top=0;
  flagDrawHeapManual=false;
}

/*******************************************************************************
 * mousePressed()
 *
 * Description: Handles logic for mouse presses.
 *              A single mouse click could be hitting any of the buttons.
 *******************************************************************************/
void mousePressed() {
  // println(mouseX);
  // println(mouseY);
  // user presses "Restart"
  if (restartButton.mouseOver()) {
    //javax.swing.JOptionPane.showMessageDialog(null, "Restarted!");
    restart();
  }
  if (heapHighlight.mouseOver())
  {

    restart();
    flagheapHighlight=true;
    // javax.swing.JOptionPane.showMessageDialog(null, "heapHighlight pressed !");
    //HeapHighlight(t.root);

    // flagDrawHeap=true;
  }

  // user presses "Read File" or "Read New File"
  if (readFileButton.mouseOver()) {


    if (userText!="")
    {


      String temp = userText;
      fileName = temp;
      userText = temp;

      try
      {
        readFile(fileName);

        //restart();
      }
      catch(Exception e) {
        errorText="File Not Found";
        //e.printStackTrace();
      }
    } else
    {
      errorText="Empty file name";
    }
  }
  // user presses "Quit"
  if (quitButton.mouseOver()) {
    //javax.swing.JOptionPane.showMessageDialog(null, "Quitting!");
    exit();
  }
  if (heapSort.mouseOver()) {

    for (int i=0; i<q.length; i++ ) println( q[i].x+"_"+ q[i].y);
    restart();

    flagDrawHeapManual=true;
    //showHeap=true;
    // javax.swing.JOptionPane.showMessageDialog(null, "after value of showHeap is "+showHeap);
    //heapSort();
  }

  if (sortButton.mouseOver()) {
    sort2();
  }

  if (convexHull.mouseOver()) {
    sort2();
    gs();
    closeConvexHull = true;
  }

  if (showGH.mouseOver()) {
    sort2();
    gs_step();
  }
} //END mousePressed

//int starter=99;
public void drawTree(  Node root) {//actually draws the tree

  // javax.swing.JOptionPane.showMessageDialog(null, "drawTree !");

  //this.t = t; // allows dispay routines to access the tree


  int dx, dy, dx2, dy2;
  int SCREEN_WIDTH=800; //screen size for panel
  int SCREEN_HEIGHT=700;
  int XSCALE, YSCALE; 
  //int totalNodes=arrA.length;
  XSCALE=SCREEN_WIDTH/t.totalnodes; //scale x by total nodes in tree
  YSCALE=(SCREEN_HEIGHT-ys)/(t.maxheight+1); //scale y by tree height

  if (root != null) { // inorder traversal to draw each node

    dx = root.xpos * XSCALE; // get x,y coords., and scale them 
    dy = root.ypos * YSCALE +ys;
    //dx = root.xpos; // get x,y coords., and scale them 
    //dy = root.ypos;


    String s = (String) root.data; //get the word at this node

    ellipse(dx, dy, 10, 10 );
    stroke(23, 78, 56);
    strokeWeight(4);
    fill(234, 123, 255 ); 

    // this draws the lines from a node to its children, if any
    if (root.left!=null) { //draws the line to left child if it exists
      dx2 = root.left.xpos * XSCALE; 
      dy2 = root.left.ypos * YSCALE +ys;

      text(t.inputString, dx2+2, dy2+2);


      line(dx, dy, dx2, dy2);
    }
    if (root.right!=null) { //draws the line to right child if it exists
      dx2 = root.right.xpos * XSCALE;//get right child x,y scaled position
      dy2 = root.right.ypos * YSCALE + ys;

      //dx2 = root.right.xpos ;//get right child x,y scaled position
      //dy//2 = root.right.ypos  ;

      line(dx, dy, dx2, dy2);
      strokeWeight(1);
    }
    drawTree( root.left); // do left side of inorder traversal
    drawTree( root.right); //now do right side of inorder traversal
  }
}



public void HeapHighlight (  Node root) {//actually draws the tree

  //javax.swing.JOptionPane.showMessageDialog(null, "drawTree !");

  //this.t = t; // allows dispay routines to access the tree

  try {
    int dx, dy, dx2, dy2;
    int SCREEN_WIDTH=800; //screen size for panel
    int SCREEN_HEIGHT=700;
    int XSCALE, YSCALE; 
    //int totalNodes=arrA.length;
    XSCALE=SCREEN_WIDTH/t.totalnodes; //scale x by total nodes in tree
    YSCALE=(SCREEN_HEIGHT-ys)/(t.maxheight+1); //scale y by tree height

    if (root != null) { // inorder traversal to draw each node
      HeapHighlight( root.right); //now do right side of inorder traversal
      TimeUnit.SECONDS.sleep(1);
      dx = root.xpos * XSCALE; // get x,y coords., and scale them 
      dy = root.ypos * YSCALE +ys;
      //dx = root.xpos; // get x,y coords., and scale them 
      //dy = root.ypos;


      String s = (String) root.data; //get the word at this node

      ellipse(dx, dy, 10, 10 );
      stroke(23, 78, 56);

      fill(234, 123, 255 ); 

      // this draws the lines from a node to its children, if any
      if (root.left!=null) { //draws the line to left child if it exists
        dx2 = root.left.xpos * XSCALE; 
        dy2 = root.left.ypos * YSCALE +ys;

        text(t.inputString, dx2+2, dy2+2);
        strokeWeight(5);

        line(dx, dy, dx2, dy2);
      }
      if (root.right!=null) { //draws the line to right child if it exists
        dx2 = root.right.xpos * XSCALE;//get right child x,y scaled position
        dy2 = root.right.ypos * YSCALE + ys;

        //dx2 = root.right.xpos ;//get right child x,y scaled position
        //dy//2 = root.right.ypos  ;

        line(dx, dy, dx2, dy2);
        strokeWeight(4);
      }

      HeapHighlight( root.left); // do left side of inorder traversal
    }
  }

  catch(Exception e) {
    errorText="File Not Found";
    //e.printStackTrace();
  }
}


void heapSort(Integer[] array)
{
  // showHeap=true;

  System.out.print("Original Array : ");


  //MyTree t = new MyTree(); // t is Binary tree we are displaying
  for (int i=0; i<array.length; i++) {

    String word=Integer.toString(array[i]);
    t.root = t.insert(t.root, word);  //insert word into Binary Search Tree
    t.inputString= t.inputString + " " + word; // add word to input string
  }
  t.computeNodePositions(); //finds x,y positions of the tree nodes
  // t.maxheight=3;
  t.maxheight=t.treeHeight(t.root); //finds tree height for scaling y axis

  //  DisplaySimpleTree dt = new DisplaySimpleTree(t);//get a display panel
  //  dt.setVisible(true); //show the display
}


//Random rand = new Random();




//for (int i = 0; i < heaparray; i++)
//{
//  arr[i] = rand.nextInt(50);
//}

////HeapSort objHeapSort= new HeapSort();

//// objHeapSort.sort(arr);

//objHeapSort.heapify(arr);

//for (int i = 0; i < heaparray; i++)
//{
//  println(arr[i]);
//}


//showHeap =true;

//for (int i = 0; i < n; i++)
//{
//  System.out.print(arr[i]+" ");
//}

void gs() {
  Stack[0] = q[0].copy();
  Stack[1] = q[1].copy(); 
  ellipse(Stack[0].x, Stack[0].y, 30, 2); 
  ellipse(Stack[1].x, Stack[1].y, 30, 2);
  top = 1;
  for (int i = 3; i < Stack.length; i++) {
    while ((top > 1) && (0 < det3(Stack[top-1].x, Stack[top-1].y, Stack[top].x, Stack[top].y, q[i].x, q[i].y))) {  
      fill(255, 0, 0); 
      ellipse(Stack[top].x, Stack[top].y, 2, 20);
      top--;
    }
    top++;
    Stack[top] = q[i].copy();
    println("top:", top);
  }
}

void gs_step() {
  if (top >= Stack.length || indexForStack >= q.length) {
    closeConvexHull = true;
    return;
  }
  if (top == 0) {
    Stack[0] = q[0].copy();
    Stack[1] = q[1].copy();
    ellipse(Stack[0].x, Stack[0].y, 30, 2);
    ellipse(Stack[1].x, Stack[1].y, 30, 2);
    top = 1;
  } else {
    while ((top > 1) && (0 < det3(Stack[top-1].x, Stack[top-1].y, Stack[top].x, Stack[top].y, q[indexForStack].x, q[indexForStack].y))) {
      fill(255, 0, 0);
      ellipse(Stack[top].x, Stack[top].y, 2, 20);
      top--;
    }
    top++;
    Stack[top] = q[indexForStack].copy();
    println("top:", top);
    indexForStack++;
  }
}

void drawButtons() {
  readFileButton.setText("Read File");
  restartButton.drawButton();
  readFileButton.drawButton();
  sortButton.drawButton();
  quitButton.drawButton();
  convexHull.drawButton();
  showGH.drawButton();
  heapSort.drawButton();
  heapHighlight.drawButton();
}