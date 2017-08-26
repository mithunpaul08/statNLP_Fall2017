
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


              //remove anything with punctuations
              val myPattern = "[a-zA-Z]+".r
              if (myPattern.findFirstIn(pos) != None) {


                if (htLemmas.contains(lemma)) {
                  var count = htLemmas(lemma)
                  count = count + 1
                  htLemmas(lemma) = count
                }
                else {
                  htLemmas += (lemma -> 1)
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

    val htLemmas_sorted= scala.collection.immutable.ListMap(htLemmas.toSeq.sortWith(_._2>_._2): _*)

    println("Lemmas top 10 :\n" + htLemmas_sorted.take(10).mkString("\n"))
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