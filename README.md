BlueRacer
===========

A Python script to email you specified comics every day.


The [Blue Racer](https://en.wikipedia.org/wiki/Coluber_constrictor_foxii) is a snake species found in the American Mid-West.

Usage
===========

    ./blueracer.py [pageURL] [comicTitle] [email]  
    ./blueracer.py http://gocomics.com/calvinandhobbes/ "Calvin and Hobbes" epicwolverine@example.com

BlueRacer is written in Python 2.7.3. While Python 2.7.3 is the only version of Python BlueRacer officially supports, it may work in older or newer versions of Python but this has not been tested. BlueRacer also requires a SMTP server to be installed and running in order to send emails. I have this working on Linux with sendmail, but it should also work on Windows (and other platforms) if you can find a one to use. While not required to function, BlueRacer was designed to be run every morning with an automation program such as crontab. 

    30 0 * * * python ~/BlueRacer/blueracer.py http://gocomics.com/garfield Garfield epicwolverine@example.com

Supported Websites
===========
* http://gocomics.com/[comic]/
* http://arcamax.com/thefunnies/[comic]/
* http://commitstrip.com/en/ and http://commitstrip.com/fr/
* http://xkcd.com/ (partial; doesn't pass title and title text yet)

Future Plans
===========
* Add more websites
    * http://www.foxtrot.com/
* Auto-checks for comics and saves image urls (to prevent sending duplicates and allow for other features)
* Create web front-end and sign-up service
 
License
===========
BlueRacer is licensed under the GNU General Public License V3. A full copy of the license can be found in the LICENSE file in this repository or at http://www.gnu.org/licenses/.    
Licence tl;dr: http://www.tldrlegal.com/license/gnu-general-public-license-v3-(gpl-3)
