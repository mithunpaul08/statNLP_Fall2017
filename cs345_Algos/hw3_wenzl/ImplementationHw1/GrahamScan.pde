/*--------------------------------------------------------------------------------------------
 * Author Lukas Wenzl
 * 
 * Implementation of the Graham Scan, will also handle the operations on the stack
 *-------------------------------------------------------------------------------------------*/


class GrahamScan {

Point[] A;
int A_size;
Stack S;

  /*******************************************************************************
 * GrahamScan(...)
 *
 * Description: initializes the scan. Already adds the first two elements to the 
                 stack because we already know what they are.
 *******************************************************************************/
  GrahamScan(Point[] revA, int revA_size, Stack revStack) {
    A = revA;
    A_size = revA_size;
    S = revStack;
    S.push(A[0]);
    if(A_size > 1) {
      S.push(A[1]);
      
    }
    
  }
  
  /*******************************************************************************
 * doStep()
 *
 * Description: Does one step of the Graham Sort Algorithm
 *******************************************************************************/
  void doStep(int i) {
    while (isRightTurn(S.nextToTop(), S.top(), A[i])) {
      S.pop();
    }
    S.push(A[i]);
  }
  
  
  /*******************************************************************************
  * isRightTurn(...)
  *
  * Description: determines whether while driving from point 1 to 2 to 3 you turn right
  *******************************************************************************/
  boolean isRightTurn(Point one, Point two, Point three) {
    PVector vec1to2 = new PVector(two.x-one.x, two.y-one.y, 0);
    PVector vec2to3 = new PVector(three.x-two.x, three.y-two.y, 0);
    PVector cross = vec1to2.cross(vec2to3);  // cross product is orientated in z-direction, magnitude(=z component here) is the same thing as the "magic fomula" mentioned in the lecture
    if(cross.z > 0) {
      println("true");
      return true;
    } else {
      return false;
    }
  }
  
}