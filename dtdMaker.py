#!/usr/bin/env python3


print("""<?xml version="1.0" encoding="UTF-8"?>
<!--
    Author:
        Guy Taylor <thebigguy.co.uk@gmail.com>
    Refs:
        http://www.currentcost.com/cc128/xml.htm
    
    Copyright (c) 2010, Guy Taylor
    All rights reserved.
    
    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the Guy Taylor nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.
    
    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
    ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL GUY TAYLOR BE LIABLE FOR ANY
    DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
    (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
    LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
    ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
    SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

-->

<!ELEMENT msg (src,dsb,time,((tmpr,sensor,id,type,ch1?,ch2?,ch3?)|hist))>

<!-- Real-Time Output -->
<!ELEMENT src (#PCDATA)>
<!ELEMENT dsb (#PCDATA)>
<!ELEMENT time (#PCDATA)>
<!ELEMENT tmpr (#PCDATA)>
<!ELEMENT sensor (#PCDATA)>
<!ELEMENT id (#PCDATA)>
<!ELEMENT type (#PCDATA)>
<!ELEMENT ch1 (watts)>
<!ELEMENT ch2 (watts)>
<!ELEMENT ch3 (watts)>

<!ELEMENT watts (#PCDATA)>


<!-- History Output -->


<!ELEMENT hist (dsw,type,units,data+)>

<!ELEMENT dsw (#PCDATA)>
<!ELEMENT units (#PCDATA)>

""")

print("""

<!ELEMENT data (sensor,
	(
		(h001?,h002?,h003?,h004?,h005?,h006?,h007?,h008?,h009?,h010?,h011?,h012?,
		""", end='')
for i in range(13, 744):
    if i < 743:
        print("h{0}?,".format( str(i).zfill(3) ), end='')
    else:
        print("h{0}?)".format( str(i).zfill(3) ), end='')
    if i % 12 == 0:
        print("\n		", end='')
        
print("""
	|
		(d001?,d002?,d003?,d004?,d005?,d006?,d007?,d008?,d009?,d010?,d011?,d012?,
		d013?,d014?,d015?,d016?,d017?,d018?,d019?,d020?,d021?,d022?,d023?,d024?,
		d025?,d026?,d027?,d028?,d029?,d030?,d031?,d032?,d033?,d034?,d035?,d036?,
		d037?,d038?,d039?,d040?,d041?,d042?,d043?,d044?,d045?,d046?,d047?,d048?,
		d049?,d050?,d051?,d052?,d053?,d054?,d055?,d056?,d057?,d058?,d059?,d060?,
		d061?,d062?,d063?,d064?,d065?,d066?,d067?,d068?,d069?,d070?,d071?,d072?,
		d073?,d074?,d075?,d076?,d077?,d078?,d079?,d080?,d081?,d082?,d083?,d084?,
		d085?,d086?,d087?,d088?,d089?,d090?)
	|
		(m001?,m002?,m003?,m004?,m005?,m006?,m007?,m008?,m009?,m010?,m011?,m012?,
		""", end='')
for i in range(13, 85):
    if i < 84:
        print("m{0}?,".format( str(i).zfill(3) ), end='')
    else:
        print("m{0}?)".format( str(i).zfill(3) ), end='')
    if i % 12 == 0 and not i == 84:
        print("\n		", end='')
        
print("""
	)
)>

<!ELEMENT sensor (#PCDATA)>

""")

print("\n<!-- Two-Hourly History Store -->\n")
for i in range(0, 745):
    print("<!ELEMENT h{0} (#PCDATA)>".format(str(i).zfill(3)))

print("\n<!-- Daily History Store -->\n")
for i in range(1, 91):
    print("<!ELEMENT d{0} (#PCDATA)>".format(str(i).zfill(3)))

print("\n<!-- Monthly History Store -->\n")
for i in range(1, 85):
    print("<!ELEMENT m{0} (#PCDATA)>".format(str(i).zfill(3)))

