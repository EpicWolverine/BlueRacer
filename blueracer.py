#!/usr/bin/python -tt
# Copyright 2014 Brendan Ferracciolo
# 
# This file is part of BlueRacer.
#
# BlueRacer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BlueRacer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BlueRacer. If not, see <http://www.gnu.org/licenses/>.

"""<insert man page here>"""

import sys          # for various I/O functions
import urllib2      # URL fetching and handleing
import re           # regular expression support
import smtplib      # email sending support
from email.mime.multipart import MIMEMultipart   # email creation
from email.mime.text import MIMEText             # more email creation
import time         # datetime support

def main():
    sendEmail(sys.argv[3], '"BlueRacer" <test@example.com>', sys.argv[2], getComic(sys.argv[1]))

    
def getComic(url):
    try:
        page = urllib2.urlopen(urllib2.Request(url,headers={'User-Agent': 'Mozilla/5.0'}))
        #print page.read()
        
        if re.search(r'gocomics.com', url):
            comic = re.search(r'<meta\sname="twitter:image"\scontent="([\w\s\W]+?)"\s/>', page.read())
            if comic:
                #print comic.group(1)
                return comic.group(1)
            else:
                print "Comic image not found."
                return
        else:
            print "This website is not supported."
            return
    except IOError:
        print 'problem reading url:', url
        
def sendEmail(receiver, sender, comicName, imgURL):
    # create datetime string
    emailDate = time.strftime("%A, %B %d, %Y")
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = comicName + " for " + emailDate
    msg['From'] = sender
    msg['To'] = receiver

    # Create the body of the message (a plain-text and an HTML version).
    text = comicName + " for " + emailDate + "\n" + imgURL + "\n\nSent with BlueRacer (https://github.com/EpicWolverine/BlueRacer)"
    html = """\
    <html>
      <head></head>
      <body>
        <center>
            <p>
               <h2>""" + comicName + """ for """ + emailDate + """</h2><br>
               <img src=\"""" + imgURL + """\" alt=\"""" + imgURL + """\"></img><br>
               <br>
               Sent with <a href=\"https://github.com/EpicWolverine/BlueRacer\">BlueRacer</a>.
            </p>
        </center>
      </body>
    </html>
    """
    
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('localhost')
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(sender, receiver, msg.as_string())
    s.quit()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
