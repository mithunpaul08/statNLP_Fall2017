/*--------------------------------------------------------------------------------------------
 * Author Lukas Wenzl
 * 
 first easy algorithm, not used in final algorithm, can be reactivatied with the code in 
 medthod simplePoly that is commented out
 
 NOT USED ANYMORE
 *-------------------------------------------------------------------------------------------*/

/*class SimpleSort{
  Point[] A; //for cos of angles
  int A_size;
  
  SimpleSort(Point[] revA, int revA_size) {
    A_size = revA_size;
    A = revA;
  }
  
  void sort() {
    for (int i=0; i<A_size-1; i++) {
      for (int j=i+1; j<A_size; j++) {
       if(A[j].angle > A[i].angle) {
          swap(i, j); 
        }
      }
    }
  }
  
  /*******************************************************************************
  * isRightTurn(...)
  *
  * Description: determines whether while driving from point 1 to 2 to 3 you turn right
  *******************************************************************************//*
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
  
  void swap(int i, int j) {
    Point temp = A[i];
    A[i] = A[j];
    A[j] = temp;
  }
}*/