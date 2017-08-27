
 package hw1
 import com.typesafe.scalalogging.LazyLogging
import ch.qos.logback.classic.{Level, Logger}
 import org.slf4j.LoggerFactory
import scala.io.Source

object engine extends LazyLogging {
  LoggerFactory.getLogger(org.slf4j.Logger.ROOT_LOGGER_NAME).asInstanceOf[Logger].setLevel(Level.INFO)

  def readBrownToMem(fileToRead: String): scala.collection.mutable.Map[String, Int] = {


    var lines = Source.fromFile(fileToRead).getLines
    var htLemmas = scala.collection.mutable.Map[String, Int]()
    var htPos = scala.collection.mutable.Map[String, Int]()
    var htBoth = scala.collection.mutable.Map[String, Int]()

    for (lineFromInput <- lines) {

      if (lineFromInput != "") {
        var stringVersionOfTemplate = lineFromInput.split("\\s")

        //for each tuple, split based on /

        for (tuple <- stringVersionOfTemplate) {

          if (tuple != "") {



            val lemmaPos = tuple.split("/")

            if (lemmaPos.size > 1) {
              val lemma = getMyValue(0, lemmaPos).getOrElse("Error")
              val pos = getMyValue(1, lemmaPos).getOrElse("Error")


              //remove any pos with punctuations
              val myPattern = "[a-zA-Z]+".r
              if (myPattern.findFirstIn(pos) != None) {

                if (initializer.getLemmas == true) {
                  //add all lemmas to a hash table
                  if (htLemmas.contains(lemma)) {
                    var count = htLemmas(lemma)
                    count = count + 1
                    htLemmas(lemma) = count
                  }
                  else {
                    htLemmas += (lemma -> 1)
                  }

                }

                if (initializer.getPos == true) {
                  //find top 10 pos most frequent pos tags
                  if (htPos.contains(pos)) {
                    var count = htPos(pos)
                    count = count + 1
                    htPos(pos) = count
                  }
                  else {
                    htPos += (pos -> 1)
                  }
                }

                if (initializer.getPosLemmas == true) {
                  //find top 10 pos most frequent posLemma tags
                  if (htBoth.contains(tuple)) {
                    var count = htBoth(tuple)
                    count = count + 1
                    htBoth(tuple) = count
                  }
                  else {
                    htBoth += (tuple -> 1)
                  }
                } 


              }
              else {
                //println("found dot.")
                //  logger.info("Found a pattern that is not an alphabet. Its value is:" + pos)
              }


            }
          }

        }


      }
    }

    if (initializer.getLemmas == true) {
      //sort the hashtable by value and pick top 10
      val htLemmas_sorted = scala.collection.immutable.ListMap(htLemmas.toSeq.sortWith(_._2 > _._2): _*)
      println("Lemmas top 10 :\n" + htLemmas_sorted.take(10).mkString("\n"))
    }

    if (initializer.getPos == true) {
      val htPos_sorted = scala.collection.immutable.ListMap(htPos.toSeq.sortWith(_._2 > _._2): _*)
      println("POS top 10 :\n" + htPos_sorted.take(10).mkString("\n"))
    }

    if (initializer.getPosLemmas == true) {
      val htBoth_sorted = scala.collection.immutable.ListMap(htBoth.toSeq.sortWith(_._2 > _._2): _*)
      println("word-POS top 10 :\n" + htBoth_sorted.take(10).mkString("\n"))

    }
    return htLemmas;
  }

  def getMyValue(index: Int, mylist: Array[String]): Option[String] = {
    try {
      Some(mylist(index))
    }
    catch {
      case e: Exception => None
    }

  }
}