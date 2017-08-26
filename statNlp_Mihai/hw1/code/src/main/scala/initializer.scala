package hw1


import java.io.{PrintWriter, StringWriter}


import scala.collection.mutable.ArrayBuffer
import scala.io.Source

object initializer extends App  {


  var inputFileForAdjTemplate = "src/main/resources/brown_sample.txt"

  engine.readBrownToMem(inputFileForAdjTemplate)

}