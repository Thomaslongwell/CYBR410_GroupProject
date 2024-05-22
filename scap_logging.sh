#!/bin/bash

# Set the directory where you want to save the .scap files
CAPTURE_FOLDER="/home/miah/Desktop/scap"

# Ensure the capture directory exists
#mkdir -p "$scap"

# This helps get the duration to wait before starting the next capture (30 minutes)
CAPTURE_INTERVAL=$((30 * 60))  # 30 minutes in seconds

# This is the maximum duration for script execution (4 hours in this case)
MAX_DURATION=$((4 * 60 * 60))  # 4 hours in seconds


# Get the start time of the script
START_TIME=$(date +%s)


echo "Starting new snapshot: scap${scap_count}"

# Infinite loop to keep capturing the system activity
while true; do
	# This will generate a filename with a timestamp
    
	#FILENAME="$CAPTURE_FOLDER/$(date +"%Y%m%d%H%M%S").scap"
	FILENAME="/home/miah/Desktop/scap/$(date +"%Y%m%d%H%M%S").scap"
	# Capture system events until the file reaches approximately 20MB
	sudo sysdig -C 20 -w "410scap"
    
    
	# Wait for 30 minutes before starting the next capture
	#sleep 1800
	#wait for 5 seconds before starting the next capture
	#sleep 5
    
    
done
