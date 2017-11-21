/*--------------------------------------------------------------------------------------------
 * Author Lukas Wenzl
 * 
 * Implementation of the Heap Sort Algorithm. Sorts in O(n log(n)) and sorts in place
 *-------------------------------------------------------------------------------------------*/


class Heap{
  Point[] A;
  int heap_size;
  int A_size;
  
  //first point will not be used for heap structure, it is the 'bottom' point we compare all the others to to determine how ccw they are
  Heap(Point[] revA, int revA_size, int controll_point){
    A = revA;  //sorting will be done in place
    heap_size = revA_size-1;
    A_size = revA_size;
    if(controll_point>0) swap(0,controll_point);
  }
  
  /*******************************************************************************
 * buildMaxHeap()
 *
 * Description: initializes the the heap.
 *******************************************************************************/
  void buildMaxHeap() {
    for(int i= (int) (heap_size/2); i >= 1; i--) {
      maxHeapify(i);
    }
    /*for (int i= 0; i<heap_size;i++) {
      Point pnt = A[i];
      println("Point " + pnt.i + " at pos "+pnt.x+", " + pnt.y + " index: " + i);
    }*/
  }
  
  /*******************************************************************************
 * maxHeapify
 *
 * Description: Starts at i. If all the children of i are already sorted this method sorts 
                 the whole subtree starting from i into the right order IMPORTANT: starts at 1!!!
 *******************************************************************************/
  void maxHeapify(int i) {
    int l = 2*i;
    int r = 2*i+1;
    int largest = i;
    
    if(l<= heap_size && isMoreCCW(A[largest],A[l])) largest=l;
    
    if(r<= heap_size && isMoreCCW(A[largest],A[r])) largest = r;
    
    if(largest != i) {
      swap(largest,i);
      maxHeapify(largest);
    }
  }
  
  /*******************************************************************************
 * del_max()
 *
 * Description: deletes the maximum from the heap and brings it to the former last place
                of the heap
 *******************************************************************************/
  void del_max() {
    if(heap_size > 0) {
      swap(1, heap_size);
      heap_size--;
      maxHeapify(1);
    }
  }
  
  /*******************************************************************************
 * sort_CCW()
 *
 * Description: Once Heap is initialized this method sorts the Array CCW
 *******************************************************************************/  
  void sort_CCW() {
    while(heap_size>0) {
      del_max();
    }    
    
  }
  
  /*******************************************************************************
 * swap(...)
 *
 * Description: Switches the elements of A with the indizes one and two
 *******************************************************************************/
  void swap(int one, int two) {
    Point temp = A[two];
    A[two] = A[one];
    A[one] = temp;
    
  }
  
  
  /*******************************************************************************
  * isMoreCCW(...)
  *
  * Description: determines whether one is more CCW than two while roating around the starting point A[0]
  *******************************************************************************/
  boolean isMoreCCW(Point one, Point two) {
    
    PVector vec1to2 = new PVector(two.x-one.x, two.y-one.y, 0);
    PVector vec0to1 = new PVector(one.x-A[0].x, one.y-A[0].y, 0);
    PVector cross = vec1to2.cross(vec0to1);  // cross product is orientated in z-direction, magnitude(=z component here) is the same thing as the "magic fomula" mentioned in the lecture
    if(cross.z > 0) {
      //println("true");
      return true;
    } else {
      return false;
    }
    
  }
    
  /*******************************************************************************
 * displayHeap()
 *
 * Description: BONUS: displays the heap
 *******************************************************************************/
  void displayHeap() {
    stroke(0,0,0);
    fill(0,0,0);
    text("Heap: ", 50,30,50,50); 
    int y=0;
    int x=0;
    int layer = 0;
    int max_points_in_layer = 0;
    float width_screen = 800;
    int pos_corr = 0;
    for (int i=1; i<heap_size; i++) {
      layer = (int) ((log((float) i) / log(2)) );
      
      max_points_in_layer = (int) pow(2, layer);
      x= (int) ((width_screen/(max_points_in_layer+1))* (i- max_points_in_layer+1));
      y= 40*(layer+1);
      
      A[i].drawBubble(x,y);
      
      
      //println("layer: " +layer, "x " + x + " y:  " + y);
    }
      
  }
  
  /*******************************************************************************
 * HeapHighlight(int v)
 *
 * Description: as described on problem set: "a recursive method called 'HeapHighlight(v)' that highlights the points at the subtree rooted at H[v].
Start from the root of the heap. It should print these keys in an postoder order (LRD); Upon visiting a node
v, Heaphighlight(v) should first highlight the nodes of its left subtree, then the nodes of its right subtree,
and only then highlight its very own key."
 *******************************************************************************/
  void HeapHighlight(int v) {
      if(2*v <= heap_size) HeapHighlight(2*v);
      if(2*v+1 <= heap_size) HeapHighlight(2*v+1);
      A[v].highlight();
    
  }
}