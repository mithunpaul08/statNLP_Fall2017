package hw1

import com.typesafe.scalalogging.LazyLogging
 import ch.qos.logback.classic.{Level, Logger}
 import org.slf4j.LoggerFactory
 import scala.collection.mutable.ListBuffer
 import scala.io.Source

object qn2 extends LazyLogging {
  LoggerFactory.getLogger(org.slf4j.Logger.ROOT_LOGGER_NAME).asInstanceOf[Logger].setLevel(Level.INFO)

  def readEmbCalcDot(fileToRead: String) = {


    val lines = Source.fromFile(fileToRead).getLines
    var htWordEmb = scala.collection.mutable.Map[String, ListBuffer[Double]]()


    for (lineFromInput <- lines) {
      var word = ""
      var embeddings = new scala.collection.mutable.ListBuffer[Double]()

      if (lineFromInput != "") {
        val stringVersionOfTemplate = lineFromInput.split("\\s")




        //for each tuple, check if its string or Double
        for (tuple <- stringVersionOfTemplate) {


          if (tuple != "") {

            //assume that if the tuple contains a letter it will be the lemma. Else the embedding value
            val myPattern = "[a-zA-Z]+".r
            if (myPattern.findFirstIn(tuple) != None) {
              word = tuple
            }
            else {
              //if its a double value, add it all into a list buffer
              checkIfDouble(tuple) match {
                case Some(i) => {
                  embeddings += i
                }
                case None => {
                  println("the given value is not a Double:" + tuple)
                }
              }

            }
          }
        }

            //once you have all the embeddings of this word stored in a listbuffer.
            // create a hashtable that maps each word to its embeddings
            if (!(htWordEmb.contains(word))) {
              htWordEmb += (word -> embeddings)
            }
            else {
              println("error, the word already exists in htWordEmb")
            }




        //println("finished first sentence. The word is:"+word)
        //println("its embedding list is:"+embeddings.mkString(","))



      }


    }

    /*by now every word and its embeddings are added to htWordEmb.
   * Pick the vector of home, dot product with each of the other 2999 words, add to a hashtable
   * sort the list, pick top 10*/



      val home = "home"
      var homeEmbed = ListBuffer[Double]()

      if (htWordEmb.contains(home)) {
        homeEmbed = htWordEmb(home)
      }
      else {
        println("error, the word home doesnt  exist in htWordEmb")
      }


      //create a hashtable which stores the words and its dot product value with "home"
      var htWordDot = scala.collection.mutable.Map[String, Double]()

      //go through all the keys in htWordEmb and get their dot product with home. Except home itself
      for ((k, v) <- htWordEmb) {
        if (k != "home") {
          val dotProduct = findDotProduct(homeEmbed, v)
          htWordDot += (k -> dotProduct)
        }
      }
    if (initializer.getHomeSimilar == true) {

      //sort the hashtable by value and pick top 10
      val htWordDot_sorted = scala.collection.immutable.ListMap(htWordDot.toSeq.sortWith(_._2 > _._2): _*)
      println("\ntop 10 most similar words to \"home\" are :\n" + htWordDot_sorted.take(10).mkString("\n"))
    }

    if (initializer.getHomeDissimilar == true) {

      //reverse sort the hashtable by value and pick top 10
      val htWordDot_sorted = scala.collection.immutable.ListMap(htWordDot.toSeq.sortWith(_._2 < _._2): _*)
      println("\ntop 10 most dissimilar words to \"home\" :\n" + htWordDot_sorted.take(10).mkString("\n"))
    }
  }


  //takes two ListBuffer(Double) as input and returns its dot product
  def findDotProduct(x: ListBuffer[Double], y: ListBuffer[Double]): Double = {
    //run through both the lists and multiply the corresponding values

    var dot: Double = 0
    for ((m, a) <- x zip y) {
      dot = dot + (m * a)
    }
    return dot
  }

  def getMyValue(index: Int, mylist: Array[String]): Option[String] = {
    try {
      Some(mylist(index))
    }
    catch {
      case e: Exception => None
    }

  }

  //take a string, and return an int if its an int
  def checkIfDouble(value: String): Option[Double] = {
    try {
      Some(value.toDouble)
    }
    catch {
      case ex: NumberFormatException => None
    }
  }
}

