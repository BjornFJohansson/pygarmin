PyGarmin
========

This repository contains code mostly from [quentinsf/pygarmin](https://github.com/quentinsf/pygarmin)


It contains a self contained folder where it should be possible to download tcx files from old garmin watches such as
the Forerunner 205.

Usage:

1. Dowload this repository to your computer
2. Open the folder in terminal.
3. type `sudo python pygarmin "usb:" info` at the command line and hit return.
This produces the following text from my watch:

*** Product Info ***
Forerunner205 Software Version 2.80
GPS Product ID: 484
Software version: 2.80

4. Then type `sudo python garmin-sync.py` and hit return.
This should copy all tcx files from the watch to a folder called "exports".

The tcx files can be uploaded to runkeeper for example
