/*--------------------------------------------------------------------------------------------
 * Author Lukas Wenzl
 * 
 * Implementation of a Stack
 *-------------------------------------------------------------------------------------------*/


class Stack {
 
ArrayList SA;


  Stack() { //init
      SA = new ArrayList();
      //size= 0;
      //Point test = new Point(1,2,3);
      //SA.add(test);
  }
  
  void push(Point P) {
      SA.add(P);
      println("added to stack: "+ P.x + " " + P.y, " " + P.i);
      P.blinkBlue();
  }
  
  /*******************************************************************************
  * top()
  *
  * Description: Returns the top element of the stack. if non existant it
  * returns null
  *******************************************************************************/
  Point top() {
    if (SA.size() >0) {
      return (Point) SA.get(SA.size()-1);
    } else {
      return null;
    }
  }
  
  /*******************************************************************************
  * nextToTop
  *
  * Description: Returns the second to top element of the stack. If non existant 
  * it returns null
  *******************************************************************************/
  Point nextToTop() {
    if (SA.size() >1) {
      return (Point) SA.get(SA.size()-2);
    } else {
      return null;
    }
  }
  
  /*******************************************************************************
  * pop()
  *
  * Description: deletes the top element of the stack.
  *******************************************************************************/
  void pop() {
    if (SA.size() >0 ) {
      Point P = top();
      println("removed from stack: "+ P.x + " " + P.y, " " + P.i);
      P.blinkRed();
      SA.remove(SA.size()-1);
      
    }
  }
  
  /*******************************************************************************
  * drawStack()
  *
  * Description: The Stack has the current supposed elements of the CH in it. Drawing 
  * it gives the current Stage of the Graham Scan Alg.
  *******************************************************************************/
  void drawStack() {
    for (int i =0; i < SA.size(); i++) {
      Point pnt1 = (Point) SA.get(i);
      pnt1.drawPnt(100);
      if(i>0) {
        Point pnt2 = (Point) SA.get(i-1);
        strokeWeight(3);
        stroke(0,100,0);
        line(pnt1.x,pnt1.y,pnt2.x,pnt2.y);
        strokeWeight(1);
        stroke(0,0,0);
      }
    }
  }
  
  /*******************************************************************************
  * finishHull()
  *
  * Description: Connects the last element of the CH to the first
  *******************************************************************************/
  void finishHull() {
    Point pnt1 = (Point) SA.get(0);
    Point pnt2 = (Point) SA.get(SA.size()-1);
    strokeWeight(3);
    stroke(0,100,0);
    line(pnt1.x,pnt1.y,pnt2.x,pnt2.y);
    strokeWeight(1);
    stroke(0,0,0);
  }
  
  
  
  
  
  
  
  
}