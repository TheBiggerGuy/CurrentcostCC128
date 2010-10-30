import serial
from lxml import etree
import datetime

ser = serial.Serial(port='/dev/ttyUSB0',
                    baudrate=57600,
                    bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    timeout=120)

fileTxt = open("dump.txt", "a")
dtd = etree.DTD("currentcost.dtd")

fileTxt.write("\n\n\n<!-- Starting at " + str(datetime.datetime.now()) + "-->\n")

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
					print "Got msg"
				else:
					print "Not valid 'DTD' (" + temp[0] + ")"
	
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
