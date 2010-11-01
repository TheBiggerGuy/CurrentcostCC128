"Simple SAX example, updated for Python 2.0+"
import xml.sax
from xml.sax.handler import *
from optparse import OptionParser

class XML2CSV(ContentHandler):
	"""Crude extractor for xml to CSV """
	
	def __init__(self, csvFile):
		self.outFile = csvFile
	
	def startDocument(self):
		print "--- Begin Document ---"
		self.outFile.write("src, dsb, time, tmpr, sensor, id, type, ch1_watts, ch2_watts\n")
	
	def startElement(self, name, attrs):
		None
	
	def endElement(self, name):
		if name == "ch1" or name == "ch2" or name == "watts" or name == "data":
			print "no"
		if name == "msg":
			self.outFile.write("\n")
		else:
			self.outFile.write(",")
	
	def characters(self, ch):
		self.outFile.write( ch.strip("\n\t,") )


if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="write report to FILE", metavar="FILE", default="none")

    (options, args) = parser.parse_args()
    
    if options.filename == "none":
        exit()

    parser = xml.sax.make_parser()
    
    fileCSV = open("dump.csv", "w")
    handler = XML2CSV(fileCSV)
    parser.setContentHandler(handler)
    parser.parse(options.filename)
