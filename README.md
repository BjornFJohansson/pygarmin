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

    (pygarmin) bjorn@bjorn-ThinkPad-T450s:~/python_packages/pygarmin$ sudo python pygarmin "usb:" info
    *** Product Info ***
    Forerunner205 Software Version 2.80
    GPS Product ID: 484
    Software version: 2.80

    (pygarmin) bjorn@bjorn-ThinkPad-T450s:~/python_packages/pygarmin$ sudo python garmin-sync.py
    Getting data from GPS (this might take a while)...
    Exporting to exports/2017-04-14T11:51:37Z.tcx
    Exporting to exports/2017-04-15T09:37:15Z.tcx
    Exporting to exports/2017-04-16T10:01:59Z.tcx
    Exporting to exports/2017-04-27T17:20:47Z.tcx
    Exporting to exports/2017-04-29T16:33:50Z.tcx
    (pygarmin) bjorn@bjorn-ThinkPad-T450s:~/python_packages/pygarmin$ 

The tcx files can be uploaded to [runkeeper](https://runkeeper.com/user/bjornfjohansson/profile) for example.
