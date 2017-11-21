/*--------------------------------------------------------------------------------------------
 * Author Lukas Wenzl
 * 
 * 
 * description: This class lets you read a file formated in the following way: first line: number of points
 *               the in each line x,y and index
 *              Can do some elementary error handeling like misspelled file names and handels
 *              points that are outside of the canvas by throwing them away.
 *-------------------------------------------------------------------------------------------*/

import java.awt.Rectangle;


class ReadFile {
  
  BufferedReader reader;
  String line;
  int size;
  int errors;

  Point[] Anew;
  
  ReadFile(String filename)
  {
    reader = createReader(filename);  
    line = "";
    readLine();
    size = int(line); //first line of file right?
    errors = 0;
  }
  
  /*******************************************************************************
  * getArray(...)
  *
  * Description: Returns the array of points in the file
  *******************************************************************************/
  Point[] getArray(String filename)
  {

    Anew = new Point[size];
    boolean endreached = false;
    int i = 0;
    while(endreached == false)
    {
      line = readLine();

      if (line == null || line.length() < 3) { //second one in case there is an empty line at the end of the file
         // Stop reading because of an error or file is empty
         noLoop(); 
         endreached = true;
         try {
           reader.close();
         } catch (IOException e) {}
       } else {
         Point pnt = convertLine();
         Rectangle frame = new Rectangle(0, 0, 800, 500);
         if (frame.contains(pnt.x, pnt.y) ){
          Anew[i] = pnt;
          i++;
         }
         
       }
    }
    size = i;
    //println(A[1].x);
    return Anew;
  }
  
  /*******************************************************************************
  * readLine()
  *
  * Description: Reads one line of the file
  *******************************************************************************/
  String readLine()
  {
    try {
      line = reader.readLine();
    } catch (IOException e) {
      e.printStackTrace();
      line = null;
    }
    return line;
  }
  
  /*******************************************************************************
  * comvertLine()
  *
  * Description: Converts Line of file into a Point object and returns it.
  *******************************************************************************/
  Point convertLine()
  {
     String[] pieces = split(line, " ");//TAB);
     int x = int(pieces[0]);
     int y = int(pieces[1]);
     int i = int(pieces[2]);
     println("Point " + i + " at pos "+x+", " + y);
     Point pnt = new Point(x,y,i);
     pnt.blinkBlue();
     return pnt;
     
   }
  
  
}