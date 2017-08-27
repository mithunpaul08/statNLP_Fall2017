package hw1
import java.io.{PrintWriter, StringWriter}

import com.typesafe.scalalogging.LazyLogging
import ch.qos.logback.classic.{Level, Logger}
import org.slf4j.LoggerFactory
import scala.io._

import scala.collection.mutable.ArrayBuffer
import scala.io.Source
import util.control.Breaks._

object initializer extends App with LazyLogging{

  LoggerFactory.getLogger(org.slf4j.Logger.ROOT_LOGGER_NAME).asInstanceOf[Logger].setLevel(Level.INFO)
  var getLemmas=false;
  var getPos=false;
  var getPosLemmas=false;


  var inputFileForAdjTemplate = "src/main/resources/brown_sample.txt"
  try {

    println("Hi, welcome to HW1 Stat NLP Fall 2017")



    breakable {
      while (true) {

         getLemmas=false;
         getPos=false;
         getPosLemmas=false;

        println("*************************************************")
        println("Type 0 to exit.")
        println("Type 1 for Qn 1.1: top 10 most frequent words .")
        println("Type 2 for Qn 1.2: top 10 most frequent POS tags .")
        println("Type 3 for Qn 1.3: top 10 most frequent word-POS tag pairs? .")

        println("Type your input here:")
        val typeOfProgram = StdIn.readLine()

        if (typeOfProgram == "0") {
          println("Sad to see you leave. Do come back again. Bye.")
          sys.exit;

        }
        else if (typeOfProgram == "1") {
          getLemmas=true;
        }
        else if (typeOfProgram == "2") {

          getPos=true;

        }
        else if (typeOfProgram == "3") {
          getPosLemmas=true;


        }

        engine.readBrownToMem(inputFileForAdjTemplate)
      }
    }
  }

  catch {


    case e: Exception => {


      // write the error to a log file
      val sw = new StringWriter
      e.printStackTrace(new PrintWriter(sw))
      logger.error(sw.toString)
      logger.error("Error occured. Going to exit")
      sys.exit(1)

    }
  }
}