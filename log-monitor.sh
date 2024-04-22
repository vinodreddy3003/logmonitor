#!/bin/bash

# Function to gracefully stop the monitoring loop
function stop_monitoring {
    echo "log monitoring stopped due to keyboard interruption..."
    # Kill the tail process
    kill -SIGTERM $TAIL_PID
    # Remove the log file
    rm -f logs.txt
    exit
}

# Trap the SIGINT signal (Ctrl+C) and call the stop_monitoring function
trap stop_monitoring SIGINT

# Run the Python script in the background and redirect its output to a log file
python monitor.py > logs.txt &

# Get the PID of the tail process
TAIL_PID=$!

# Monitor the log file for new entries
tail -f logs.txt &

# Wait for the tail process to finish
wait $TAIL_PID
