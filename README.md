BlueRacer
===========

A Python script to email you specified comics every day.


The [Blue Racer](https://en.wikipedia.org/wiki/Coluber_constrictor_foxii) is a snake species found in the American Mid-West.

Usage
===========

**./blueracer.py _[pageURL]_ _[comicTitle]_ _[email]_**  
Example: ./blueracer.py http://gocomics.com/Garfield/ Garfield epicwolverine@example.com

BlueRacer is written in Python 2.7.3. While Python 2.7.3 is the only version of Python BlueRacer officially supports, it may work in older or newer versions of Python but this has not been tested. BlueRacer also requires a SMTP server to be installed and running in order to send emails. I have this working on Linux with sendmail, but it should also work on Windows (and other platforms) if you can find a one to use.

Supported Websites
===========
* http://gocomics.com/[comic]/

### Planned Support
* http://xkcd.com
* http://dilbert.com/
* http://arcamax.com/thefunnies/[comic]/
 
License
===========
BlueRacer is licensed under the GNU General Public License V3. A full copy of the license can be found in the LICENSE file in this repository or at http://www.gnu.org/licenses/.    
Licence tl;dr: http://www.tldrlegal.com/license/gnu-general-public-license-v3-(gpl-3)
