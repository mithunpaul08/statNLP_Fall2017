package hw1
import java.io.{PrintWriter, StringWriter}

import com.typesafe.scalalogging.LazyLogging
import ch.qos.logback.classic.{Level, Logger}
import org.slf4j.LoggerFactory
import scala.io.Source

import scala.collection.mutable.ArrayBuffer
import scala.io.Source

object initializer extends App with LazyLogging{

  LoggerFactory.getLogger(org.slf4j.Logger.ROOT_LOGGER_NAME).asInstanceOf[Logger].setLevel(Level.INFO)

  val getLemmas=false;
  val getPos=false;
  val getPosLemmas=true;

  var inputFileForAdjTemplate = "src/main/resources/brown_sample.txt"
  try {



    engine.readBrownToMem(inputFileForAdjTemplate)
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