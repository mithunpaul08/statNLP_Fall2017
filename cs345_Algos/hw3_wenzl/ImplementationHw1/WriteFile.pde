/*--------------------------------------------------------------------------------------------
 * Author Lukas Wenzl
 * 
 * descripition: makes it possible to write result into a file.
 *-------------------------------------------------------------------------------------------*/


class WriteFile {
  
  PrintWriter output;

  
  WriteFile(String filename)
  {
     output = createWriter(filename);
  }
  
  
  /*******************************************************************************
  * saveData(...)
  *
  * Description: writes a list of points into the file
  *******************************************************************************/
  void saveData(ArrayList SA) {
    
    for(int i = 0; i < SA.size(); i++) {    
      Point P = (Point) SA.get(i);
       output.println(P.x + " " + P.y + " " + P.i  );  
     }
     
     
  }
  
  /*******************************************************************************
  * closeWriter()
  *
  * Description: closes the writer
  *******************************************************************************/
  void closeWriter() {
    output.flush();
    output.close();
  }
  
  
}