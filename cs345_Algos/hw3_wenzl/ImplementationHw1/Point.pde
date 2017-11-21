/*--------------------------------------------------------------------------------------------
 * Author Lukas Wenzl
 * 
 *
 * description: Class to handle the points on screen. Also used to display the points and 
 *              hold information specific to the point (like highlighting)
 *-------------------------------------------------------------------------------------------*/


class Point {
  int x; //xposition
  int y; //yposition
  int i; //index
  int index_in_simple_poly;
  
  boolean isPartOfSimplePoly;
  boolean isPartOfConvexHull;
  //double angle; //cosine of angle for now, will go from 1 to -1              ///was only used for simpleSort!
  int redness;
  int blueness;
  int radius;
  
  //BONUS
  int yellowness;
  
  Point(int xpos, int ypos, int index)
  {
    x = xpos;
    y = ypos;
    i = index;
    redness = 0;
    blueness = 0;
    yellowness = 0;
    radius = 10;
    index_in_simple_poly = -1;
    //angle = 2;
    
    isPartOfSimplePoly = true;
    isPartOfConvexHull = false;
  }
  
  /*******************************************************************************
  * drawPnt(...)
  *
  * Description: Draws the point on the screen, with the appropriate color and size
  *******************************************************************************/
  void drawPnt(int greenness)
  {
    ellipseMode(CENTER);  // Set ellipseMode to CENTER
    fill(redness,greenness,blueness);  // Set fill to gray (100)
    if (redness>0) redness=redness-5;
    if (blueness>0) blueness=blueness-5;
    if (radius>10) radius = radius-1;
    stroke(256,256,256);
    ellipse(x, y, radius, radius);  // Draw gray ellipse using CENTER mode
    fill(0,0,0);
    stroke(0,0,0);
    if(index_in_simple_poly!=-1) {
      text(""+index_in_simple_poly, x,y, 50, 50); 
      //text(""+i, x,y, 50, 50); 
    }
  }
  
  /*******************************************************************************
  * setNumber(index)
  *
  * Description: sets the index within the simple polygon. This is done because that
  * Number is displayed next to the Point at all times after the simple polygon was created
  *******************************************************************************/
  void setNumber(int index) {
    index_in_simple_poly = index;
  }
  
  /*void setAngle(double newangle) {
    angle = newangle;
  }*/  //used for simpleSort
  
  /*******************************************************************************
  * blinkRed()
  *
  * Description: Makes the point laerger and red. Effect will wear out after a few
  * itterations of draw.
  *******************************************************************************/
  void blinkRed() {
    redness = 255;
    blueness =0;
    radius = 35;
  }
  
  /*******************************************************************************
  * blinkBlue()
  *
  * Description: Makes the point laerger and blue. Effect will wear out after a few
  * itterations of draw.
  *******************************************************************************/
  void blinkBlue() {
    blueness = 255;
    radius = 25;
  }
  
  /*******************************************************************************
  * Bonus: drawBubble(...)
  *
  * Description: When displaying the heap this method draws a single bubble with 
  * the index in it in the given position on the screen
  *******************************************************************************/
  void drawBubble(int xpos, int ypos) {
    ellipseMode(CENTER);
    fill(256,256,256-yellowness);
    if(yellowness >0) yellowness = yellowness - 40;
    // draw index with circle around it
    int pos_corr = 0;
    if(i < 10) pos_corr = 5;
    ellipse(xpos+10,ypos+10,30,30);
    fill(0,0,0);
    text(""+i, xpos+pos_corr,ypos,50,50); 
    
    
  }
  
  /*******************************************************************************
  * Bonus: highlight()
  *
  * Description: highlights the Bubble displayed in heap display mode.
  *******************************************************************************/
  void highlight() {
    yellowness = 240; //(1 und 2 in rgb)
  }
  
  /*
  int x()
  {
    return x;
  }
  
  int y()
  { 
    return y;
  }
  
  int i()
  {
    return i;
  }
  */
  
  
}