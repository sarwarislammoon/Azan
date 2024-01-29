#!/bin/bash

# Function to check if the network is available
function is_network_available {
    ping -c 1 google.com > /dev/null 2>&1
    return $?
}

# Wait until the network is available
while ! is_network_available; do
    sleep 10
done

# Now that the network is available, run your command

#/usr/bin/python3 /home/sarwar_rpi_4/Desktop/Azan/azan.py >> /home/sarwar_rpi_4/Desktop/Azan/logfile.log 2>&1
nohup /usr/bin/python3 /home/sarwar_rpi_4/Desktop/Azan/test.py >> /home/sarwar_rpi_4/Desktop/Azan/logfile.log 2>&1 &



