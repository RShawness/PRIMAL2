#!/bin/bash

while true; do
    # Run your Python script
    python driver.py

    # Check exit status
    if [ $? -eq 139 ]; then
        echo "Detected segfault, restarting script..."
        sleep 10  # Optional: to prevent immediate respawning
    else
        break  # Exit the loop if the script exits normally
    fi
done
