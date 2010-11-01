import serial
from lxml import etree
import datetime

"""


guy@Guys-Desktop:~/Code/git/CurrentcostCC128$ python main.py 
    Traceback (most recent call last):
      File "main.py", line 34, in <module>
        xml = etree.XML(temp[0])
      File "lxml.etree.pyx", line 2512, in lxml.etree.XML (src/lxml/lxml.etree.c:48057)
      File "parser.pxi", line 1545, in lxml.etree._parseMemoryDocument (src/lxml/lxml.etree.c:71812)
      File "parser.pxi", line 1424, in lxml.etree._parseDoc (src/lxml/lxml.etree.c:70673)
      File "parser.pxi", line 938, in lxml.etree._BaseParser._parseDoc (src/lxml/lxml.etree.c:67442)
      File "parser.pxi", line 539, in lxml.etree._ParserContext._handleParseResultDoc (src/lxml/lxml.etree.c:63824)
      File "parser.pxi", line 625, in lxml.etree._handleParseResult (src/lxml/lxml.etree.c:64745)
      File "parser.pxi", line 565, in lxml.etree._raiseParseError (src/lxml/lxml.etree.c:64088)
    lxml.etree.XMLSyntaxError: Start tag expected, '<' not found, line 2, column 1
guy@Guys-Desktop:~/Code/git/CurrentcostCC128$ 






"""

ser = serial.Serial(port='/dev/CurrentcostCC128',
                    baudrate=57600,
                    bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    timeout=120)

fileTxt = open("dump.txt", "a")
fileLog = open("dump.log", "a")
dtd = etree.DTD("CurrentcostCC128.dtd")

fileTxt.write("\n\n\n<!-- Starting at " + str(datetime.datetime.now()) + "-->\n")
fileLog.write("Starting at " + str(datetime.datetime.now()) +"\n")

ser.open()

keepLooping = True
inputBuffer = ""
while(keepLooping):
	
	try:
		if ser.inWaiting() > 0:
			x = ser.read(ser.inWaiting())
			inputBuffer = inputBuffer + str(x)
			
			if inputBuffer.find("</msg>") > 0:
				temp = inputBuffer.split("</msg>", 1)
				inputBuffer = temp[1]
				temp[0] = temp[0]+"</msg>"
				xml = etree.XML(temp[0])
				if dtd.validate(xml):
					fileTxt.write(temp[0])
					fileTxt.flush()
					fileLog.write("Got msg\n")
					fileLog.flush()
				else:
					fileLog.write("Not valid 'DTD' (\n" + temp[0] + "\n)\n")
					fileLog.flush()
	
	except serial.SerialTimeoutException:
		print "TimeOut Error"
	except serial.SerialException:
		print "serial Error"
	except KeyboardInterrupt:
		print "Closing down"
		keepLooping = False
		
	#except Exception:
	#	print "Error!"

ser.close()
fileTxt.close()
