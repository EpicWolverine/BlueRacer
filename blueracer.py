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


import sys
import urllib2
import re

def main():
    wget(sys.argv[1])

    
def wget(url):
    try:
        
        page = urllib2.urlopen(urllib2.Request(url,headers={'User-Agent': 'Mozilla/5.0'}))
        #print page.read()
        
        if re.search(r'gocomics.com', url):
            comic = re.search(r'<meta\sname="twitter:image"\scontent="([\w\s\W]+?)"\s/>', page.read())
            if comic:
                print comic.group(1)
            else:
                print comic
        else:
            print "This website is not supported."
    except IOError:
        print 'problem reading url:', url

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()