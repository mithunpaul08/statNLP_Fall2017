
 package hw1

import scala.io.Source
import scala.collection.mutable._

object engine {

  def readBrownToMem(fileToRead: String): Map[String, Int] = {


    var lines = Source.fromFile(fileToRead).getLines
    var htLemmas = Map[String, Int]()

    for (lineFromInput <- lines) {

      if (lineFromInput != "") {
        var stringVersionOfTemplate = lineFromInput.split("\\s")
        println("stringVersionOfTemplate:" + stringVersionOfTemplate(1))
        //for each tuple, split based on /

        for (tuple <- stringVersionOfTemplate) {

          if (tuple != "") {
            println("tuple:" + tuple)
            val lemmaPos = tuple.split("/")


            val lemma = getMyValue(0, lemmaPos).getOrElse("Error")
            val pos= getMyValue(1, lemmaPos).getOrElse("Error")

            println("lemma:" + lemma)

            println("POS:"+pos)

            if(htLemmas.contains(lemma))
              {
                var count=htLemmas(lemma)
                count=count+1
                htLemmas(lemma)=count
              }
            else
            {
              htLemmas+=(lemma->1)
            }


          }

        }


      }
    }

    scala.collection.immutable.ListMap(htLemmas.toSeq.sortBy(_.2))

    println("htlemmas:"+htLemmas.mkString("\n"))


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