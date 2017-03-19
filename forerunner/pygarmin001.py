#! /usr/bin/env python

import garmin

# Create a 'physical layer' connection using serial port
phys = garmin.UnixSerialLink("/dev/ttyS0")

# Create a Garmin object using this connection
gps = garmin.Garmin(phys)

# Get the waypoints from the GPS
# (This may take a little while)
waypoints = gps.getWaypoints()

# Print the waypoints
for w in waypoints:
    print w.ident,
    lat = garmin.degrees(w.slat)
    lon = garmin.degrees(w.slon)
    print lat, lon, w.cmnt