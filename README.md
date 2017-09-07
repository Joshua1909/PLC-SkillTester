# plcskilltester
This is the working project for the PLC Skill Tester.

As seen at CrikeyCon 2017.

![The PLC Skill Tester at CrikeyCon](/media/crikeycon.jpg?raw=true "PLC Skill Tester")

Background:
------

The idea was to create an interactive box/booth where people take turns in hacking some basic logic flaws in a PLC. The size and layout of the original box is similar to a “marble machine” you might see on YouTube, and the machine moves a ball around in a continuous cycle.
The box is driven by a single Velocio ACE PLC with 6 outputs, which run 3 stepper drivers/motors. The Velocio is programmed to have the “state” register remotely writable via Modbus, so by messing with the “state” register, people can get the motors to move at times that will cause the ball to “escape” the system.
There are 3 tracks where the ball can “escape”, and it falls down the green/yellow tracks and ejects a chocolate coin.


Prerequisites:
------

python - required for pymobus and interaction with PLC
  
* https://github.com/python

pymodbus - for reading/writing PLC registers over Modbus
  
* https://github.com/bashwork/pymodbus
 
Velocio ACE PLC - hardware for running system
  
* http://velocio.net/ace/
  
vBuilder and vFactory for programming the PLC and HMI respectively.
  
* http://velocio.net/vbuilder/
  
* http://velocio.net/vfactory/
  
  
Credits:
------
 
* Credit for the pymodbus script goes to Justin Searle. This script was modified from an example on his website:

* http://www.samuraistfu.org/resources/
  
  
Roadmap:
------

* There are a number of improvements and future features to introduce. I'll put pen to paper at some point.