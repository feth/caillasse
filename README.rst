Caillasse
=========

dev status
----------
I'm currently working on implementation, it's not working yet.

apropos
-------
This is a basic shared expenses balance calculator GUI.
When I say basic, I mean that it can handle most corner cases. You need to install velat (and its dependency peinard) to run Caillasse.
Then you may want to read velat's Readme.

dependencies
------------
- velat (current git master HEAD)
- peinard (quite stable)
Both can be fetched from github

install
-------
For the time being:

git clone this and deps
mkvirtualenv caillasse
python setup.py install in peinard, then velat, then caillasse.
then you can run 'caillasse'
